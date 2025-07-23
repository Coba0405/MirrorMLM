from decimal import Decimal, ROUND_HALF_UP

def rint(x: float) -> int:
    return int(Decimal(str(x)).quantize(Decimal("0"),rounding=ROUND_HALF_UP))

def next_counts(prev_count, joins, month_index, cont_rate, grace_months):
    """
    prev_count: 全月末の人数
    joins: 今月加入人数
    month_index: 1始まり
    全員一律の近似モデル
    """
    # 加入して2ヶ月は100％残留
    if month_index <= grace_months:
        stayed = prev_count + joins
    else:
        stayed =rint((prev_count) * cont_rate) + joins
    return stayed

def calc_joins(cum_invited, prev_joined):
    """20人勧誘で1人加入（端数は四捨五入）"""
    target = rint(cum_invited / 20)
    return max(target - prev_joined, 0)
