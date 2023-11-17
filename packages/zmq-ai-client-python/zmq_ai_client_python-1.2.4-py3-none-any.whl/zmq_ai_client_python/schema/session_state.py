from dataclasses import dataclass
from typing import Optional, Dict


@dataclass
class SessionStateResponse:
    """
    Dataclass representing a session cache response.
    """
    session_id: str
    user_id: str
    exists: bool
    key: Optional[int]
    created_date: Optional[int]
    updated_date: Optional[int]
    prompt: Optional[str]
    session_tokens_size: Optional[int]
    session_tokens_keep_size: Optional[int]
    context_truncated: Optional[bool]
    key_values: Optional[Dict[str, str]] = None

