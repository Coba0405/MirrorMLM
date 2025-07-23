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
    
