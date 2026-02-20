BLOCKED_DOMAINS = ["pinterest.com", "quora.com", "reddit.com/r/memes", "yahoo.answers.com"]

PREFERRED_DOMAINS = ["arxiv.org", "github.com", "stackoverflow.com", "docs.python.org",
                     "medium.com", "towardsdatascience.com", "huggingface.co", "openai.com"]

def rank_and_filter_sources(sources: list[dict], min_score: float = 0.3) -> list[dict]:
    """
    Input: list of { title, url, content, score }
    Output: filtered + ranked list
    """
    filtered = []

    for source in sources:
        url = source.get("url", "")

        # Block low quality domains
        if any(blocked in url for blocked in BLOCKED_DOMAINS):
            continue

        # Boost preferred domains
        boost = 0.2 if any(preferred in url for preferred in PREFERRED_DOMAINS) else 0.0

        adjusted_score = source.get("score", 0.0) + boost
        source["adjusted_score"] = adjusted_score

        if adjusted_score >= min_score:
            filtered.append(source)

    # Sort by adjusted score descending
    ranked = sorted(filtered, key=lambda x: x["adjusted_score"], reverse=True)
    return ranked