import os
import requests
from typing import List, Optional, Dict


class Tool:
    name: str = "base"
    description: str = ""

    def run(self, query: str) -> str:
        raise NotImplementedError


class WebSearchTool(Tool):
    name = "web_search"
    description = "Perform a web search and return text snippets"

    def __init__(
        self,
        provider: Optional[str] = None,
        duckduckgo_url: str | None = None,
        tavily_url: str | None = None,
        tavily_api_key: str | None = None,
    ):
        self.provider = provider or os.getenv("SEARCH_PROVIDER", "duckduckgo")
        self.duckduckgo_url = (
            duckduckgo_url or "https://duckduckgo.com/?q={query}&t=h_&ia=web"
        )
        self.tavily_url = tavily_url or "https://api.tavily.com/search"
        self.tavily_api_key = tavily_api_key or os.getenv("TAVILY_API_KEY")

    def _duckduckgo_search(self, query: str) -> str:
        url = self.duckduckgo_url.format(query=query)
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        return resp.text[:1000]

    def _tavily_search(self, query: str) -> str:
        if not self.tavily_api_key:
            raise ValueError("TAVILY_API_KEY not set")
        params: Dict[str, str] = {
            "api_key": self.tavily_api_key,
            "query": query,
            "search_depth": "basic",
        }
        resp = requests.get(self.tavily_url, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        results = data.get("results") or []
        snippets = []
        for r in results[:3]:
            title = r.get("title", "")
            content = r.get("content", "")
            snippets.append(f"{title}: {content}")
        return "\n".join(snippets)

    def run(self, query: str) -> str:
        try:
            if self.provider == "tavily":
                return self._tavily_search(query)
            return self._duckduckgo_search(query)
        except Exception as e:
            return f"Search error: {e}"
