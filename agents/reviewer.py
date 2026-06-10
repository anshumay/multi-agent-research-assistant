from utils.llm import call_llm


def reviewer_agent(report):

    prompt = f"""
    You are an expert reviewer.

    Review the report below.

    Evaluate:
    - Completeness
    - Clarity
    - Structure
    - Missing insights
    - Repetition

    Return:

    Strengths:
    ...

    Improvements:
    ...

    Report:
    {report}
    """

    return call_llm(prompt)