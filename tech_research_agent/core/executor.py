from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL_NAME = "llama-3.1-8b-instant"

def call_local_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def research(user_id: str, query: str, mode: str = "quick") -> str:
    if mode == "quick":
        prompt = f"You are a helpful research assistant. Give a thorough answer with 3-4 paragraphs including examples.\n\nQuestion: {query}"
    else:
        prompt = f"You are an expert research assistant. Give a very detailed answer with introduction, key concepts, examples, use cases and summary.\n\nQuestion: {query}"
    return call_local_llm(prompt)

def quick_research(user_id, query): return research(user_id, query, mode="quick")
def deep_research(user_id, query): return research(user_id, query, mode="deep")

