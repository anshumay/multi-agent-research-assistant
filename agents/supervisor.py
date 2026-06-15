from utils.llm import call_llm


def supervisor_agent(query):

    prompt = f"""
    You are a workflow supervisor.

    Choose ONE:

    RESEARCH
    MEMORY_LOOKUP
    MEMORY_SUMMARIZE

    Rules:

    RESEARCH
    - New topic
    - Needs web search

    MEMORY_LOOKUP
    - User asks about a specific previously researched topic

    Examples:
    Softmax
    BERT
    Transformer Models

    MEMORY_SUMMARIZE
    - User asks:
    - Show previous research
    - Summarize past research
    - What have I researched before?

    Return ONLY one option.

    Query:
    {query}
    """
    return call_llm(prompt).strip()