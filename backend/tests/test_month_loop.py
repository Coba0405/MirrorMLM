import sys, os
sys.path.append(os.getcwd())
from backend.simulation.month_loop import simulate
from backend.config.members import initial_members
from backend.domain.bonus import calc_bonus
from backend.simulation.params import SimParams

# 1.メンバー初期化が正しく行われているか
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
        invite_success_rate= 0.05,
        activity_cost_monthly = 10000
    )
    result, _, _ = simulate(params,initial_members())
    # print(result)
    assert result[0]["count_child"] == 0

# 2.20人勧誘した時にcount_childに+1されるか
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
        invite_success_rate= 0.05,
        activity_cost_monthly = 10000
    )
    records, _, _ = simulate(params,initial_members())
    # print(results)
    assert records[0]["count_child"] == 1

# 3. 加入してからcont_rateの継続率が適用されているか
def test_cont_rate_decreases_children():
    # 初期状態子10人の初期メンバーを作る
    members = {"A": {"parent": None, "join_month": 0}}
    for i in range(1,11):
        members[f"B{i}"] = {"parent": "A", "join_month": 1}

    params = SimParams(
        months = 3,
        self_monthly_yen = 30000,
        invite_per_month = 0,
        child_monthly_yen = 20000,
        grand_monthly_yen = 0,
        cont_rate = 0.9439,
        grace_months = 0,
        child_activity_rate = 0.9,
        invite_success_rate = 0.05,
        activity_cost_monthly = 10000
    )
    records, _, _ = simulate(params, initial_members())

    # 月毎のアクティブ子の人数をチェック
    assert records[0]["count_child"] <= 10
    assert records[1]["count_child"] <= records[0]["count_child"]
    assert records[2]["count_child"] <= records[1]["count_child"]

#  arrange:準備段階, act:実行, assert:挙動確認

# 4. 加入したユーザーがgrace_monthsの期間は継続率減少の対象外になっているか
def test_grace_months_not_cont_rate():
    params = SimParams(
        months = 4,
        self_monthly_yen = 10000,
        invite_per_month = 20,
        child_monthly_yen = 10000,
        grand_monthly_yen = 10000,
        cont_rate = 0,
        grace_months = 2,
        child_activity_rate = 1,
        invite_success_rate = 0.05,
        activity_cost_monthly = 10000
    )
    records, _, _ = simulate(params, initial_members())

    assert records[0]["count_child"] == 1 # B1加入
    assert records[1]["count_child"] == 2 # B2加入 B1猶予期間1ヶ月目
    assert records[2]["count_child"] == 3 # B3加入 B1猶予期間2ヶ月目、B2猶予期間1ヶ月目
    assert records[3]["count_child"] == 3 # B4加入 B1脱落、B2猶予期間2ヶ月目

# 5. count_childが0の場合、invites_pool_grandが増えないこと
def test_no_grand_without_children():
    params = SimParams(
        months = 2,
        self_monthly_yen = 10000,
        invite_per_month = 0,
        child_monthly_yen = 10000,
        grand_monthly_yen = 10000,
        cont_rate = 1,
        grace_months = 2,
        child_activity_rate = 1,
        invite_success_rate = 0.05,
        activity_cost_monthly = 10000
    )
    records, _, _ = simulate(params, initial_members())

    assert records[0]["count_child"] == 0
    assert records[0]["invites_pool_grand"] == 0
    assert records[1]["count_child"] == 0
    assert records[1]["invites_pool_grand"] == 0

# 6. count_childが1の場合、invites_pool_grandが増えること
def test_grand_without_children():
    params = SimParams(
        months = 3,
        self_monthly_yen = 10000,
        invite_per_month = 10,
        child_monthly_yen = 10000,
        grand_monthly_yen = 10000,
        cont_rate = 1,
        grace_months = 0,
        child_activity_rate = 1,
        invite_success_rate = 1,
        activity_cost_monthly = 10000
    )
    records, _, _ = simulate(params, initial_members())

    assert records[0]["count_child"] == 0
    # assert records[0]["count_grand"] == 0
    # assert records[0]["invites_pool_child"] == 10
    assert records[0]["invites_pool_grand"] == 0
    assert records[1]["count_child"] == 1
    # assert records[1]["count_grand"] == 0
    assert records[1]["invites_pool_grand"] == 10
    # print(records[1]["invites_pool_grand"])

# 7. 加入した子にidが付与されていること
def test_child_created_id():
    params = SimParams(
        months = 2,
        self_monthly_yen = 10000,
        invite_per_month = 20,
        child_monthly_yen = 10000,
        grand_monthly_yen = 10000,
        cont_rate = 1,
        grace_months = 0,
        child_activity_rate = 1,
        invite_success_rate = 1,
        activity_cost_monthly = 10000
    )

    _, members, _ = simulate(params, initial_members())
    child_ids = []
    for mid in members:
        if mid.startswith("B"):
            child_ids.append(mid)
    assert len(child_ids) > 0
    assert "B1" in child_ids
    assert "B2" in child_ids
    assert members["B1"]["parent"] == "A"
    assert members["B2"]["parent"] == "A"
    # print(f"{child_ids}")

# 8. 加入した孫にidが付与されていること
def test_grand_creat_id():
    params = SimParams(
        months = 3,
        self_monthly_yen = 10000,
        invite_per_month = 20,
        child_monthly_yen = 10000,
        grand_monthly_yen = 10000,
        cont_rate = 1,
        grace_months = 0,
        child_activity_rate = 1,
        invite_success_rate = 1,
        activity_cost_monthly = 10000
    )

    _, members, _ = simulate(params, initial_members())
    grand_ids = []
    for mid in members:
        if mid.startswith("C"):
            grand_ids.append(mid)

    assert len(grand_ids) > 0
    assert "C1" in grand_ids
    assert "C2" in grand_ids
    assert members["C1"]["parent"] == "B1" or "B2"
    assert members["C2"]["parent"] == "B1" or "B2"
    # print(members["C1"]["parent"])
    # print(members["C2"]["parent"])
    # print(grand_ids["parent"])

# 9. 加入した子、孫にparentとjoin_monthが付与されていること
def test_retention_parent_and_join_month():
    params = SimParams(
        months = 3,
        self_monthly_yen = 10000,
        invite_per_month = 20,
        child_monthly_yen = 10000,
        grand_monthly_yen = 10000,
        cont_rate = 1,
        grace_months = 0,
        child_activity_rate = 1,
        invite_success_rate = 0,
        activity_cost_monthly = 10000
    )
    _, members, _ = simulate(params, initial_members())

    for mid, meta in members.items():
        if mid.startswith("B") or mid.startswith("C"):
            assert "parent" in meta, f"{mid} にparentがありません"
            assert "join_month" in meta, f"{mid} に join_month がありません"

# 10. 現在の継続している子のうちアクティブな子の数を数える
def test_is_active_user():
    params = SimParams(
        months = 3,
        self_monthly_yen = 10000,
        invite_per_month = 40,
        child_monthly_yen = 10000,
        grand_monthly_yen = 10000,
        cont_rate = 1,
        grace_months = 0,
        child_activity_rate = 0.5,
        invite_success_rate = 0.05,
        activity_cost_monthly = 10000
    )
    records, _ , _= simulate(params, initial_members())

    assert records[0]["num_active_children"] == 1
    assert records[1]["num_active_children"] == 2
