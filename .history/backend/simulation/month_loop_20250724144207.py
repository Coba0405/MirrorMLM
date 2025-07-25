import random
from backend.domain.bonus import calc_bonus
from backend.config.members import initial_members
from .population import next_counts, calc_join_and_remainder
from backend.simulation.params import SimParams

def simulate(params: SimParams, members: dict) -> list:
    members = initial_members()
    next_child_id = 1
    next_grand_id = 1
    recodes = []
    count_child = 0 #現在の子の人数
    count_grand = 0 #現在の孫の人数
    invites_pool_child = 0 #これまで勧誘した子の数
    invites_pool_grand = 0 #これまで勧誘した孫の数

    for month in range(1, params.months + 1):
        # 勧誘プールへ追加
        invites_pool_child += params.invite_per_month
        invites_pool_grand += int((params.invite_per_month * 1.5))

        # 新規加入数と余りの計算
        new_child, invites_pool_child = calc_join_and_remainder(invites_pool_child) #population.pyで定義したcalc_join_and_remainder関数を実行←用意しているinvites_pool_childを入れる。左辺のnew_childに商、invite_pool_childに余りを格納
        new_grand, invites_pool_grand = calc_join_and_remainder(invites_pool_grand)

        # 子の新規加入時に動的にmembersに追加
        for _ in range(new_child):
            member_id = f"B{next_child_id}"
            members[member_id] = {"parent": "A", "join_month": month}
            next_child_id += 1

        # 孫の新規加入時に動的にmembersに追加
        for _ in range(new_grand):
            # ランダムで親(B)を選択
            child_ids = [mid for mid, meta in members.items() if meta["parent"] == "A"]
            if not child_ids:
                break
            parent_id = random.choice(child_ids)
            members[f"C{next_grand_id}"] = {
                "parent": parent_id,
                "join_month": month
            }
            next_grand_id += 1

        def is_activate(join_month, current_month, cont_rate, grace_months):
            if current_month - join_month < grace_months:
                return True
            return random.random() < cont_rate

        # 継続率ロジック
        count_child = sum(1 for mid, meta in members.items() if mid.startswith("B") and is_activate(meta["join_month"], month, params.cont_rate, params.grace_months))
        count_grand = sum(1 for mid, meta in members.items() if mid.startswith("C") and is_activate(meta["join_month"], month, params.cont_rate, params.grace_months))
        # count_child = next_counts(count_child, new_child, month, params.cont_rate, params.grace_months)
        # count_grand = next_counts(count_grand, new_grand, month, params.cont_rate, params.grace_months)

        # 購入額の組み立て
        purchases = {"A": params.self_monthly_yen}
        #個別ノードごとに計算
        for mid, meta in members.items():
            if is_activate(meta["join_month"], month, params.cont_rate, params.grace_months):
                if mid.startswith("B"):
                purchases[mid] = params.child_monthly_yen
            elif mid.startswith("C"):
                purchases[mid] = params.grand_monthly_yen

        # ボーナス計算呼び出し 関数を直接呼び出す
        bonus_info = calc_bonus(purchases, members, root_id="A")

        rec = {
            "month": month,
            "child_count": count_child,
            "invites_pool_child": invites_pool_child,
            "grand_count": count_grand,
            "invites_pool_grand": invites_pool_grand,
            "group_pv": bonus_info["A"]["group_pv"],
            "group_bv": bonus_info["A"]["group_bv"],
            "rate": bonus_info["A"]["rate"],
            "bonus": bonus_info["A"]["bonus"],
        }
        # レコード（辞書）を作成し、append
        recodes.append(rec)
    return recodes
