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
    # 親だけ返っているか
    assert set(data.keys()) == {"A"}

    # 必須フィールドが存在するか&正しいか
    a = data["A"]
    
