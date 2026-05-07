from utils.llm import call_llm

def writer_agent(analysis_data):
    prompt = f"""
    You are a professional report writer.

    Use the structured insights below to create a detailed report.

    Structure:
    - Title
    - Executive Summary
    - Key Insights
    - Detailed Analysis
    - Conclusion

    Analysis:
    {analysis_data}
    """

    return call_llm(prompt)