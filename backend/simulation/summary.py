from decimal import Decimal
from .month_loop import simulate
from .params import SimParams, TotalCost

def _dec2float(x):
    return float(x) if isinstance(x, Decimal) else x

def calc_summary(
        months: int,
        self_monthly_yen: int,
        invite_per_month: int,
        activity_cost_monthly: int = 0,
        **extra_params
):
    totals = TotalCost()
    params = SimParams(
        months=months,
        self_monthly_yen=self_monthly_yen,
        invite_per_month=invite_per_month,
        activity_cost_monthly=activity_cost_monthly,
        **extra_params
    )
    records, _, totals = simulate(params)

    # 年商（年収）目標の判定
    annual_target = params.target_annual_income
    reached_year = None #到達していなければNone
    bonus_sum = 0
    for i, rec in enumerate(records, start=1):
        bonus_sum += Decimal(rec["bonus"])
        if i % 12 == 0:
            year_no = i // 12
            if bonus_sum >= annual_target:
                reached_year = year_no
                break
            bonus_sum = 0

    summary = {
        # records とそろえたキー名
        "total_self_purchases 全期間の自己購入費": _dec2float(totals.self_purchases),
        "total_activity_cost 全期間の活動費": int(totals.activity_cost),
        "invites 加入総数": totals.invites,
        "bonus 全期間のbonus": _dec2float(totals.bonus),
        "net_profit 全期間の純利益・純損失": _dec2float(totals.net_profit),
    }

    last_12 = records[-12:]
    bonus_12 = sum(Decimal(rec["bonus"]) for rec in last_12)
    act_12 = sum(Decimal(rec["activity_cost_monthly"]) for rec in last_12)
    self_12 = sum(Decimal(rec["self_purchase"]) for rec in last_12)
    net_12 = bonus_12 - act_12 - self_12

    summary["last_year_summary"] = {
        "annual_income 最後の1年のbonus総額": float(bonus_12),
        "total_activity_cost 最後の1年の活動費": float(act_12),
        "total_self_purchases 最後の1年の自己購入費": float(self_12),
        "net_profit 最後の1年の純利益・純損失": float(net_12)
    }
    summary["target_annual_income 目標年商"] = annual_target
    summary["target_reached_year 目標年商に到達するまでに要した年数"] = reached_year
    return records, summary
