from decimal import Decimal, ROUND_HALF_UP

ROUND2 = Decimal("0.01")
def q2(value: Decimal | float | int) -> Decimal:

    return Decimal(value).quantize(ROUND2, ROUND_HALF_UP)
