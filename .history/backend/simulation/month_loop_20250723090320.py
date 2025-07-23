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
    cum_invited
