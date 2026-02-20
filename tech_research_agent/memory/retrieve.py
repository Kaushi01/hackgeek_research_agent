import requests
from qdrant_client.models import Filter, FieldCondition, MatchValue

from memory.qdrant_db import client
# -------------------------
# Ollama Embedding Config
# -------------------------
OLLAMA_EMBED_URL = "http://localhost:11434/api/embeddings"
EMBED_MODEL = "nomic-embed-text"


def embed(text: str):
    response = requests.post(
        OLLAMA_EMBED_URL,
        json={
            "model": EMBED_MODEL,
            "prompt": text
        }
    )

    if response.status_code != 200:
        raise Exception(f"Ollama embedding error: {response.text}")

    return response.json()["embedding"]


# -------------------------
# Retrieve Functions
# -------------------------

def retrieve_preferences(user_id: str, query: str, limit: int = 3):
    results = client.query_points(
        collection_name="user_preferences",
        query=embed(query),
        limit=limit,
        query_filter=Filter(
            must=[FieldCondition(key="user_id", match=MatchValue(value=user_id))]
        )
    )
    return [r.payload["preference"] for r in results.points]


def retrieve_history(user_id: str, query: str, limit: int = 3):
    results = client.query_points(
        collection_name="research_history",
        query=embed(query),
        limit=limit,
        query_filter=Filter(
            must=[FieldCondition(key="user_id", match=MatchValue(value=user_id))]
        )
    )
    return [
        {"query": r.payload["query"], "summary": r.payload["summary"]}
        for r in results.points
    ]


def retrieve_facts(user_id: str, query: str, limit: int = 3):
    results = client.query_points(
        collection_name="key_facts",
        query=embed(query),
        limit=limit,
        query_filter=Filter(
            must=[FieldCondition(key="user_id", match=MatchValue(value=user_id))]
        )
    )
    return [r.payload["fact"] for r in results.points]


def retrieve(user_id: str, query: str) -> str:
    preferences = retrieve_preferences(user_id, query)
    history = retrieve_history(user_id, query)
    facts = retrieve_facts(user_id, query)

    context = ""

    if preferences:
        context += "USER PREFERENCES:\n"
        for p in preferences:
            context += f"  - {p}\n"

    if history:
        context += "\nPAST RESEARCH:\n"
        for h in history:
            context += f"  - Asked: {h['query']}\n"
            context += f"    Summary: {h['summary']}\n"

    if facts:
        context += "\nKEY FACTS FROM PAST SESSIONS:\n"
        for f in facts:
            context += f"  - {f}\n"

    if not context:
        context = "No previous memory found for this user."

    return context