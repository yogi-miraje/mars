# mars

Multi-Agentic Research System

This repository contains a simple prototype implementation of a multi-agent research assistant written in Python. The system spawns subagents to perform web searches in parallel and synthesizes their results using a language model router.

## Usage

```bash
pip install -r requirements.txt  # install dependencies
python -m multi_agent_research.main
```

You will be prompted for a research question and the agents will attempt to produce a concise answer.

### Search Provider

By default the system uses DuckDuckGo for web search. To use the Tavily Search API instead, set the following environment variables:

```bash
export SEARCH_PROVIDER=tavily
export TAVILY_API_KEY=your_api_key_here
```

DuckDuckGo will be used whenever `SEARCH_PROVIDER` is not set.
