from decimal import Decimal

YEN_PER_PV = Decimal("1")Decimal(1.2987)           #1PVあたりの金額
BV_PER_PV = Decimal(1.395)             #PVからBVに換算
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
