import json
from bonus_cals import cals_bonus

members = {
    "A": {"parent": None},
    "B": {"parent": "A"},
    "C": {"parent": "B"},
}

def test_bonus_case_abc():
    purchases = {"A": 50000, "B": 100000, "C": 20000}
    result = calc_bonus(purchases, members, root_id="A")
    a = result["A"]
    assert a["bonus"]
