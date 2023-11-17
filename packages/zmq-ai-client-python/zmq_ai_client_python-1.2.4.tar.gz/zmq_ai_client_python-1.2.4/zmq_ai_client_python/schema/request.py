from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Dict

from zmq_ai_client_python.schema.completion import Message, Function


class RequestType(Enum):
    CHAT_COMPLETION_REQUEST = 0x01
    SESSION_STATE_REQUEST = 0x02
    TITLE_GENERATION_REQUEST = 0x03
    HEALTH_CHECK_REQUEST = 0x04


@dataclass
class ChatCompletionRequest:
    """
    Dataclass representing a chat completion request to the model.
    """
    messages: List[Message]  # List of messages in the request
    model: str  # Name of the model to be used
    frequency_penalty: Optional[float] = 0.0  # Penalty for frequent tokens in the output
    function_call: Optional[str] = None  # Optional function call
    functions: Optional[List[Function]] = None  # Optional list of functions in the request
    logit_bias: Optional[Dict[int, float]] = None  # Bias for certain tokens in the output
    max_tokens: Optional[int] = 2 ** 31 - 1  # Maximum number of tokens in the output
    n: Optional[int] = 1  # Number of completions to generate
    presence_penalty: Optional[float] = 0.0  # Penalty for new tokens in the output
    stop: Optional[List[str]] = None  # List of tokens to stop the generation
    stream: Optional[bool] = False  # Whether to stream the output
    temperature: Optional[float] = 1.0  # Sampling temperature for the model's output
    top_p: Optional[float] = 1.0  # Nucleus sampling parameter
    user: Optional[str] = None  # Optional user identifier for the request
    key_values: Optional[Dict[str, str]] = None  # Optional key_values for advanced options


@dataclass
class SessionStateRequest:
    """
    Dataclass representing a session cache request to the model.
    """
    session_id: str
    user_id: str
    has_detail: bool = False

