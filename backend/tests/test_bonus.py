import json, sys, os
from decimal import Decimal
sys.path.append(os.getcwd())
from backend.domain.bonus import calc_bonus
from backend.domain.constants import PV_PER_YEN, BV_PER_PV, BONUS_TABLE

members = {
    "A": {"parent": None},
    "B": {"parent": "A"},
    "C": {"parent": "B"},
}

# 指定したPVから逆算してYENに変換
def pv_to_yen(pv):
    return pv / PV_PER_YEN

def get_expected_rate(pv):
    for threshold, rate in BONUS_TABLE:
        if pv >= threshold:
            return rate
    return Decimal("0.00")

# PV境界値テスト
def test_calc_bonus():
    test_cases = [29999, 30000, 89999, 90000, 179999, 180000, 359999, 360000, 599999, 600000, 999999, 1000000, 1499999, 1500000]
    for pv in test_cases:
        rate =  get_expected_rate(pv)
        bv = pv * BV_PER_PV
        expected_bonus = bv * rate

        yen = pv / PV_PER_YEN
        purchases = {"A": yen}
        members = {"A": {"parent": None, "join_month": 0}}
        result = calc_bonus(purchases, members, "A")

        actual_rate = Decimal(str(result["A"]["rate"]))
        actual_bonus = Decimal(str(result["A"]["bonus"]))

        assert actual_rate == Decimal(rate)
        assert actual_bonus.quantize(Decimal("1.")) == expected_bonus.quantize(Decimal("1."))


def test_bonus_case_a():
    purchases = {"A": 30000, "B": 20000, "C": 20000}
    result = calc_bonus(purchases, members, root_id="A")
    assert result["A"]["bonus"] == 1909


# 親以外も返す場合は以下をアクティブ化bonus.pyの5をコメントアウトし6をアクティブ化する
# def test_bonus_case_a():
#     purchases = {"A": 10000, "B": 1140000, "C": 800000}
#     result = calc_bonus(purchases, members, root_id="A")
#     assert result["A"]["bonus"] == 1636
#     assert result["B"]["bonus"] == 230182
#     assert result["C"]["bonus"] == 87273

# def test_bonus_case_b():
#     purchases = {"A": 50000, "B": 470000, "C": 20000}
#     result = calc_bonus(purchases, members, root_id="A")
#     assert result["A"]["bonus"] == 4091
#     assert result["B"]["bonus"] == 40091
#     assert result["C"]["bonus"] == 0

# def test_bonus_case_c():
#     purchases = {"A": 30000, "B": 20000, "C": 20000}
#     result = calc_bonus(purchases, members, root_id="A")
#     print("A DEBUG:", result["A"])
#     print("B DEBUG:", result["B"])
#     print("C DEBUG:", result["C"])
#     assert result["A"]["bonus"] == 1909
#     assert result["B"]["bonus"] == 0
#     assert result["C"]["bonus"] == 0
