from decimal import Decimal, ROUND_HALF_UP

def rint(x: float) -> int:
    return int(Decimal(str(x)).quantize(Decimal("0"),rounding=ROUND_HALF_UP))

def next_counts(prev_count, joins, month_index, cont)
