from decimal import Decimal, ROUND_HALF_UP
from params import SimParams, cont_rate, grace_months

def rint(x: float) -> int:
    return int(Decimal(str(x)).quantize(Decimal("0"),rounding=ROUND_HALF_UP))

# 加入ロジック
def calc_join(cum_invited, prev_joined):
    """20人勧誘で1人加入（端数は四捨五入）"""
    target = rint(cum_invited / 20)
    return max(target - prev_joined, 0)
    # 入力した月間勧誘人数が勧誘人数(cum_invited_child/cum_invited_cgrand)が20人に達するごとに(count_child/count_grand)1人追加する(1ヶ月で40人や60人勧誘したらどう処理する？)
    # 20人に達したとき(cum_invited_child/cum_invited_cgrand)を初期化する
    #
def calc_join_and_remainder()

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
