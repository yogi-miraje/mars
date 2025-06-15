from __future__ import annotations

from typing import Dict, Any

from .models import TaskEnvelope


class Worker:
    """Simple worker that executes tasks using a runner."""

    def __init__(self, runner: 'Runner') -> None:
        self.runner = runner

    async def execute(self, task: TaskEnvelope) -> Dict[str, Any]:
        return await self.runner.run(task)


class Runner:
    """Base runner interface."""

    async def run(self, task: TaskEnvelope) -> Dict[str, Any]:
        raise NotImplementedError


class EchoRunner(Runner):
    """Demo runner that echoes parameters."""

    async def run(self, task: TaskEnvelope) -> Dict[str, Any]:
        return {"echo": task.parameters}
