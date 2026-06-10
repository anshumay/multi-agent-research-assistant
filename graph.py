from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.researcher import research_agent
from agents.analyst import analyst_agent
from agents.writer import writer_agent
from agents.reviewer import reviewer_agent

from utils.parser import parse_json
from utils.memory import save_memory


# -----------------------------
# STATE
# -----------------------------

class AgentState(TypedDict):
    query: str
    research: dict
    research_status: str
    analysis: dict
    draft_report: str
    report: str
    critique: str
    retry_count: int


# -----------------------------
# NODES
# -----------------------------

def research_node(state: AgentState):

    print("\n🔍 RESEARCH NODE")

    research_raw = research_agent(state["query"])
    research = parse_json(research_raw)
    
    save_memory({
    "query": state["query"],
    "research": research
    })

    return {
    "research": research,
    "retry_count": state.get("retry_count", 0) + 1
    }


def analysis_node(state: AgentState):

    print("\n📊 ANALYSIS NODE")

    analysis_raw = analyst_agent(state["research"])
    analysis = parse_json(analysis_raw)

    return {
        "analysis": analysis
    }


def writer_node(state: AgentState):

    print("\n✍️ WRITER NODE")

    report = writer_agent(state["analysis"])

    return {
    "draft_report": report,
    "report": report
    }

def validate_research_node(state: AgentState):

    print("\n✅ VALIDATION NODE")

    research = state["research"]

    if (
        isinstance(research, dict)
        and "facts" in research
        and len(research["facts"]) > 0
    ):
        return {
            "research_status": "valid"
        }

    return {
        "research_status": "invalid"
    }

def research_router(state: AgentState):

    if state["research_status"] == "valid":
        return "analysis"

    if state["retry_count"] >= 2:
        return END

    return "research"

def reflection_node(state):

    print("\n🪞 REFLECTION NODE")

    critique = reviewer_agent(
        state["report"]
    )

    return {
        "critique": critique
    }

def revision_node(state):

    print("\n✍️ REVISION NODE")

    prompt = f"""
    Improve the report using reviewer feedback.

    Reviewer Feedback:
    {state['critique']}

    Original Report:
    {state['report']}

    Return only the improved report.
    """

    from utils.llm import call_llm

    revised_report = call_llm(prompt)

    return {
        "report": revised_report
    }

# -----------------------------
# GRAPH
# -----------------------------

builder = StateGraph(AgentState)

builder.add_node("research", research_node)
builder.add_node("validate_research", validate_research_node)
builder.add_node("analysis", analysis_node)
builder.add_node("writer", writer_node)
builder.add_node("reflection", reflection_node)
builder.add_node("revision", revision_node)

builder.set_entry_point("research")

# builder.add_edge("research", "analysis")
builder.add_edge("research", "validate_research")
builder.add_conditional_edges(
    "validate_research",
    research_router
)
builder.add_edge("analysis", "writer")
builder.add_edge( "writer", "reflection")
builder.add_edge("reflection", "revision")
builder.add_edge("revision", END)

graph = builder.compile()