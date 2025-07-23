from decimal import Decimal, ROUND_HALF_UP
from params import SimParams

def rint(x: float) -> int:
    return int(Decimal(str(x)).quantize(Decimal("0"),rounding=ROUND_HALF_UP))

# 加入ロジック
def calc_join_and_remainder(invites_pool):
    # invites_poolは「前月までの勧誘人数 + 今月の勧誘人数」が「既に」入った状態で渡される
    new_join, remainder = divmod(invites_pool, 20) #new_join→商→今月の加入人数、remainder→余り→次月に持ち越す勧誘人数
    return new_join, remainder

# 離脱ロジック

# month_loop.pyに人数を反映→・api/simulatoでJSON確認

def next_counts(params: SimParams,prev_count, joins, month_index, cont_rate, grace_months):
    """
    prev_count: 前月末の人数
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
