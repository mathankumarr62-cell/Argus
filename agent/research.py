from agent.state import AgentState
from agent.search import search_web


def rank_sources(results: list[dict]) -> list[dict]:
    for result in results:
        score = 0

        if result.get("title"):
            score += 1

        if result.get("url"):
            score += 1

        if result.get("snippet"):
            score += 1

        url = result.get("url", "")

        trusted_domains = [
            "nvidia.com",
            "aws.amazon.com",
            "databricks.com",
            "microsoft.com",
            "google.com",
            "ibm.com",
            "openai.com"
        ]

        if any(domain in url for domain in trusted_domains):
            score += 2

        result["score"] = score

    return sorted(
        results,
        key=lambda result: result["score"],
        reverse=True
    )


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
            normalized_url = url.replace("://www.", "://")

            if normalized_url and normalized_url not in seen_urls:
                seen_urls.add(normalized_url)
                results.append(result)

    state["results"] = rank_sources(results)

    return state