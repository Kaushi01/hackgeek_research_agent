def format_citations(sources: list[dict]) -> list[dict]:
    """
    Input: list of ranked sources
    Output: list of citations with { index, title, url, snippet }
    """
    citations = []

    for i, source in enumerate(sources, start=1):
        title = source.get("title", "Untitled")
        url = source.get("url", "")
        content = source.get("content", "") or source.get("full_text", "")
        snippet = content[:200].replace("\n", " ").strip() + "..." if content else "No preview available."

        citations.append({
            "index": i,
            "title": title,
            "url": url,
            "snippet": snippet
        })

    return citations


def format_citations_as_text(citations: list[dict]) -> str:
    """
    Returns citations as a readable string for LLM context or UI display.
    """
    lines = []
    for c in citations:
        lines.append(f"[{c['index']}] {c['title']}\n    URL: {c['url']}\n    Preview: {c['snippet']}\n")
    return "\n".join(lines)

# ## 📦 Your `requirements.txt` additions

# Tell your team to add these to the shared requirements file:
# ```
# tavily-python
# requests
# beautifulsoup4