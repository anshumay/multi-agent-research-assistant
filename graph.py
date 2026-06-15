from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.researcher import research_agent
from agents.analyst import analyst_agent
from agents.writer import writer_agent
from agents.reviewer import reviewer_agent
from agents.supervisor import supervisor_agent
from agents.memory_summarizer import memory_summarizer

from utils.parser import parse_json
from utils.memory import load_memory, save_memory, find_in_memory


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
    workflow_type: str


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

def supervisor_node(state):

    print("\n🧠 SUPERVISOR NODE")

    workflow_type = supervisor_agent(
        state["query"]
    )

    return {
        "workflow_type": workflow_type
    }

def memory_node(state):

    print("\n🧠 MEMORY NODE")

    memory = load_memory()

    summary = ""

    for item in memory[-5:]:

        summary += (
            f"\nTopic: {item['query']}\n"
        )

    return {
        "report": summary
    }

def supervisor_router(state):

    workflow = state["workflow_type"]

    if workflow == "MEMORY_LOOKUP":
        return "memory_lookup"

    if workflow == "MEMORY_SUMMARIZE":
        return "memory"

    return "research"

def memory_lookup_node(state):

    memory_item = find_in_memory(state["query"])

    if memory_item:

        summary = memory_summarizer(memory_item)

        return {
            "report": summary
        }

    return {
        "report": "No matching memory found."
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
builder.add_node("supervisor", supervisor_node)
builder.add_node("memory", memory_node)
builder.add_node("memory_lookup", memory_lookup_node)

# Start the workflow from the supervisor node
builder.set_entry_point("supervisor")

# Supervisor router
builder.add_conditional_edges("supervisor", supervisor_router, {"memory_lookup": "memory_lookup", "memory": "memory", "research": "research"})

# Memory nodes
builder.add_edge(
    "memory",
    END
)
builder.add_edge(
    "memory_lookup",
    END
)

# Research nodes
builder.add_edge("research", "validate_research")
builder.add_conditional_edges("validate_research", research_router, {"analysis": "analysis", "research": "research"})
builder.add_edge("analysis", "writer")
builder.add_edge( "writer", "reflection")
builder.add_edge("reflection", "revision")
builder.add_edge("revision", END)

graph = builder.compile()