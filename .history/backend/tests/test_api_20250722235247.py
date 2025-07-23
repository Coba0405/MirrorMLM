import json
from app import app

def test_bonus_endpoint():
    client = app.test_client()
    payload = {"purchases": {"A": 50000, "B": 100000, "C": 20000}}
    res = client.post("/api/bonus", json=payload)
    assert res.status_code == 200
    data = res.get_json()
    assert "A" in data
    assert data["A"]["bonus"] == 6000
