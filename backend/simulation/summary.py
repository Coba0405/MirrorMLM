from decimal import Decimal, InvalidOperation
from .month_loop import simulate
from .params import SimParams, TotalCost

def _dec2int(x):
    try:
        if x is None:
            return 0
        d = Decimal(x)
        if d.is_nan():
            return 0
        return int(d)
    except (InvalidOperation, TypeError, ValueError):
        return 0

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
    annual_target = params.target_annual_income or Decimal('0')
    reached_year = None #到達していなければNone
    target_year_bonus = 0
    bonus_sum = 0

    for i, rec in enumerate(records, start=1):
        bonus_sum += Decimal(rec["bonus"])
        if i % 12 == 0:
            year_no = i // 12
            if reached_year is None and bonus_sum >= annual_target:
                reached_year = year_no
                target_year_bonus = _dec2int(bonus_sum)
            bonus_sum = Decimal('0')

    summary = {
        # records とそろえたキー名
        "total_self_purchases": _dec2int(totals.self_purchases), #全期間の自己購入費
        "total_activity_cost": _dec2int(totals.activity_cost), #全期間の活動費
        "invites": _dec2int(totals.invites), #加入総数
        "bonus": _dec2int(totals.bonus), #全期間のbonus
        "net_profit": _dec2int(totals.net_profit), #全期間の純利益・純損失
        "target_annual_income": _dec2int(annual_target),
        "target_reached_year": reached_year,
        "target_year_bonus":    target_year_bonus,
    }

    last_12 = records[-12:]
    bonus_12 = sum(Decimal(rec["bonus"]) for rec in last_12)
    act_12 = sum(Decimal(rec["activity_cost_monthly"]) for rec in last_12)
    self_12 = sum(Decimal(rec["self_purchase"]) for rec in last_12)
    net_12 = bonus_12 - act_12 - self_12

    summary["last_year_summary"] = {
        "annual_income": _dec2int(bonus_12), #最後の1年のbonus総額
        "total_activity_cost": _dec2int(act_12), #最後の1年の活動費
        "total_self_purchases": _dec2int(self_12), #最後の1年の自己購入費
        "net_profit": _dec2int(net_12) #最後の1年の純利益・純損失
    }
    # summary["target_annual_income"] = _dec2int(annual_target) #目標年商
    # summary["target_reached_year"] = reached_year #目標年商に到達するまでに要した年数
    # summary["target_year_bonus"] = target_year_bonus
    return records, summary
