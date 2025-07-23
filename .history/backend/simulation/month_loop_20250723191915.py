from backend.domain.bonus import calc_bonus
from .population import next_counts, calc_join_and_remainder
from params import invite_per_month

def simulate(params: SimParams, members: dict) -> list:
    recode = []
    count_child = 0, #現在の子の人数
    count_grand = 0, #現在の孫の人数
    invites_pool_child = 0, #勧誘した子の数
    invites_pool_grand = 0, #勧誘した孫の数

    for month in range(1, params.months + 1):
        # 勧誘プールへ追加
        invites_pool_child += invite_per_month(params)
        invites_pool_grand += invite_per_month(params)
        # 新規加入数とあまりの計算
        new_join, remainder = divmod(invites_pool_child)

    recode.append(params)
