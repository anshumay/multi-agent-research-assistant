from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.researcher import research_agent
from agents.analyst import analyst_agent
from agents.writer import writer_agent

from utils.parser import parse_json


# -----------------------------
# STATE
# -----------------------------

class AgentState(TypedDict):
    query: str
    research: dict
    analysis: dict
    report: str


# -----------------------------
# NODES
# -----------------------------

def research_node(state: AgentState):

    print("\n🔍 RESEARCH NODE")

    research_raw = research_agent(state["query"])
    research = parse_json(research_raw)

    return {
        "research": research
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
        "report": report
    }


# -----------------------------
# GRAPH
# -----------------------------

builder = StateGraph(AgentState)

builder.add_node("research", research_node)
builder.add_node("analysis", analysis_node)
builder.add_node("writer", writer_node)

builder.set_entry_point("research")

builder.add_edge("research", "analysis")
builder.add_edge("analysis", "writer")
builder.add_edge("writer", END)

graph = builder.compile()