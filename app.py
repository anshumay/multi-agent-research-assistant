from graph import graph


if __name__ == "__main__":

    query = input("Enter your research topic: ")

    result = graph.invoke({
        "query": query
    })

    print("\n📄 FINAL REPORT:\n")

    print(result["report"])