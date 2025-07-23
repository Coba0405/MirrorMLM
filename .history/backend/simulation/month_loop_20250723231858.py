import requests
from backend.domain.bonus import calc_bonus
from backend.config.members import initial_members
from .population import next_counts, calc_join_and_remainder
from params import SimParams

def simulate(params: SimParams, members: dict) -> list:
    members = initial_members()
    next_child_id = 1
    next_grand_id = 1
    recodes = []
    count_child = 0 #現在の子の人数
    count_grand = 0 #現在の孫の人数
    invites_pool_child = 0, #これまで勧誘した子の数
    invites_pool_grand = 0, #これまで勧誘した孫の数

    for month in range(1, params.month + 1):
        # 子の新規加入時に動的にmembersに追加
        new_child, invites_pool_child = calc_join_and_remainder(invites_pool_child)
        for _ in range(new_child):
            member_id = f"B{next_child_id}"
            members[member_id] = {"parent": "A", "join_month": month}
            next_child_id += 1
            # 勧誘プールへ追加
            invites_pool_child += params.invite_per_month
            # 新規加入数と余りの計算
            new_child, invites_pool_child = calc_join_and_remainder(invites_pool_child) #population.pyで定義したcalc_join_and_remainder関数を実行←用意しているinvites_pool_childを入れる。左辺のnew_childに商、invite_pool_childに余りを格納
            # 継続率ロジック
            count_child = next_counts(count_child, new_child, month, params.cont_rate, params.grace_months)

        new_grand, invites_pool_grand = calc_join_and_remainder(invites_pool_grand)
        for _ in range(new_grand):
            member_id = f"C{next_grand_id}"
            members[member_id] = {"parent": "B", "join_month": month}
            next_grand_id += 1
            invites_pool_grand += float((params.invite_per_month * 1.5))
            new_grand, invites_pool_grand = calc_join_and_remainder(invites_pool_grand)
            count_grand = next_counts(count_child, new_child, month, params.cont_rate, params.grace_months)



        # 購入額の組み立て　修正要
        purchases = {"A": params.self_monthly_yen}
        if count_child > 0:
            purchases["B"] = params.child_monthly_yen * count_child
        if count_grand > 0:
            purchases["C"] = params.grand_monthly_yen * count_grand

        # ボーナス計算呼び出し 関数を直接呼び出す
        bonus_info = calc_info = calc_bonus(purchases, members, root_id="A")

        # PV/BV/bonus API呼び出し
        url = "http://localhost:8000/api/bonus"
        requests.get

        # レコード（辞書）を作成し、append
        recodes.append(params)
    return recodes
