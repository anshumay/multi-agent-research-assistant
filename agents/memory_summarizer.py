from utils.llm import call_llm


def memory_summarizer(memory_item):

    prompt = f"""
    You are a helpful assistant.

    Convert the stored research into a concise,
    human-readable summary.

    Research:
    {memory_item}

    Return a well-structured summary.
    """

    return call_llm(prompt)