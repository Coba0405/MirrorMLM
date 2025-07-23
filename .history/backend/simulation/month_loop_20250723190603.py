from backend.domain.bonus import calc_bonus
from .population import next_counts, calc_join_and_remainder

def simulate(params: SimParams, members: dict) -> list:
    recode = []
    count_child = 0, #現在の子の人数
    count_grand = 0,
    inva

    recode.append(params)
