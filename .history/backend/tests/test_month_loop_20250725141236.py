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
params = SimParams(months=1, )
def test_initial_values_in_simulation():
    # count_child
    # count_grand
    # invites_pool_child
    # invites_pool_grand
# 子が20人勧誘ごとにcount_childに+1されるか
# 加入したユーザーがgrace_monthsの期間は継続率減少の対象外になっているか
# 加入してからcont_rateの継続率が適用されているか
# count_childが0の場合、invites_pool_grandが増えないこと
# 加入した子、孫にidが付与されていること
# 加入した子、孫にparentとjoin_monthが付与されていること
# 孫が加入したとき、ランダム
