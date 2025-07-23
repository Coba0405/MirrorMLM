import json
from backend.domain.bonus import calc_bonus

members = {
    "A": {"parent": None},
    "B": {"parent": "A"},
    "C": {"parent": "B"},
}

def test_bonus_case_a():
    purchases = {"A": 10000, "B": 1140000, "C": 800000}
    result = calc_bonus(purchases, members, root_id="A")
    print("A DEBUG:", result["A"])
    print("B DEBUG:", result["B"])
    print("C DEBUG:", result["C"])
    assert result["A"]["bonus"] == 64707

def test_bonus_case_b():
    purchases = {"A": 50000, "B": 450000, "C": 20000}
    result = calc_bonus(purchases, members, root_id="A")
    print("A DEBUG:", result["A"])
    print("B DEBUG:", result["B"])
    print("C DEBUG:", result["C"])
    assert result["A"]["bonus"] == 6438

def test_bonus_case_b():
    purchases = {"A": 50000, "B": 450000, "C": 20000}
    result = calc_bonus(purchases, members, root_id="A")
    print("A DEBUG:", result["A"])
    print("B DEBUG:", result["B"])
    print("C DEBUG:", result["C"])
    assert result["A"]["bonus"] == 6438
