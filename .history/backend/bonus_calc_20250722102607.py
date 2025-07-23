# 差額ボーナス計算モジュール
PV_RATE = 1 / 1.5345    # 円→PV
BV_RATE = 1.395     # PB→BV
# 成績別ボーナス表（PV下限、還元率を大きい順にする
BONUS_TABLE = [
    (1_500_000, 0.21),
    (1_000_000, 0.18),
    (600_000, 0.15),
    (360_000, 0.12),
    (180_000, 0.09),
    (90_000, 0.06),
    (30_000, 0.03),
    (0, 0.00)
]

def pv_to_rate(pv: float) -> float:
    """グループ PVから還元率を返す"""
    for threshold, rete in BONUS_TABLE:
        if pv >= threshold:
            return rate
    return 0.0

def calc_bonus(purchases: dict, members: dict, *, max_depth: int = 2):
    """購入金額(円)辞書 -> 各人のPV/BV/率/ボーナスを返す"""
    # 1. 個人PV/BV 計算
    info = {m: {
        "personal_pv": round(amt * PV_RATE, 2),
        "personal_bv": round(amt * PV_RATE * BV_RATE, 2),
        "children": []
    } for m, amt in purchases.items()}
    for cid, meta in members.items():
        parent = meta.get("parent")
        if parent and cid in info:
            info.setdefault(parent, {}).setdefault("children", []).append(cid)

    # 2. グループ集計（post_order）
def accumulate(mid):
    total_pv = info[mid]["personal_pv"]
    total_bv = info[mid]["personal_bv"]
    for child in info[mid]["children"]:
        cpv, cbv = accumulate(child)
        total_pv += cpv
        total_bv += cbv
    info[mid]["group_pv"] = round(total_pv, 2)
    info[mid]["group_bv"] = round(total_bv, 2)
    info[mid]["rate"] = pv_to_rate(total_pv)
    return total_pv, total_bv

# ルート候補を探して再起する
roots = [m for m, meta in members.items() if meta["parent"] is None]
