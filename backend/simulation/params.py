from dataclasses import dataclass, field
from decimal import Decimal
import random

def _rand_cont() -> int:
    return random.randrange(3_000, 30_000)

@dataclass
class SimParams:
    months: int #シミュレーション期間
    self_monthly_yen: int #自分の月間製品購入費
    invite_per_month: int #月間勧誘人数
    activity_cont_monthly: int = 0
    child_monthly_yen: int = field(default_factory=_rand_cont) #子の月間製品購入費
    grand_monthly_yen: int = field(default_factory=_rand_cont) #孫の月間製品購入費
    cont_rate: float = 0.9439 #ダウン会員継続率
    grace_months: int = 2 #初期会員残留猶予期間
    child_activity_rate: float = 0.7 #勧誘した子のアクティブ率70%
    invite_success_rate: float = 0.05 #勧誘成功率

class TotalCost:
    self_purchases: Decimal = Decimal(0) #自分の製品購入費総額
    activity_cost: Decimal = Decimal(0) #販促費用総額
    bonus: Decimal = Decimal(0) #ボーナス総額
    invites: int = 0 #純利益

    @property
    def net_profit(self) -> Decimal:
        return self.bonus - (self.self_purchases + self.activity_cost)

