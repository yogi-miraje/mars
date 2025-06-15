import pytest
from fastapi.testclient import TestClient

from mars.gateway import app

client = TestClient(app)


def test_query_endpoint():
    resp = client.post("/query", params={"user_id": "u1", "prompt_id": "p1", "text": "hello"})
    assert resp.status_code == 200
    data = resp.json()
    assert "result" in data
