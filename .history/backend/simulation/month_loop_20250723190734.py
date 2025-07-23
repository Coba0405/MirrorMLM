from backend.domain.bonus import calc_bonus
from .population import next_counts, calc_join_and_remainder

def simulate(params: SimParams, members: dict) -> list:
    recode = []
    count_child = 0, #現在の子の人数
    count_grand = 0, #現在の孫の人数
    invites_pool_child = 0, #勧誘した子の数
    invites_pool_grand = 0, #勧誘した孫の数
    joined

    recode.append(params)
