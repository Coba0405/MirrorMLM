from dataclasses import dataclass, field
from decimal import Decimal

@dataclass
class SimParams:
    months: int #シミュレーション期間
    self_monthly_yen: int #自分の月間製品購入費
    invite_per_month: int #月間勧誘人数
    activity_cost_monthly: int #月間勧誘費
    target_annual_income: int = 0
    child_monthly_yen: int = 17000 #子の月間製品購入費
    grand_monthly_yen: int = 17000
    cont_rate: float = 0.9439 #ダウン会員(子)継続率
    grace_months: int = 2 #初期会員残留猶予期間
    child_activity_rate: float = 0.7 #勧誘した子のアクティブ率70%
    invite_success_rate: float = 0.05 #勧誘成功率
    area: str = "city_center"

@dataclass
class TotalCost:
    self_purchases: Decimal = field(default_factory=lambda: Decimal(0)) #自分の製品購入費総額
    activity_cost: Decimal = field(default_factory=lambda: Decimal(0)) #販促費用全期間総額
    bonus: Decimal = field(default_factory=lambda: Decimal(0)) #ボーナス総額
    invites: int = 0 #累計加入人数

    # 純利益 or 純損失
    @property
    def net_profit(self) -> Decimal:
        return self.bonus - (self.self_purchases + self.activity_cost)

