from agent.state import AgentState


def create_research_plan(state: AgentState) -> AgentState:
    query = state["query"]

    state["research_plan"] = [
        f"Understand the research question: {query}",
        "Identify the important information needed",
        "Collect and analyze relevant sources"
    ]

    return state