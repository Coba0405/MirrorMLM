import json
from backend.app import app

def test_bonus_endpoint():
    client = app.test_client()
    payload = {"purchases": {"A":50000,"B":100000,"C":20000}}
    res = client.post("/api/bonus", json=payload)
    assert res.status_code == 200
    # json
    assert res.is_json
    data = res.get_json()
    # 親だけ帰っているか
    assert
    data = res.get_json()
    assert "A" in data
    print("A DEBUG:", ["A"])
    assert data["A"]["bonus"] == 32193
