from .month_loop import simulate
from .params import SimParams, TotalCost

def calc_totals(months: int, self_yen: int, invite: int, activity_cont: int):
    params = SimParams(
        months =  months,
        self_monthly_yen = self_yen,
        invite_per_month = invite,
        activity_cont_monthly = activity_cont
    )

    # シミュレーションを実行
    records, members, totals = simulate(params)
    # paramsのシミュレーション期間 * 月間製品購入費をかけた値を"total_self_monthly_yen"に代入
    total_self_monthly_yen = totals.self_purchases
    # シミュレーション期間の最初の12ヶ月間 * 月間製品購入費をかけた値を"year_self_monthly_yenに代入
    year_self_monthly_yen = params.self_monthly_yen * 12

    return int(total_self_monthly_yen), int(year_self_monthly_yen)

