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


    summary = {
        # records とそろえたキー名
        "total_self_purchases": _dec2float(totals.self_purchases),
        "total_activity_cost": int(totals.activity_cost),
        "invites": totals.invites,
        "bonus": _dec2float(totals.bonus),
        "net_profit": _dec2float(totals.net_profit),
    }

    last_12 = records[-12:]
    bonus_12 = sum(Decimal(rec["bonus"]) for rec in last_12)
    act_12 = sum(Decimal(rec["activity_cost_monthly"]) for rec in last_12)
    self_12 = sum(Decimal(rec["self_purchase"]) for rec in last_12)
    net_12 = bonus_12 - act_12 - self_12

    summary["last_year_summary"] = {
        "bonus": float(bonus_12),
        "total_activity_cost": float(act_12),
        "total_self_purchases": float(self_12),
        "net_profit": float(net_12)
    }
    return records, summary
