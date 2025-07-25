import sys, os
sys.path.append(os.getcwd())
from backend.simulation.month_loop import simulate
from backend.config.members import initial_members
from backend.domain.bonus import calc_bonus
from backend.simulation.params import SimParams

# 初期化が正しく行われているか
def test_initial_value():
    assert len(initial_members()) == 1

def test_initial_values_in_simulation():
    params = SimParams(months=1, self_monthly_yen=10000, invite_per_month=0)
    results = simulate(params, initial_members())
    assert results[0]["count"] == 0
    assert results[0]["count_grand"] == 0
    assert results[0]["invites_pool_child"] == 0
    assert results[0]["invites_pool_grand"] == 0
    # simulate.count_child == 0
    # simulate.count_grand == 0
    # simulate.invites_pool_child == 0
    # simulate.invites_pool_child == 0

# def is_active():
#     assert current_month - meta["join_month"] < grace_months

# # 月毎のループ制御
# def test_month_loop_logic():
#     for month in range(1, SimParams.months + 1):
#         assert month == SimParams.months + 1