from __future__ import annotations

import logging
from typing import Any, AsyncIterator, Dict, Iterator, List, Mapping, Optional, cast

from langchain.callbacks.manager import (
    AsyncCallbackManagerForLLMRun,
    CallbackManagerForLLMRun,
)
from langchain.chat_models.base import BaseChatModel
from langchain.pydantic_v1 import Field, root_validator
from langchain.schema import ChatGeneration, ChatResult
from langchain.schema.messages import (
    AIMessage,
    AIMessageChunk,
    BaseMessage,
    ChatMessage,
    FunctionMessage,
    HumanMessage,
    SystemMessage,
)
from langchain.schema.output import ChatGenerationChunk
from langchain.utils import get_from_dict_or_env

logger = logging.getLogger(__name__)


def convert_message_to_dict(message: BaseMessage) -> dict:
    """Convert a message to a dictionary that can be passed to the API."""
    message_dict: Dict[str, Any]
    if isinstance(message, ChatMessage):
        message_dict = {"role": message.role, "content": message.content}
    elif isinstance(message, HumanMessage):
        message_dict = {"role": "user", "content": message.content}
    elif isinstance(message, AIMessage):
        message_dict = {"role": "assistant", "content": message.content}
        if "function_call" in message.additional_kwargs:
            message_dict["function_call"] = message.additional_kwargs["function_call"]
            # If function call only, content is None not empty string
            if message_dict["content"] == "":
                message_dict["content"] = None
    elif isinstance(message, FunctionMessage):
        message_dict = {
            "role": "function",
            "content": message.content,
            "name": message.name,
        }
    else:
        raise TypeError(f"Got unknown type {message}")

    return message_dict


def _convert_dict_to_message(_dict: Mapping[str, Any]) -> AIMessage:
    content = _dict.get("result", "") or ""
    if _dict.get("function_call"):
        additional_kwargs = {"function_call": dict(_dict["function_call"])}
        if "thoughts" in additional_kwargs["function_call"]:
            # align to api sample, which affects the llm function_call output
            additional_kwargs["function_call"].pop("thoughts")
    else:
        additional_kwargs = {}
    return AIMessage(
        content=content,
        additional_kwargs={**_dict.get("body", {}), **additional_kwargs},
    )


class QianfanChatEndpoint(BaseChatModel):
    """Baidu Qianfan chat models.

    To use, you should have the ``qianfan`` python package installed, and
    the environment variable ``qianfan_ak`` and ``qianfan_sk`` set with your
    API key and Secret Key.

    ak, sk are required parameters
    which you could get from  https://cloud.baidu.com/product/wenxinworkshop

    Example:
        .. code-block:: python

            from langchain.chat_models import QianfanChatEndpoint
            qianfan_chat = QianfanChatEndpoint(model="ERNIE-Bot",
                endpoint="your_endpoint", qianfan_ak="your_ak", qianfan_sk="your_sk")
    """

    model_kwargs: Dict[str, Any] = Field(default_factory=dict)

    client: Any

    qianfan_ak: Optional[str] = None
    qianfan_sk: Optional[str] = None

    streaming: Optional[bool] = False
    """Whether to stream the results or not."""

    request_timeout: Optional[int] = 60
    """request timeout for chat http requests"""

    top_p: Optional[float] = 0.8
    temperature: Optional[float] = 0.95
    penalty_score: Optional[float] = 1
    """Model params, only supported in ERNIE-Bot and ERNIE-Bot-turbo.
    In the case of other model, passing these params will not affect the result.
    """

    model: str = "ERNIE-Bot-turbo"
    """Model name.
    you could get from https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Nlks5zkzu
    
    preset models are mapping to an endpoint.
    `model` will be ignored if `endpoint` is set.
    Default is ERNIE-Bot-turbo.
    """

    endpoint: Optional[str] = None
    """Endpoint of the Qianfan LLM, required if custom model used."""

    @root_validator()
    def validate_enviroment(cls, values: Dict) -> Dict:
        values["qianfan_ak"] = get_from_dict_or_env(
            values,
            "qianfan_ak",
            "QIANFAN_AK",
        )
        values["qianfan_sk"] = get_from_dict_or_env(
            values,
            "qianfan_sk",
            "QIANFAN_SK",
        )
        params = {
            "ak": values["qianfan_ak"],
            "sk": values["qianfan_sk"],
            "model": values["model"],
            "stream": values["streaming"],
        }
        if values["endpoint"] is not None and values["endpoint"] != "":
            params["endpoint"] = values["endpoint"]
        try:
            import qianfan

            values["client"] = qianfan.ChatCompletion(**params)
        except ImportError:
            raise ValueError(
                "qianfan package not found, please install it with "
                "`pip install qianfan`"
            )
        return values

    @property
    def _identifying_params(self) -> Dict[str, Any]:
        return {
            **{"endpoint": self.endpoint, "model": self.model},
            **super()._identifying_params,
        }

    @property
    def _llm_type(self) -> str:
        """Return type of chat_model."""
        return "baidu-qianfan-chat"

    @property
    def _default_params(self) -> Dict[str, Any]:
        """Get the default parameters for calling Qianfan API."""
        normal_params = {
            "model": self.model,
            "endpoint": self.endpoint,
            "stream": self.streaming,
            "request_timeout": self.request_timeout,
            "top_p": self.top_p,
            "temperature": self.temperature,
            "penalty_score": self.penalty_score,
        }

        return {**normal_params, **self.model_kwargs}

    def _convert_prompt_msg_params(
        self,
        messages: List[BaseMessage],
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """
        Converts a list of messages into a dictionary containing the message content
        and default parameters.

        Args:
            messages (List[BaseMessage]): The list of messages.
            **kwargs (Any): Optional arguments to add additional parameters to the
            resulting dictionary.

        Returns:
            Dict[str, Any]: A dictionary containing the message content and default
            parameters.

        """
        messages_dict: Dict[str, Any] = {
            "messages": [
                convert_message_to_dict(m)
                for m in messages
                if not isinstance(m, SystemMessage)
            ]
        }
        for i in [i for i, m in enumerate(messages) if isinstance(m, SystemMessage)]:
            if "system" not in messages_dict:
                messages_dict["system"] = ""
            messages_dict["system"] += cast(str, messages[i].content) + "\n"

        return {
            **messages_dict,
            **self._default_params,
            **kwargs,
        }

    def _generate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> ChatResult:
        """Call out to an qianfan models endpoint for each generation with a prompt.
        Args:
            messages: The messages to pass into the model.
            stop: Optional list of stop words to use when generating.
        Returns:
            The string generated by the model.

        Example:
            .. code-block:: python
                response = qianfan_model("Tell me a joke.")
        """
        if self.streaming:
            completion = ""
            for chunk in self._stream(messages, stop, run_manager, **kwargs):
                completion += chunk.text
            lc_msg = AIMessage(content=completion, additional_kwargs={})
            gen = ChatGeneration(
                message=lc_msg,
                generation_info=dict(finish_reason="stop"),
            )
            return ChatResult(
                generations=[gen],
                llm_output={"token_usage": {}, "model_name": self.model},
            )
        params = self._convert_prompt_msg_params(messages, **kwargs)
        response_payload = self.client.do(**params)
        lc_msg = _convert_dict_to_message(response_payload)
        gen = ChatGeneration(
            message=lc_msg,
            generation_info={
                "finish_reason": "stop",
                **response_payload.get("body", {}),
            },
        )
        token_usage = response_payload.get("usage", {})
        llm_output = {"token_usage": token_usage, "model_name": self.model}
        return ChatResult(generations=[gen], llm_output=llm_output)

    async def _agenerate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[AsyncCallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> ChatResult:
        if self.streaming:
            completion = ""
            token_usage = {}
            async for chunk in self._astream(messages, stop, run_manager, **kwargs):
                completion += chunk.text

            lc_msg = AIMessage(content=completion, additional_kwargs={})
            gen = ChatGeneration(
                message=lc_msg,
                generation_info=dict(finish_reason="stop"),
            )
            return ChatResult(
                generations=[gen],
                llm_output={"token_usage": {}, "model_name": self.model},
            )
        params = self._convert_prompt_msg_params(messages, **kwargs)
        response_payload = await self.client.ado(**params)
        lc_msg = _convert_dict_to_message(response_payload)
        generations = []
        gen = ChatGeneration(
            message=lc_msg,
            generation_info={
                "finish_reason": "stop",
                **response_payload.get("body", {}),
            },
        )
        generations.append(gen)
        token_usage = response_payload.get("usage", {})
        llm_output = {"token_usage": token_usage, "model_name": self.model}
        return ChatResult(generations=generations, llm_output=llm_output)

    def _stream(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> Iterator[ChatGenerationChunk]:
        params = self._convert_prompt_msg_params(messages, **kwargs)
        for res in self.client.do(**params):
            if res:
                msg = _convert_dict_to_message(res)
                chunk = ChatGenerationChunk(
                    text=res["result"],
                    message=AIMessageChunk(
                        content=msg.content,
                        role="assistant",
                        additional_kwargs=msg.additional_kwargs,
                    ),
                )
                yield chunk
                if run_manager:
                    run_manager.on_llm_new_token(chunk.text, chunk=chunk)

    async def _astream(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[AsyncCallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> AsyncIterator[ChatGenerationChunk]:
        params = self._convert_prompt_msg_params(messages, **kwargs)
        async for res in await self.client.ado(**params):
            if res:
                msg = _convert_dict_to_message(res)
                chunk = ChatGenerationChunk(
                    text=res["result"],
                    message=AIMessageChunk(
                        content=msg.content,
                        role="assistant",
                        additional_kwargs=msg.additional_kwargs,
                    ),
                )
                yield chunk
                if run_manager:
                    await run_manager.on_llm_new_token(chunk.text, chunk=chunk)
