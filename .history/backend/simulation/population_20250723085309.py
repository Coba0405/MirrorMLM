from decimal import Decimal, ROUND_HALF_UP

def rint(x: float) -> int:
    return int(Decimal(str(x)).quantize(Decimal("0"),rounding=ROUND_HALF_UP))

def next_counts(prev_count, joins, month_index, cont_ratem grace_months):
    """
    prev_count: 全月末の人数
    joins: 今月加入人数
    month_index: 1始まり
    全員
    """
