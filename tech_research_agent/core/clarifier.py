# core/clarifier.py

def needs_clarification(query: str) -> bool:
    vague_patterns = ["compare", "explain", "optimize", "improve"]

    if len(query.split()) < 4:
        return True

    for word in vague_patterns:
        if word in query.lower() and len(query.split()) < 6:
            return True

    return False


def generate_clarification(query: str) -> str:
    return (
        f"Your question '{query}' seems broad.\n"
        "Do you want:\n"
        "1) Theoretical explanation\n"
        "2) Production trade-offs\n"
        "3) Benchmarks and numbers\n"
        "Please clarify."
    )