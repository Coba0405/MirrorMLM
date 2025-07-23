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
    cum_invited_self = 0
    cum_invited_child = 0
    cum_invited_grand = 0
    joined_self = 0
    joined_child = 0
    joined_grand = 0

    for m in range(1, params.months + 1):
        # 勧誘人数
        cum_invited_self += params.invite
