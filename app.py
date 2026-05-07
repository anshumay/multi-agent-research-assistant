from agents.researcher import research_agent
from agents.analyst import analyst_agent
from agents.writer import writer_agent

from utils.parser import parse_json


def run_pipeline(query):
    print("\n🔍 Researching...\n")

    research_raw = research_agent(query)
    research = parse_json(research_raw)

    if "error" in research:
        print("\n❌ Research parsing failed")
        return

    print("\n" + "="*50)
    print("\n📦 STRUCTURED RESEARCH:\n")
    print("="*50)
    print(research)

    print("\n📊 Analyzing...\n")

    analysis_raw = analyst_agent(research)
    analysis = parse_json(analysis_raw)
    if "error" in analysis:
        print("\n❌ Analysis parsing failed")
        return

    print("\n" + "="*50)
    print("\n📦 STRUCTURED ANALYSIS:\n")
    print("="*50)
    print(analysis)


    print("\n✍️ Writing report...\n")
    report = writer_agent(analysis)

    return report


if __name__ == "__main__":
    query = input("Enter your research topic: ")

    final_report = run_pipeline(query)

    print("\n" + "="*50)
    print("\n📄 FINAL REPORT:\n")
    print("="*50)
    print(final_report)