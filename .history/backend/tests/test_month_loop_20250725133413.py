import sys, os
sys.path.append(os.getcwd())
from backend.simulation.month_loop import simulate
from backend.config.members import initial_members
from backend.domain.bonus import calc_bonus
from backend.simulation.params import SimParams

# メンバー初期化が正しく行われているか
def test_initial_member_value():
    assert len(initial_members()) == 1

# simulateの初期値が正常か
params = SimParams
def test_initial_values_in_simulation():
    # count_child
    assert 
    # count_grand
    # invites_pool_child
    # invites_pool_grand



# def is_active():
#     assert current_month - meta["join_month"] < grace_months

# # 月毎のループ制御
# def test_month_loop_logic():
#     for month in range(1, SimParams.months + 1):
#         assert month == SimParams.months + 1