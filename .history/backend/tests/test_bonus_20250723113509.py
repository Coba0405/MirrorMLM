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
    print("")
    assert result["A"]["bonus"] 
