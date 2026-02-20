from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PayloadSchemaType
from dotenv import load_dotenv
import os

load_dotenv()

client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
)

# ✅ Use correct dimension (nomic-embed-text = 768)
VECTOR_SIZE = 768

COLLECTIONS = [
    "user_preferences",
    "research_history",
    "key_facts"
]


def create_collections():
    existing = [c.name for c in client.get_collections().collections]

    for name in COLLECTIONS:
        if name not in existing:
            client.create_collection(
                collection_name=name,
                vectors_config=VectorParams(
                    size=VECTOR_SIZE,
                    distance=Distance.COSINE
                )
            )
            print(f"[CREATED] {name}")
        else:
            print(f"[EXISTS] {name}")

        # ✅ Create payload index for user_id
        client.create_payload_index(
            collection_name=name,
            field_name="user_id",
            field_schema=PayloadSchemaType.KEYWORD,
        )

    print("Qdrant is connected and ready!")


if __name__ == "__main__":
    create_collections()