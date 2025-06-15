# Mars

Mult-Agentic Research System

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Create a `.env` file with your OpenAI key:

```
OPENAI_API_KEY=your-key-here
```

## Running

Call the agent from Python:

```python
import mars
mars.run()
```

This defaults to the query:

```
Find board members of top 10 S&P 500 companies by market cap.
```

You can pass a custom query:

```python
mars.run("your question")
```

