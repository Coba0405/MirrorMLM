from backend.bonus_calc import calc_bonus
from .population import next_counts, calc_joins

def simulate(params: "SimParams", members_tamplate):
    """
    members_template: {"A":{"parent:None"},"B":{"parent:"A"},"C":{"parent":"B"}}
    
    """