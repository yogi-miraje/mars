from __future__ import annotations

import uuid
from typing import Dict, Any

from .models import TaskEnvelope, ErrorEnvelope


class Orchestrator:
    """Simplified orchestrator prototype."""

    def __init__(self, worker: 'Worker') -> None:
        self.worker = worker

    def create_task(self, user_id: str, tool_context: Dict[str, Any], prompt_template_id: str, parameters: Dict[str, Any]) -> TaskEnvelope:
        task = TaskEnvelope(
            task_id=str(uuid.uuid4()),
            user_id=user_id,
            playbook_version="0.1.0",
            tool_context=tool_context,
            prompt_template_id=prompt_template_id,
            parameters=parameters,
        )
        return task

    async def run_task(self, task: TaskEnvelope) -> Dict[str, Any]:
        try:
            result = await self.worker.execute(task)
            return {"task_id": task.task_id, "result": result}
        except Exception as exc:
            error = ErrorEnvelope(task_id=task.task_id, error_code="WORKER_ERROR", retryable=False, details=str(exc))
            return error.dict()
