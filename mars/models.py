from __future__ import annotations

from pydantic import BaseModel
from typing import Optional, Dict, Any

class TaskEnvelope(BaseModel):
    task_id: str
    user_id: str
    playbook_version: str
    tool_context: Dict[str, Any]
    prompt_template_id: str
    parameters: Dict[str, Any]
    memory_pointer: Optional[str] = None

class ErrorEnvelope(BaseModel):
    task_id: str
    error_code: str
    retryable: bool
    details: Optional[str] = None
