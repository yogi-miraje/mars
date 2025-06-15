import json
import os
from typing import Any, Dict


class Memory:
    """Simple file-backed key-value memory."""

    def __init__(self, filepath: str = "memory.json"):
        self.filepath = filepath
        self._data: Dict[str, Any] = {}
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r", encoding="utf-8") as f:
                    self._data = json.load(f)
            except Exception:
                self._data = {}

    def save(self, key: str, value: Any) -> None:
        self._data[key] = value
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(self._data, f, indent=2)
        except Exception:
            pass

    def load(self, key: str) -> Any:
        return self._data.get(key)
