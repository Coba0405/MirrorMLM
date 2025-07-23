from backend.bonus_calc import calc_bonus
from .population import next_counts, calc_joins

def simulate(params: "SimParams", members_tamplate):
    """
    members_template: {"A":{"parent:None"},"B":{"parent:"A"},"C":{"parent":"B"}}
    戻り値: 月次レコードのリスト
    """
    records = []
    # 人数初期化
    count_child = 0
    count_grand = 0
    cum_invited_self = 0 #自分は固定で1
    cum_invited_child = 0
    cum_invited_grand = 0
    joined_self = 0
    joined_child = 0
    joined_grand = 0

    for m in range(1, params.months + 1):
        # 勧誘人数
        cum_invited_self += params.invite_per_month
        cum_invited_child += params.invite_per_month
        cum_invited_grand += params.invite_per_month

        # 加入人数
        new_child = cals_joins(cum_invited_child, joined_child)
        new_grand = cals_joins(cum_invited_grand, joined_grand)

        # 人数更新
        count_child = next_counts(count_child, new_child, m, params.cont_rate, params.grace_months)
        joined_child += new_child

        count_grand = next_counts(count_child, new_child, m, params.cont_rate, params.grace_months)
        joined_grand +=
