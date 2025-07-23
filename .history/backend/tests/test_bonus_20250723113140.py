import json
from backend.domain.bonus import calc_bonus

members = {
    "A": {"parent": None},
    "B": {"parent": "A"},
    "C": {"parent": "B"},
}

def test_bonus_case_abc():
    purchases = {"A": 50000, "B": 100000, "C": 20000}
    result = calc_bonus(purchases, members, root_id="A")
    print("A DEBUG:", result["A"])
    print("B DEBUG:", result["B"])
    print("C DEBUG:", result["C"])
    assert result["A"]["bonus"] == ["A"][]
    # a = result["A"]
    # 期待値は以前 curl で確認した 6,000円 等
    # assert a["bonus"] == 6000
    # assert a["group_pv"] >= 0
