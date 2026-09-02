from agent.state import AgentState


def prepare_research_tasks(state: AgentState) -> AgentState:
    plan = state["research_plan"]

    state["results"] = [
        f"Research task prepared: {task}"
        for task in plan
    ]

    return state