from backend.bonus_calc import calc_bonus
from .population import next_counts, calc_joins

def simulate(params: "SimParams", members_tamplate):
    """
    members_template: {"A":{"parent:None"},"B":{"parent:"A"},"C":{"parent":"B"}}
    戻り値: 月次レコードのリスト
    """
    records = []
    # 人数初期化
    count_child = 0
    count_grand = 0
    cum_invited_self = 0 #自分は固定で1
    cum_invited_child = 0
    cum_invited_grand = 0
    joined_self = 0
    joined_child = 0
    joined_grand = 0

    for m in range(1, params.months + 1):
        # 勧誘人数
        cum_invited_self += params.invite_per_month
        cum_invited_child += params.invite_per_month
        cum_invited_grand += params.invite_per_month

        # 加入人数
        new_child = cals_joins(cum_invited_child, joined_child)
        new_grand = cals_joins(cum_invited_grand, joined_grand)

        # 人数更新
        count_child = next_counts(count_child, new_child, m, params.cont_rate, params.grace_months)
        joined_child += new_child

        count_grand = next_counts(count_child, new_child, m, params.cont_rate, params.grace_months)
        joined_grand += new_grand

        # 今月の購入額
        purchases = {"A": params.self_monthly_yen}
        # 子と孫は平均購入金額×人数
        if count_child > 0:
            purchases["B"] = params.child_monthly_yen * count_child
        if count_grand > 0:
            purchases["C"] = params.grand_monthly_yen * count_grand

        # ボーナス（親だけ返す）
        bonus_info = calc_bonus(purchases, members_template, root_id="A")
        # レコード保存
        records.append({
            "month": m,
            "child_count": count_child,
            "grand_count": count_grand,
            "group_pv": bonus_info["A"]["group_pv"],
            "group_bv": bonus_info["A"]["group_bv"],
            "rate": bonus_info["A"]["rate"]
            ""
        })
