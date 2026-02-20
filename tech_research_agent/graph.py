from tech_research_agent.utils.cost_tracker import estimate_cost
from tech_research_agent.core.router import detect_mode
from tech_research_agent.core.clarifier import needs_clarification, generate_clarification
from tech_research_agent.core.executor import research as quick_research
from tech_research_agent.core.executor import research as deep_research
from tech_research_agent.core.config import AgentConfig
from tech_research_agent.memory.retrieve import retrieve
from tech_research_agent.memory.store import store

def run_agent(user_id: str, query: str, tools=None):
    """
    Main agent execution function
    """

    # 1️⃣ Retrieve memory
    context = retrieve(user_id, query)

    # 2️⃣ Generate response (replace with your LLM call if different)
    response = f"Context:\n{context}\n\nAnswering query:\n{query}"

    # 3️⃣ Store memory
    store(user_id, query, response)

    return response