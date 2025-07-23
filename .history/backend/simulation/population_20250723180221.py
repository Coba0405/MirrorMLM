from decimal import Decimal, ROUND_HALF_UP
from params import SimParams, cont_rate, grace_months

def rint(x: float) -> int:
    return int(Decimal(str(x)).quantize(Decimal("0"),rounding=ROUND_HALF_UP))

# 加入ロジック
def calc_join_and_remainder(invites_pool):
    cum_invited = [0]
    invites_pool += (cum_invited_child + invite_per_month)
    if invites_pool % 20 == 0:
        new_join += 1


    month_loop.pyからcum_invited_child = 0を取得する
    params.pyからinvite_per_monthを取得する
    invite_per_monthの人数をcum_invited_childに追加する
    20人を超える月（40人・60人）の場合は divmodを使用
    cum_invited_childの人数が20に達したときcount_child += 1する


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
