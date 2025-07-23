import json
from backend.bonus_calc import calc_bonus

members = {
    "A": {"parent": None},
    "B": {"parent": "A"},
    "C": {"parent": "B"},
}

def test_bonus_case_abc():
    purchases = {"A": 50000, "B": 100000, "C": 20000}
    result = calc_bonus(purchases, members, root_id="A")
    print("DEBUG:", result["A"]) 
    a = result["A"]
    assert a["bonus"] == 6000
    assert a["group_pv"] >= 0
