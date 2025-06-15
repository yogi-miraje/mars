from .agent import LeadResearcherAgent


def main() -> None:
    query = input("Enter your research question: ")
    lead = LeadResearcherAgent()
    answer = lead.run(query)
    print("\nFinal Answer:\n", answer)


if __name__ == "__main__":
    main()
