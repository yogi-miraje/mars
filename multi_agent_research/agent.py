from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict

from .tool import WebSearchTool
from .memory import Memory
from .utils import run_parallel, llm_route


@dataclass
class TaskResult:
    task: str
    summary: str


class Subagent:
    """Worker that executes a single research task."""

    def __init__(self, task: str, memory: Memory | None = None):
        self.task = task
        self.memory = memory or Memory()
        self.tools = [WebSearchTool()]

    def run(self) -> TaskResult:
        search_results = self.tools[0].run(self.task)
        summary_prompt = (
            f"Your task is: {self.task}."\
            " Summarize the following search results in a concise paragraph:\n"\
            f"{search_results}"
        )
        summary = llm_route(summary_prompt)
        return TaskResult(task=self.task, summary=summary)


class LeadResearcherAgent:
    """Orchestrates research by spawning subagents and synthesizing results."""

    def __init__(self, memory: Memory | None = None):
        self.memory = memory or Memory()

    def plan(self, query: str) -> List[str]:
        prompt = (
            "Given the question, break it into independent research tasks."\
            f"\nQuestion: {query}"
        )
        tasks_text = llm_route(prompt)
        tasks = [t.strip("- ") for t in tasks_text.splitlines() if t.strip()]
        return tasks if tasks else [query]

    def run(self, query: str) -> str:
        tasks = self.plan(query)
        self.memory.save("plan", tasks)

        subagents = [Subagent(task, memory=self.memory) for task in tasks]
        results: List[TaskResult] = run_parallel(lambda sa: sa.run(), subagents)
        self.memory.save("results", [r.__dict__ for r in results])

        synthesis = "".join(
            f"Task: {r.task}\nSummary: {r.summary}\n" for r in results
        )
        final_prompt = (
            f"Synthesize the following research results into a single answer to "
            f"the question: {query}\n\n{synthesis}"
        )
        final_answer = llm_route(final_prompt)
        self.memory.save("final_answer", final_answer)
        return final_answer
