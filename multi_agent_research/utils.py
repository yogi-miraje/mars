from concurrent.futures import ThreadPoolExecutor
from typing import Callable, Iterable, List
import os


def run_parallel(func: Callable[[any], any], items: Iterable[any]) -> List[any]:
    with ThreadPoolExecutor() as executor:
        return list(executor.map(func, items))


def llm_route(prompt: str, provider: str | None = None) -> str:
    provider = provider or os.getenv("LLM_PROVIDER", "stub")
    if provider == "openai" and os.getenv("OPENAI_API_KEY"):
        try:
            import openai
            resp = openai.ChatCompletion.create(
                model=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
                messages=[{"role": "user", "content": prompt}],
            )
            return resp.choices[0].message.content.strip()
        except Exception as e:
            return f"OpenAI error: {e}"
    return f"[Stubbed LLM response] {prompt[:200]}"
