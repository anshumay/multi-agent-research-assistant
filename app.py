from agents import research_agent, analyst_agent, writer_agent, parse_json

def run_pipeline(query):
    print("\n🔍 Researching...\n")
    research_raw = research_agent(query)
    research = parse_json(research_raw)

    print("\n📦 STRUCTURED RESEARCH:\n")
    print(research)

    print("\n📊 Analyzing...\n")
    analysis_raw = analyst_agent(research)
    analysis = parse_json(analysis_raw)

    print("\n📦 STRUCTURED ANALYSIS:\n")
    print(analysis)

    print("\n✍️ Writing report...\n")
    report = writer_agent(analysis)

    return report


if __name__ == "__main__":
    user_query = input("Enter your research topic: ")
    final_output = run_pipeline(user_query) 

    print("\n📄 FINAL REPORT:\n")
    print(final_output)
