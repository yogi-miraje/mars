import os
from dotenv import load_dotenv
from openai import OpenAI

def run(query: str | None = None):
    """Run the Mars agent with a given query or the default example."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)
    if not query:
        query = (
            "Find board members of top 10 S&P 500 companies by market cap.")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": query}],
    )
    print(response.choices[0].message.content)

