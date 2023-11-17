from dataclasses import dataclass
from typing import List, Optional, Dict, Literal


@dataclass
class FunctionCall:
    """
    Dataclass representing a function call in the request.
    """
    arguments: str
    name: str


@dataclass
class Message:
    """
    Dataclass representing a message in the request.
    """
    content: str  # Content of the message
    role: str  # Role of the message sender (e.g., "user" or "system")
    function_call: Optional[FunctionCall] = None  # Optional function call associated with the message
    name: Optional[str] = None  # Optional name of the sender


@dataclass
class Function:
    """
    Dataclass representing a function that can be called in the request.
    """
    name: str  # Name of the function
    parameters: str  # Optional parameters for the function
    description: Optional[str] = None  # Optional description of the function


@dataclass
class ChatCompletionChoice:
    """
    Dataclass representing a choice in a chat completion.
    """
    finish_reason: Literal["stop", "length", "content_filter", "function_call"]  # Reason for finishing the choice
    index: int  # Index of the choice
    message: Message  # Message associated with the choice


@dataclass
class ChatCompletionUsage:
    """
    Dataclass representing the usage statistics of a chat completion.
    """
    completion_tokens: int  # Number of tokens in the completion
    prompt_tokens: int  # Number of tokens in the prompt
    total_tokens: int  # Total number of tokens (prompt + completion)


@dataclass
class ChatCompletion:
    """
    Dataclass representing a chat completion.
    """
    id: str  # Unique identifier for the completion
    choices: List[ChatCompletionChoice]  # List of choices in the completion
    created: int  # Timestamp of when the completion was created
    model: str  # Name of the model to be used
    object: Literal["chat_completion"]  # Type of the object (always "chat_completion" for this class)
    usage: ChatCompletionUsage  # Usage statistics for the completion
    key_values: Optional[Dict[str, str]] = None  # Optional key_values for advanced options
