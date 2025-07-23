from decimal import Decimal, ROUND_HALF_UP
# 差額ボーナス計算モジュール
PV_RATE = Decimal("1") / Decimal("1.3")    # 円→PV
BV_RATE = Decimal("1.395")     # PB→BV
# 成績別ボーナス表（PV下限、還元率を大きい順にする
BONUS_TABLE = [
    (1_500_000, Decimal("0.21")),
    (1_000_000, Decimal("0.18")),
    (600_000,   Decimal("0.15")),
    (360_000,   Decimal("0.12")),
    (180_000,   Decimal("0.09")),
    (90_000,    Decimal("0.06")),
    (30_000,    Decimal("0.03")),
    (0,         Decimal("0.00")),
]

def rint(x: Decimal) -> int:
    # 四捨五入で整数化
    return int(x.quantize(Decimal("0"), rounding=ROUND_HALF_UP))

def pv_to_rate(pv: int) -> Decimal:
    """グループ PVから還元率を返す"""
    for threshold, rate in BONUS_TABLE:
        if pv >= threshold:
            return rate
    return Decimal("0.0")

def calc_bonus(purchases: dict, members: dict, root_id: str):
    """
    purchases: {"A":50000, "B":30000, "C":20000}
    root_id:   "A" 固定（今回は常にAと明示）

    返り値は root_id だけの dict
    """
    # 1. 個人値(personal)
    info = {}
    for mid, yen in purchases.items():
        pv = PV_RATE * Decimal(yen)
        bv = pv * BV_RATE
        info[mid] = {
            "personal_pv": rint(pv),
            "personal_bv": rint(bv),
            "children": []
        }

    # 2. 親子リンク
    for cid, meta in members.items():
        parent = meta.get("parent")
        if parent and cid in info:
            info.setdefault(parent, {"children": [], "personal_pv": 0, "personal_bv": 0})
            info[parent]["children"].append(cid)
            # info.setdefault(parent, {"children": []})
            # info[parent].setdefault("children", []).append(cid)

    # 3. group 集計 (post-order)
    def accum(mid):
        total_pv = info[mid].get("personal_pv", 0)
        total_bv = info[mid].get("personal_bv", 0)
        for child in info[mid].get("children", []):
            cpv, cbv = accum(child)
            total_pv += cpv
            total_bv += cbv
        info[mid]["group_pv"] = total_pv
        info[mid]["group_bv"] = total_bv
        info[mid]["rate"] = pv_to_rate(total_pv)
        return total_pv, total_bv
    accum(root_id)

    # 4. 差額ボーナス（top-down）
    def diff_bonus(mid):
        subtotal = Decimal(info[mid]["group_bv"]) * info[mid]["rate"]
        child_sub = Decimal("0")
        for child in info[mid].get("children", []):
            child_sub += diff_bonus(child)
        info[mid]["bonus"] = rint(subtotal - child_sub)
        return subtotal

    diff_bonus(root_id)

    # 5. 親だけ返す
    # parent_only = {
    #     root_id: {
    #         "personal_pv": info[root_id]["personal_pv"],
    #         "personal_bv": info[root_id]["personal_bv"],
    #         "group_pv":    info[root_id]["group_pv"],
    #         "group_bv":    info[root_id]["group_bv"],
    #         "rate":        float(info[root_id]["rate"]),  # JSON化で小数→float
    #         "bonus":       info[root_id]["bonus"],
    #     }
    # }
    # return parent_only

    # 5. 全員分返す（test_bonus.pyテスト用）
    # Decimal は JSON 化しづらいので float にしたい項目があれば変換
    for d in info.values():
        if isinstance(d.get("rate"), Decimal):
            d["rate"] = float(d["rate"])
    return info
