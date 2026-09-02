import os

from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()


def search_web(query: str) -> list[dict]:
    api_key = os.getenv("TAVILY_API_KEY")

    if not api_key:
        raise ValueError("TAVILY_API_KEY is not configured")

    client = TavilyClient(api_key=api_key)

    response = client.search(
        query=query,
        max_results=5
    )

    results = []

    for result in response.get("results", []):
        results.append(
            {
                "title": result.get("title", ""),
                "url": result.get("url", ""),
                "snippet": result.get("content", "")
            }
        )

    return results