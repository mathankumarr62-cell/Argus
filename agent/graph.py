from langgraph.graph import StateGraph, START, END
from agent.state import AgentState
from agent.nodes import create_research_plan
from agent.research import prepare_research_tasks


def build_research_graph():
    graph = StateGraph(AgentState)

    graph.add_node("create_research_plan", create_research_plan)
    graph.add_node("prepare_research_tasks", prepare_research_tasks)

    graph.add_edge(START, "create_research_plan")
    graph.add_edge("create_research_plan", "prepare_research_tasks")
    graph.add_edge("prepare_research_tasks", END)

    return graph.compile()