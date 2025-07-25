import random
from backend.domain.bonus import calc_bonus
from backend.config.members import initial_members
from .population import calc_join_and_remainder
from backend.simulation.params import SimParams

def simulate(params: SimParams, members: dict) -> list:
    members = initial_members()
    next_child_id = 1
    next_grand_id = 1
    recodes = []
    count_child = 0 #現在の子の人数
    count_grand = 0 #現在の孫の人数
    invites_pool_child = 0 #親がこれまで勧誘した子の数
    invites_pool_grand = 0 #子がこれまで勧誘した孫の数

    def is_active(join_month, current_month, cont_rate, grace_months):
        # 現在月数から加入月数を差し引いた月数が、残留猶予期間より小さい時
        if current_month - join_month < grace_months:
            return True
        return random.random() < cont_rate

    for month in range(1, params.months + 1):
        # 勧誘プールへ追加
        invites_pool_child += params.invite_per_month
        # 新規加入数(new_child)と余り(invites_pool_child)を代入
        new_child, invites_pool_child = calc_join_and_remainder(invites_pool_child) #population.pyで定義したcalc_join_and_remainder関数を実行←用意しているinvites_pool_childを入れる。左辺のnew_childに商、invite_pool_childに余りを格納

        # その子の新規加入時に動的にmembersに追加
        for _ in range(new_child):
            member_id = f"B{next_child_id}"
            # 加入した子にIDを付与してmembersの辞書に追加
            members[member_id] = {"parent": "A", "join_month": month}
            next_child_id += 1

        active_children = [
            # membersの中からmember_idとmetaでそのidに紐づく情報を順繰りに取得
            mid for mid, meta in members.items()
            # IDが"B"で始まる人に絞る 且つ join_monthから継続率、猶予期間から現在も活動しているかを判定
            if mid.startswith("B") and is_active(meta["join_month"],month, params.cont_rate, params.grace_months)
        ]
        # 実際のアクティブユーザーの活動人数を算出してnum_activate_childrenに代入
        num_active_children = int(len(active_children) * params.child_activity_rate)
        # 実際のアクティブユーザーと勧誘
        child_invites_total = num_active_children * params.invite_per_month
        invites_pool_grand += int(child_invites_total * params.invite_success_rate)

        # 孫の新規加入時に動的にmembersに追加
        new_grand, invites_pool_grand = calc_join_and_remainder(invites_pool_grand)
        for _ in range(new_grand):
            # ランダムで親(B)を選択
            if not active_children:
                break
            parent_id = random.choice(active_children)
            members[f"C{next_grand_id}"] = {
                "parent": parent_id,
                "join_month": month
            }
            next_grand_id += 1


        # 継続率ロジック
        count_child = sum(1 for mid, meta in members.items() if mid.startswith("B") and is_active(meta["join_month"], month, params.cont_rate, params.grace_months))
        count_grand = sum(1 for mid, meta in members.items() if mid.startswith("C") and is_active(meta["join_month"], month, params.cont_rate, params.grace_months))

        # 購入額の組み立て
        purchases = {"A": params.self_monthly_yen}
        #個別ノードごとに計算
        for mid, meta in members.items():
            join_month = meta["join_month"]
            if is_active(join_month, month, params.cont_rate, params.grace_months):
                if mid.startswith("B"):
                    if month == join_month:
                        purchases[mid] = 470000
                    else:
                        purchases[mid] = params.child_monthly_yen
                elif mid.startswith("C"):
                    if month == join_month:
                        purchases[mid] = 470000
                    else:
                        purchases[mid] = params.grand_monthly_yen

        # ボーナス計算呼び出し 関数を直接呼び出す
        bonus_info = calc_bonus(purchases, members, root_id="A")

        rec = {
            "month": month,
            "child_count": count_child,
            "grand_count": count_grand,
            "invites_pool_child": invites_pool_child,
            "invites_pool_grand": invites_pool_grand,
            "child_monthly_yen": params.child_monthly_yen,
            "grand_monthly_yen": params.grand_monthly_yen,
            "group_pv": bonus_info["A"]["group_pv"],
            "group_bv": bonus_info["A"]["group_bv"],
            "rate": bonus_info["A"]["rate"],
            "bonus": bonus_info["A"]["bonus"],
        }
        # レコード（辞書）を作成し、append
        recodes.append(rec)
    return recodes
