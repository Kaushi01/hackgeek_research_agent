import requests
from qdrant_client.models import PointStruct
from datetime import datetime
import uuid

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
# Store Functions
# -------------------------

def store_preference(user_id: str, preference: str):
    client.upsert(
        collection_name="user_preferences",
        points=[PointStruct(
            id=str(uuid.uuid4()),
            vector=embed(preference),
            payload={
                "user_id": user_id,
                "preference": preference,
                "timestamp": datetime.now().isoformat()
            }
        )]
    )
    print(f"[STORED] Preference for {user_id}: {preference}")


def store_research(user_id: str, query: str, summary: str, mode: str):
    client.upsert(
        collection_name="research_history",
        points=[PointStruct(
            id=str(uuid.uuid4()),
            vector=embed(query),
            payload={
                "user_id": user_id,
                "query": query,
                "summary": summary,
                "mode": mode,
                "timestamp": datetime.now().isoformat()
            }
        )]
    )
    print(f"[STORED] Research for {user_id}: {query}")


def store_fact(user_id: str, fact: str, topic: str):
    client.upsert(
        collection_name="key_facts",
        points=[PointStruct(
            id=str(uuid.uuid4()),
            vector=embed(fact),
            payload={
                "user_id": user_id,
                "fact": fact,
                "topic": topic,
                "timestamp": datetime.now().isoformat()
            }
        )]
    )
    print(f"[STORED] Fact for {user_id}: {fact}")


def store(user_id: str, query: str, result: str):
    """
    Generic store function required by graph.py
    """
    store_research(
        user_id=user_id,
        query=query,
        summary=result,
        mode="default"
    )