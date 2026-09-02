from langgraph.graph import StateGraph, START, END
from agent.state import AgentState
from agent.nodes import create_research_plan


def build_research_graph():
    graph = StateGraph(AgentState)

    graph.add_node("create_research_plan", create_research_plan)

    graph.add_edge(START, "create_research_plan")
    graph.add_edge("create_research_plan", END)

    return graph.compile()