import sys, os
sys.path.append(os.getcwd())
from backend.simulation.month_loop import simulate
from backend.config.members import initial_members
from backend.domain.bonus import calc_bonus
from backend.simulation.params import SimParams

def test_initial_value():
    simulate.initial_members.count == 1
    simulate.count_child == 0
    simulate.count_grand == 0
    invites_pool_child == 0
