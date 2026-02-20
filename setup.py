import os

files = [
    "tech-research-agent/app.py",
    "tech-research-agent/config.py",
    "tech-research-agent/requirements.txt",
    "tech-research-agent/README.md",
    "tech-research-agent/graph/graph.py",
    "tech-research-agent/graph/mode_controller.py",
    "tech-research-agent/graph/fallback.py",
    "tech-research-agent/retrieval/web_search.py",
    "tech-research-agent/retrieval/fetcher.py",
    "tech-research-agent/retrieval/ranker.py",
    "tech-research-agent/retrieval/citation.py",
    "tech-research-agent/memory/qdrant_client.py",
    "tech-research-agent/memory/store.py",
    "tech-research-agent/memory/retrieve.py",
    "tech-research-agent/utils/cost_tracker.py",
    "tech-research-agent/utils/latency.py",
]

for path in files:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w').close()

print("âœ… Project structure created!")
