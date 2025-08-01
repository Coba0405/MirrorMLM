import random
from decimal import Decimal
from backend.domain.bonus import calc_bonus
from backend.config.members import initial_members
from .population import calc_join_and_remainder
from .cost import calc_monthly_activity_cost
from backend.simulation.params import SimParams, TotalCost

def simulate(params: SimParams, members: dict | None = None):
    members = initial_members() if members is None else members
    totals = TotalCost()
    next_child_id = 1
    next_grand_id = 1
    records = []
    count_child = 0 #現在の子の人数
    count_grand = 0 #現在の孫の人数
    invites_pool_child = 0 #親がこれまで勧誘した子の数
    invites_pool_grand = 0 #子がこれまで勧誘した孫の数

    active_map = {mid: True for mid in members}
    # メインループ
    for month in range(1, params.months + 1):
        # 累計生存率で指数関数的に継続率を減らす
        for mid, meta in members.items():
            if mid == "A":
                active_map[mid] - True
                continue

            if not active_map.get(mid, True):
                continue

            age = month - meta["join_month"]
            if age <= params.grace_months:
                continue

            if random.random() >= params.cont_rate:
                active_map[mid] = False

        # 勧誘プールへ追加
        invites_pool_child += params.invite_per_month
        # 新規加入数(new_child)と余り(invites_pool_child)を代入
        new_child, invites_pool_child = calc_join_and_remainder(invites_pool_child) #population.pyで定義したcalc_join_and_remainder関数を実行←用意しているinvites_pool_childを入れる。左辺のnew_childに商、invite_pool_childに余りを格納

        # その子の新規加入時に動的にmembersに追加
        for _ in range(new_child):
            mid = f"B{next_child_id}"; next_child_id += 1
            # 加入した子にIDを付与してmembersの辞書に追加
            members[mid] = {"parent": "A", "join_month": month}
            active_map[mid] = True

        active_children = [mid for mid, meta in members.items() if mid.startswith("B") and active_map.get(mid, False)]

        # 実際のアクティブユーザーの活動人数を算出してnum_activate_childrenに代入
        num_active_children = int(len(active_children) * params.child_activity_rate)
        # 実際のアクティブユーザーが勧誘した人数をchild_invites_totalに代入
        child_invites_total = num_active_children * params.invite_per_month
        # 勧誘成功した人をinvites_pool_grandに代入
        invites_pool_grand += int(child_invites_total * params.invite_success_rate)

        # 孫の新規加入時に動的にmembersに追加
        new_grand, invites_pool_grand = calc_join_and_remainder(invites_pool_grand)
        for _ in range(new_grand):
            # ランダムで親(B)を選択
            if not active_children:
                break
            parent_id = random.choice(active_children)
            mid = f"C{next_grand_id}"; next_grand_id += 1
            members[mid] = {"parent": parent_id, "join_month": month}
            active_map[mid] = True

        totals.invites += new_child + new_grand

        # 現在のアクティブな子、孫を数える（退会せず勧誘を継続しているユーザー）
        count_child = sum(1 for mid in members if mid.startswith("B") and active_map[mid])
        count_grand = sum(1 for mid in members if mid.startswith("C") and active_map[mid])

        # 月毎の購入額を設定
        purchases = {"A": params.self_monthly_yen}
        totals.self_purchases += Decimal(params.self_monthly_yen)
        # totals.activity_cost += Decimal(params.activity_cost_monthly)
        for mid, meta in members.items():
            if not active_map[mid]:
                continue
            join_month = meta["join_month"]
            if mid.startswith("B"):
                if month == join_month:
                    # 加入した初月だけ360,000PVになるよう560,000円分購入
                    purchases[mid] = 560000
                else:
                    # 加入月以外はランダムに取得する金額
                    purchases[mid] = params.child_monthly_yen
            elif mid.startswith("C"):
                if month == join_month:
                    purchases[mid] = 560000
                else:
                    purchases[mid] = params.grand_monthly_yen

        # ボーナス計算呼び出し 関数を直接呼び出す
        bonus_info = calc_bonus(purchases, members, root_id="A")
        totals.bonus += Decimal(bonus_info["A"]["bonus"])

        activity_cost_monthly = calc_monthly_activity_cost(params.area, params.invite_per_month)
        totals.activity_cost += Decimal(activity_cost_monthly)

        rec = {
            "month": month,
            "count_child": count_child,
            "count_grand": count_grand,
            "invites_pool_child": invites_pool_child,
            "invites_pool_grand": invites_pool_grand,
            "child_monthly_yen": params.child_monthly_yen,
            "grand_monthly_yen": params.grand_monthly_yen,
            "num_active_children": num_active_children, #ユニットテスト用
            "group_pv": bonus_info["A"]["group_pv"],
            "group_bv": bonus_info["A"]["group_bv"],
            "rate": bonus_info["A"]["rate"],
            "bonus": float(bonus_info["A"]["bonus"]),
            "self_purchase": params.self_monthly_yen,
            # "total_self_purchases": float(totals.self_purchases),
            "activity_cost_monthly": activity_cost_monthly
        }
        # レコード（辞書）を作成し、append
        records.append(rec)
    return records, members, totals