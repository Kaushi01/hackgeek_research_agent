# core/router.py

def detect_mode(query: str) -> str:
    query_lower = query.lower()

    if "deep" in query_lower:
        return "deep"

    if len(query.split()) > 25:
        return "deep"

    return "quick"