from agent.state import AgentState
from agent.search import search_web


def prepare_research_tasks(state: AgentState) -> AgentState:
    plan = state["research_plan"]

    results = []

    for task in plan:
        search_results = search_web(task)

        for result in search_results:
            results.append(
                f"{result['title']}: {result['snippet']}"
            )

    state["results"] = results

    return state