# Multi-Agent Research Assistant

A multi-agent AI system that performs:
- Web research
- Analysis
- Structured report generation

## Features
- Research Agent
- Analyst Agent
- Writer Agent
- Real web search integration
- Structured JSON outputs

## Tech Stack
- Python
- OpenAI API
- SerpAPI
- Streamlit
- LangGraph

## LangGraph Workflow

The project uses LangGraph for orchestration with:

- Shared agent state
- Node-based execution
- Sequential workflow management

Flow:
Research → Analysis → Writer

## Architecture

UI (Streamlit)
      ↓
LangGraph Orchestration
      ↓
Research Agent
      ↓
Analysis Agent
      ↓
Writer Agent
      ↓
Persistent Memory

## Setup

```bash
pip install -r requirements.txt