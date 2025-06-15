from __future__ import annotations

import uvicorn
from fastapi import FastAPI, HTTPException

from .models import TaskEnvelope
from .worker import Worker, EchoRunner
from .orchestrator import Orchestrator

app = FastAPI(title="mars-gateway")

runner = EchoRunner()
worker = Worker(runner)
orchestrator = Orchestrator(worker)


@app.post("/query")
async def query(user_id: str, prompt_id: str, text: str):
    task = orchestrator.create_task(
        user_id=user_id,
        tool_context={},
        prompt_template_id=prompt_id,
        parameters={"text": text},
    )
    result = await orchestrator.run_task(task)
    if "error_code" in result:
        raise HTTPException(status_code=500, detail=result)
    return result


def main() -> None:
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
