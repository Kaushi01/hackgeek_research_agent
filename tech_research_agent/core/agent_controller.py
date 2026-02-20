# core/agent_controller.py

import time
from core.router import detect_mode
from core.executor import research
from memory.retrieve import retrieve
from memory.store import store_research


def run_agent(query, mode="quick", session_id="", user_id="default_user", preferences={}):
    start_time = time.time()

    # 1. Auto-detect mode if not forced
    if mode not in ("quick", "deep"):
        mode = detect_mode(query)

    # 2. Retrieve memory context from Qdrant
    try:
        memory_context = retrieve(user_id, query)
        memory_used = [] if memory_context == "No previous memory found for this user." else [memory_context]
    except Exception:
        memory_context = ""
        memory_used = []

    # 3. Build enriched query with memory context
    if memory_context and memory_context != "No previous memory found for this user.":
        enriched_query = f"{memory_context}\n\nNow answer this question:\n{query}"
    else:
        enriched_query = query

    # 4. Generate answer via Ollama (gemma3:4b)
    answer = research(user_id=user_id, query=enriched_query, mode=mode)

    # 5. Save this research to Qdrant memory
    memory_saved = []
    try:
        store_research(user_id=user_id, query=query, summary=answer[:500], mode=mode)
        memory_saved = [f"Stored: {query[:60]}..."]
    except Exception:
        pass

    latency = round(time.time() - start_time, 2)

    return {
        "answer": answer,
        "mode": mode,
        "clarifying_question": None,
        "citations": [],
        "memory": {
            "used": memory_used,
            "saved": memory_saved
        },
        "metrics": {
            "latency_s": latency,
            "tokens_in": None,
            "tokens_out": None,
            "estimated_cost_usd": 0.0
        },
        "debug": {
            "model": "gemma3:4b",
            "embed_model": "nomic-embed-text",
            "memory_context_found": bool(memory_used),
            "mode_used": mode
        }
    }


if __name__ == "__main__":
    result = run_agent("What is a data warehouse?", mode="quick", user_id="test_user")
    print(result["answer"])