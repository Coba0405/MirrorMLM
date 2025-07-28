from dataclasses import asdict, is_dataclass
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
        "activity_cost": _dec2float(totals.activity_cost),
        "bonus": _dec2float(totals.bonus),
        "invites": totals.invites,
        "net_profit": _dec2float(totals.net_profit),
    }
    return records, summary
# def _dec2float(obj):
#     if isinstance(obj, Decimal):
#         return float(obj)
#     if is_dataclass(obj):
#         return {k: _dec2float(v) for k, v in asdict(obj).items()}
#     if isinstance(obj, dict):
#         return {k: _dec2float(v) for k, v in obj.items()}
#     return obj

# def calc_totals(months: int, self_yen: int, invite: int, activity_cost: int):
#     params = SimParams(
#         months=months,
#         self_monthly_yen=self_yen,
#         invite_per_month=invite,
#         activity_cost_monthly=activity_cost
#     )

#     # シミュレーション実行
#     records, _, totals = simulate(params)

#     # データクラス → 辞書化 → Decimal→float 変換
#     totals_dict = _dec2float(asdict(totals))

#     one_year = self_yen * 12
#     return totals_dict, one_year

