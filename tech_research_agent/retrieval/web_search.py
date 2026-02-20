import os
from tavily import TavilyClient

client = TavilyClient(api_key="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")

def multi_query_search(queries: list, max_results_per_query: int = 5) -> list:
    all_results = []
    seen_urls = set()

    for query in queries:
        try:
            response = client.search(
                query=query,
                max_results=max_results_per_query,
                include_answer=False,
                search_depth="advanced"
            )
            for r in response.get("results", []):
                if r["url"] not in seen_urls:
                    seen_urls.add(r["url"])
                    all_results.append({
                        "title": r.get("title", ""),
                        "url": r.get("url", ""),
                        "content": r.get("content", ""),
                        "score": r.get("score", 0.0)
                    })
        except Exception as e:
            print(f"[web_search] Error for query '{query}': {e}")

    return all_results