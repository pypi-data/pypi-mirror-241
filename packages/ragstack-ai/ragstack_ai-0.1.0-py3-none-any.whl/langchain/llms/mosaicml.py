from typing import Any, Dict, List, Mapping, Optional

import requests

from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM
from langchain.llms.utils import enforce_stop_tokens
from langchain.pydantic_v1 import Extra, root_validator
from langchain.utils import get_from_dict_or_env

INSTRUCTION_KEY = "### Instruction:"
RESPONSE_KEY = "### Response:"
INTRO_BLURB = (
    "Below is an instruction that describes a task. "
    "Write a response that appropriately completes the request."
)
PROMPT_FOR_GENERATION_FORMAT = """{intro}
{instruction_key}
{instruction}
{response_key}
""".format(
    intro=INTRO_BLURB,
    instruction_key=INSTRUCTION_KEY,
    instruction="{instruction}",
    response_key=RESPONSE_KEY,
)


class MosaicML(LLM):
    """MosaicML LLM service.

    To use, you should have the
    environment variable ``MOSAICML_API_TOKEN`` set with your API token, or pass
    it as a named parameter to the constructor.

    Example:
        .. code-block:: python

            from langchain.llms import MosaicML
            endpoint_url = (
                "https://models.hosted-on.mosaicml.hosting/mpt-7b-instruct/v1/predict"
            )
            mosaic_llm = MosaicML(
                endpoint_url=endpoint_url,
                mosaicml_api_token="my-api-key"
            )
    """

    endpoint_url: str = (
        "https://models.hosted-on.mosaicml.hosting/mpt-7b-instruct/v1/predict"
    )
    """Endpoint URL to use."""
    inject_instruction_format: bool = False
    """Whether to inject the instruction format into the prompt."""
    model_kwargs: Optional[dict] = None
    """Keyword arguments to pass to the model."""
    retry_sleep: float = 1.0
    """How long to try sleeping for if a rate limit is encountered"""

    mosaicml_api_token: Optional[str] = None

    class Config:
        """Configuration for this pydantic object."""

        extra = Extra.forbid

    @root_validator()
    def validate_environment(cls, values: Dict) -> Dict:
        """Validate that api key and python package exists in environment."""
        mosaicml_api_token = get_from_dict_or_env(
            values, "mosaicml_api_token", "MOSAICML_API_TOKEN"
        )
        values["mosaicml_api_token"] = mosaicml_api_token
        return values

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        _model_kwargs = self.model_kwargs or {}
        return {
            **{"endpoint_url": self.endpoint_url},
            **{"model_kwargs": _model_kwargs},
        }

    @property
    def _llm_type(self) -> str:
        """Return type of llm."""
        return "mosaic"

    def _transform_prompt(self, prompt: str) -> str:
        """Transform prompt."""
        if self.inject_instruction_format:
            prompt = PROMPT_FOR_GENERATION_FORMAT.format(
                instruction=prompt,
            )
        return prompt

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        is_retry: bool = False,
        **kwargs: Any,
    ) -> str:
        """Call out to a MosaicML LLM inference endpoint.

        Args:
            prompt: The prompt to pass into the model.
            stop: Optional list of stop words to use when generating.

        Returns:
            The string generated by the model.

        Example:
            .. code-block:: python

                response = mosaic_llm("Tell me a joke.")
        """
        _model_kwargs = self.model_kwargs or {}

        prompt = self._transform_prompt(prompt)

        payload = {"inputs": [prompt]}
        payload.update(_model_kwargs)
        payload.update(kwargs)

        # HTTP headers for authorization
        headers = {
            "Authorization": f"{self.mosaicml_api_token}",
            "Content-Type": "application/json",
        }

        # send request
        try:
            response = requests.post(self.endpoint_url, headers=headers, json=payload)
        except requests.exceptions.RequestException as e:
            raise ValueError(f"Error raised by inference endpoint: {e}")

        try:
            if response.status_code == 429:
                if not is_retry:
                    import time

                    time.sleep(self.retry_sleep)

                    return self._call(prompt, stop, run_manager, is_retry=True)

                raise ValueError(
                    f"Error raised by inference API: rate limit exceeded.\nResponse: "
                    f"{response.text}"
                )

            parsed_response = response.json()

            # The inference API has changed a couple of times, so we add some handling
            # to be robust to multiple response formats.
            if isinstance(parsed_response, dict):
                output_keys = ["data", "output", "outputs"]
                for key in output_keys:
                    if key in parsed_response:
                        output_item = parsed_response[key]
                        break
                else:
                    raise ValueError(
                        f"No valid key ({', '.join(output_keys)}) in response:"
                        f" {parsed_response}"
                    )
                if isinstance(output_item, list):
                    text = output_item[0]
                else:
                    text = output_item
            else:
                raise ValueError(f"Unexpected response type: {parsed_response}")

            # Older versions of the API include the input in the output response
            if text.startswith(prompt):
                text = text[len(prompt) :]

        except requests.exceptions.JSONDecodeError as e:
            raise ValueError(
                f"Error raised by inference API: {e}.\nResponse: {response.text}"
            )

        # TODO: replace when MosaicML supports custom stop tokens natively
        if stop is not None:
            text = enforce_stop_tokens(text, stop)
        return text
