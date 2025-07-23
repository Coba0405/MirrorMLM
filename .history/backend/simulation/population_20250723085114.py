from decimal import Decimal, ROUND_HALF_UP

def rint(x: float) -> int:
    return int(Decimal(str(x)).quantize(Decimal("0"),rounding=RO))
