import json
from backend.domain.bonus import bonus_calc

members = {
    "A": {"parent": None},
    "B": {"parent": "A"},
    "C": {"parent": "B"},
}

def test_bonus_case_abc():
    purchases = {"A": 50000, "B": 100000, "C": 20000}
    result = domain.bonus(purchases, members, root_id="A")
    a = result["A"]
    # 期待値は以前 curl で確認した 6,000円 等
    assert a["bonus"] == 6000
    assert a["group_pv"] >= 0
