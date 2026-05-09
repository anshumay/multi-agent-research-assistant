# 🤖 Multi-Agent Research Assistant

A modular Agentic AI application built using
- LangGraph orchestration
- Multi-agent workflows
- Real-time web search
- Persistent memory
- Streamlit UI

This project demonstrates how specialized AI agents can collaborate to perform:
- research
- analysis
- structured reasoning
- report generation

---

# 🚀 Features

## ✅ Multi-Agent Architecture
The system uses specialized agents:
- **Research Agent** → gathers grounded information using web search
- **Analysis Agent** → extracts themes and insights
- **Writer Agent** → generates structured reports

---

## ✅ LangGraph Orchestration
Uses LangGraph for:
- stateful workflows
- node-based execution
- conditional routing
- retry handling
- shared state management

---

## ✅ Tool Grounding
The Research Agent uses:
- SerpAPI
- real search results
- source-backed reasoning

This reduces hallucinations and improves reliability.

---

## ✅ Persistent Memory
The system stores previous research history and injects contextual memory into future workflows.

---

## ✅ Streamlit UI
Interactive frontend with:
- sidebar controls
- memory viewer
- expandable outputs
- report generation
- download support

---

# 🏗️ Architecture

```text
                ┌────────────────────┐
                │    Streamlit UI    │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │    LangGraph       │
                │   Orchestration    │
                └─────────┬──────────┘
                          │
          ┌───────────────┼───────────────┐
          ▼                               ▼
┌──────────────────┐           ┌──────────────────┐
│  Research Agent  │           │ Persistent Memory│
└─────────┬────────┘           └──────────────────┘
          │
          ▼
┌──────────────────┐
│ Validation Node  │
└─────────┬────────┘
          │
          ▼
┌──────────────────┐
│ Analysis Agent   │
└─────────┬────────┘
          │
          ▼
┌──────────────────┐
│ Writer Agent     │
└─────────┬────────┘
          │
          ▼
   Structured Report
```

---

# 🧠 Agent Workflow

```text
User Query
    ↓
Research Agent
    ↓
Validation Node
    ↓
Analysis Agent
    ↓
Writer Agent
    ↓
Final Report
```

---

# 📂 Project Structure

```text
multi-agent-research-assistant/
│
├── agents/
│   ├── researcher.py
│   ├── analyst.py
│   └── writer.py
│
├── tools/
│   └── search.py
│
├── utils/
│   ├── parser.py
│   ├── llm.py
│   └── memory.py
│
├── memory/
│   └── .gitkeep
│
├── graph.py
├── streamlit_app.py
├── app.py
├── requirements.txt
├── .env.example
└── README.md
```

---

# ⚙️ Tech Stack

| Component | Technology |
|---|---|
| Orchestration | LangGraph |
| LLM | OpenAI GPT |
| Frontend | Streamlit |
| Search Tool | SerpAPI |
| Language | Python |
| Memory | JSON-based persistence |

---

# 🔧 Installation

## 1. Clone Repository

```bash
git clone https://github.com/anshumay/multi-agent-research-assistant.git

cd multi-agent-research-assistant
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

### macOS/Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
SERPAPI_API_KEY=your_serpapi_api_key
```

---

# ▶️ Running the Application

## Terminal Version

```bash
python app.py
```

---

## Streamlit UI

```bash
streamlit run streamlit_app.py
```

---

# 🧪 Example Queries

Try:
- BERT
- Transformer Models
- Agentic AI Trends
- Vector Databases Comparison
- GenAI in Healthcare

---

# 🔄 LangGraph Features Implemented

## ✅ Stateful Workflow
Shared state across nodes.

## ✅ Conditional Routing
Validation-based routing and retries.

## ✅ Retry Handling
Automatic retry logic for failed research steps.

## ✅ Structured Outputs
JSON-based communication between agents.

---

# 📌 Future Improvements

Planned enhancements:
- RAG integration
- Vector databases
- PDF upload support
- Multi-user memory
- Parallel agents
- Supervisor agent
- Deployment on Streamlit Cloud
- Docker support
- Authentication

---

# 🧠 Key Learnings

This project explores:
- Agentic AI systems
- Multi-agent orchestration
- Stateful workflows
- Tool grounding
- Long-term memory
- Structured reasoning
- LLM system design

---

# 📸 UI Preview

_Add screenshots here after deployment._

---

# 👨‍💻 Author

Built by Anshumay Rath

---

# ⭐ If You Like This Project

Consider starring the repository and sharing feedback.

