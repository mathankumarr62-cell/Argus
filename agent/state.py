from typing import TypedDict


class AgentState(TypedDict):
    query: str
    research_plan: list[str]
    results: list[str]
    final_answer: str