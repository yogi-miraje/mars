from .utils import llm_route


def evaluate_answer(answer: str) -> str:
    prompt = (
        "Score the following answer for completeness and quality on a scale of 1-5:"\
        f"\n{answer}"
    )
    return llm_route(prompt)
