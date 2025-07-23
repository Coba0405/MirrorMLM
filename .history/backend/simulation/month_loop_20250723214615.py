import requests, url
from backend.domain.bonus import calc_bonus
from .population import next_counts, calc_join_and_remainder
from params import SimParams

def simulate(params: SimParams, members: dict) -> list:
    recode = []
    count_child = 0, #現在の子の人数
    count_grand = 0, #現在の孫の人数
    invites_pool_child = 0, #これまで勧誘した子の数
    invites_pool_grand = 0, #これまで勧誘した孫の数

    for month in range(1, params.months + 1):
        # 勧誘プールへ追加
        invites_pool_child += params.invite_per_month
        invites_pool_grand += float((params.invite_per_month * 1.5))

        # 新規加入数と余りの計算
        new_child, invites_pool_child = calc_join_and_remainder(invites_pool_child) #population.pyで定義したcalc_join_and_remainder関数を実行←用意しているinvites_pool_childを入れる。左辺のnew_childに商、invite_pool_childに余りを格納
        new_grand, invites_pool_grand = calc_join_and_remainder(invites_pool_grand)
        # 継続率ロジック
        count_child = next_counts(count_child, new_child, month, params.cont_rate, params.grace_months) # 
        count_grand = next_counts(count_child, new_child, month, params.cont_rate, params.grace_months)
        # new_join, remainder = divmod(invites_pool_child, 20)
        # return new_join, remainder
        # if new_join == 1:
        #     count_child += new_join
        # elif remainder:
        #     None
        # else:
        #     break
        # new_join, remainder = divmod(invites_pool_grand, 20)
        # return new_join, remainder

        # 購入額の組み立て　修正要
        purchases = {"A": params.self_monthly_yen}
        if count_child > 0:
            purchases["B"] = params.child_monthly_yen * count_child
        
        # child_total_yen = count_child * child_monthly_yen
        # grand_total_yen = count_child * grand_monthly_yen

        # PV/BV/bonus API呼び出し
        url = "http://localhost:8000/api/bonus"
        requests.get


        # レコード（辞書）を作成し、append
    recode.append(params)
