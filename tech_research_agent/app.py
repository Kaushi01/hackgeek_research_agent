# app.py
import streamlit as st
from core.agent_controller import run_agent

# Page config
st.set_page_config(page_title="HackGeek Research Agent", layout="wide")
st.title("🔍 HackGeek Research Agent")

# Sidebar options
st.sidebar.header("Settings")
mode = st.sidebar.selectbox("Select mode:", ["quick", "detailed"])
session_id = st.sidebar.text_input("Session ID:", "session_1")
user_id = st.sidebar.text_input("User ID:", "user_1")

# Main input
query = st.text_input("Enter your query here:")

if st.button("Run Agent") and query:
    with st.spinner("Researching…"):
        # Call agent
        result = run_agent(
            query=query,
            mode=mode,
            session_id=session_id,
            user_id=user_id,
            preferences={}
        )

    # Display answer
    st.subheader("📄 Answer")
    st.markdown(result["answer"])

    # Display citations if available
    if result.get("citations"):
        st.subheader("📚 Citations")
        for c in result["citations"]:
            st.markdown(f"- [{c['title']}]({c['url']}) — {c.get('snippet','')}")

    # Display memory used/saved
    memory = result.get("memory", {})
    if memory.get("used") or memory.get("saved"):
        st.subheader("🧠 Memory")
        if memory.get("used"):
            st.markdown("**Used:** " + ", ".join(memory["used"]))
        if memory.get("saved"):
            st.markdown("**Saved:** " + ", ".join(memory["saved"]))

    # Display metrics
    metrics = result.get("metrics", {})
    if metrics:
        st.subheader("📊 Metrics")
        st.markdown(
            "\n".join([f"- **{k}**: {v}" for k, v in metrics.items() if v is not None])
        )

    # Display debug info
    debug = result.get("debug", {})
    if debug:
        with st.expander("⚙️ Debug Info"):
            st.json(debug)