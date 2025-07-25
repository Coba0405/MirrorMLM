import sys, os
sys.path.append(os.getcwd())
from backend.simulation.month_loop import simulate
from backend.config.members import initial_members
from backend.domain.bonus import calc_bonus
from backend.simulation.params import SimParams

# メンバー初期化が正しく行われているか
def test_initial_member_value():
    assert len(initial_members()) == 1

# 勧誘が20人に満たない時count_childは変わらないか
def test_count_child_19_invites():
    params = SimParams(
        months = 1,
        self_monthly_yen = 30000,
        invite_per_month = 19,
        child_monthly_yen = 20000,
        grand_monthly_yen = 20000,
        cont_rate = 0.9439,
        grace_months = 2,
        child_activity_rate = 0.9,
        invite_success_rate= 0.05
    )
    result = simulate(params,initial_members)
    # print(result)
    assert result[0]["count_child"] == 0

# 20人勧誘した時にcount_childに+1されるか
def test_count_child_20_invites():
    params = SimParams(
        months = 1,
        self_monthly_yen = 30000,
        invite_per_month = 20,
        child_monthly_yen = 20000,
        grand_monthly_yen = 20000,
        cont_rate = 1,
        grace_months = 2,
        child_activity_rate = 0.9,
        invite_success_rate= 0.05
    )
    results = simulate(params,initial_members())
    # print(results)
    assert results[0]["count_child"] == 1

# 加入したユーザーがgrace_monthsの期間は継続率減少の対象外になっているか
def test_cont_rate_decreases_children():
    # 初期状態子10人の初期メンバーを作る
    members = {"A": {"parent": None, "join_month": 0}},
    for i in range(1,11):
        members = {[f"B{i}"]: {"parent": "A", "join_month": 1}}

    params = SimParams(
        months = 6,
        self_monthly_yen = 30000,
        invite_per_month = 0,
        child_monthly_yen = 20000,
        grand_monthly_yen = 0,
        cont_rate = 0.9439,
        grace_months = 0,
        child_activity_rate = 0.9,
        invite_success_rate = 0.05
    )
    results = simulate(params, initial_members())
    count_child_month = results[0]["count_child"]

    # 月毎のアクティブ子の人数をチェック
    assert results[0]["count_child"] 

    # 子の人数と継続率を計算してcontinuation_rateへ代入
    count_child_month = count_child_month * params.cont_rate
    # continuation_rateが0.9439だったらTrueを返す
    assert count_child_month == 9
    continuation_rate = count_child_month * params.cont_rate
    assert count_child_month == 8
    continuation_rate = count_child_month * params.cont_rate
    assert count_child_month == 8
#  arrange:準備段階, act:実行, assert:挙動確認

# 加入してからcont_rateの継続率が適用されているか
# count_childが0の場合、invites_pool_grandが増えないこと
# 加入した子、孫にidが付与されていること
# 加入した子、孫にparentとjoin_monthが付与されていること
# 現在のアクティブな子の数を数える
# 現在のアクティブな孫の数を数える
# calc_bonusの返り値が正しいか

