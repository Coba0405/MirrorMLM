import sys, os
sys.path.append(os.getcwd())
from backend.simulation.month_loop import simulate
from backend.config.members import initial_members
from backend.domain.bonus import calc_bonus
from backend.simulation.params import SimParams

# メンバー初期化が正しく行われているか
def test_initial_member_value():
    assert len(initial_members()) == 1

# 20人勧誘した時にcount_childに+1されるか
def test_count_child_20_invites():
    params = SimParams(
        months = 2,
        self_monthly_yen = 30000,
        invite_per_month = 19,
        child_monthly_yen = 20000,
        grand_monthly_yen = 20000,
        cont_rate = 1,
        grace_months = 12,
        child_activity_rate = 0.0,
        invite_success_rate= 0.05
    )
    results = simulate(params,initial_members())
    print(results)
    results[0]["count_child"] == 1

# 勧誘が20人に満たない時count_childは変わらないか
def test_count_child_19_invites():
    params = Sim

# 加入したユーザーがgrace_monthsの期間は継続率減少の対象外になっているか
# 加入してからcont_rateの継続率が適用されているか
# count_childが0の場合、invites_pool_grandが増えないこと
# 加入した子、孫にidが付与されていること
# 加入した子、孫にparentとjoin_monthが付与されていること
# 現在のアクティブな子の数を数える
# 現在のアクティブな孫の数を数える
# calc_bonusの返り値が正しいか

