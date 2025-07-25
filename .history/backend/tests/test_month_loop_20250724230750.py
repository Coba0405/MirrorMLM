import sys, os
sys.path.append(os.getcwd())
from backend.simulation.month_loop import simulate, is_active
from backend.config.members import initial_members
from backend.domain.bonus import calc_bonus
from backend.simulation.params import SimParams

# 初期化が正しく行われているか
def test_initial_value():
    initial_members.count == 1
    simulate.count_child == 0
    simulate.count_grand == 0
    simulate.invites_pool_child == 0
    simulate.invites_pool_child == 0

def is_active():
    
    current_month - join_month

def test_month_loop_logic():
