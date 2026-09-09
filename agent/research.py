from agent.state import AgentState
from agent.search import search_web


def prepare_research_tasks(state: AgentState) -> AgentState:
    query = state["query"]

    search_queries = [
        f"{query} definition",
        f"{query} how it works",
        f"{query} applications and examples"
    ]

    results = []
    seen_urls = set()

    for search_query in search_queries:
        search_results = search_web(search_query)

        for result in search_results:
            url = result.get("url", "")

            if url and url not in seen_urls:
                seen_urls.add(url)
                results.append(result)

    state["results"] = results

    return state