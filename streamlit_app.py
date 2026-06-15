import streamlit as st
from utils.memory import load_memory
from graph import graph

st.set_page_config(
    page_title="Multi-Agent Research Assistant",
    page_icon="🤖",
    layout="wide"
)

st.markdown(
    """
    <style>
    .stApp {
        padding-top: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("⚙️ Controls")
st.title("🤖 Multi-Agent Research Assistant")
st.markdown("---")

st.markdown(
    """
    AI-powered research assistant using:
    - LangGraph
    - Multi-agent orchestration
    - Tool grounding
    - Persistent memory
    """
)

query = st.sidebar.text_input(
    "Enter research topic:"
)

run_button = st.sidebar.button("🚀 Run Research")

st.sidebar.subheader("🧠 Memory")

memory = load_memory()

if memory:
    for item in memory[-3:]:
        st.sidebar.write(f"• {item['query']}")
else:
    st.sidebar.write("No memory yet.")

if st.sidebar.button("🗑️ Clear Memory"):

    with open("memory/research_history.json", "w") as f:
        f.write("[]")

    st.sidebar.success("Memory cleared!")

if run_button and query:

    with st.spinner("Running LangGraph workflow..."):

        result = graph.invoke({
            "query": query,
            "retry_count": 0
        })

    st.success("Workflow completed!")

    st.subheader("📄 Final Report")

    if "report" in result:
        st.write(result["report"])
        st.download_button(
            label="📥 Download Report",
            data=result["report"],
            file_name="research_report.txt",
            mime="text/plain"
        )
    else:
        st.error("Workflow failed.")

    with st.expander("📝 Original Draft"):
        if "draft_report" in result:
            st.write(result["draft_report"])

    with st.expander("🪞 Reflection Feedback"):
        if "critique" in result:
            st.write(result["critique"])
    
    with st.expander("🔍 Research Output"):
        if "research" in result:
            st.json(result["research"])

    with st.expander("📊 Analysis Output"):
        if "analysis" in result:
            st.json(result["analysis"])

elif run_button:
    st.warning("Please enter a research topic.")