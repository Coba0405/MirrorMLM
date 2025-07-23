from decimal import Decimal, ROUND_HALF_UP
from params import SimParams, cont_rate, grace_months

def rint(x: float) -> int:
    return int(Decimal(str(x)).quantize(Decimal("0"),rounding=ROUND_HALF_UP))

# 加入ロジック
# 人口ロジック用モジュールの用意
# backend/simulation/population.py に、calc_join_and_remainder(invites_pool) 関数を実装。


# 離脱ロジック

# month_loop.pyに人数を反映→・api/simulatoでJSON確認

def next_counts(prev_count, joins, month_index, cont_rate, grace_months):
    """
    prev_count: 全月末の人数
    joins: 今月加入人数
    month_index: 1始まり
    全員一律の近似モデル
    """
    # 加入して2ヶ月は100％残留（残留はその人のみが対象）
    if month_index <= grace_months:
        stayed = prev_count + joins
    else:
        stayed =rint((prev_count) * cont_rate) + joins
    return stayed
