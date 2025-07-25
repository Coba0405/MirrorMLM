from dataclasses import dataclass

@dataclass
class SimParams:
    months: int #加入何ヶ月目か
    self_monthly_yen: int #自分の月間製品購入費
    invite_per_month: int #月間勧誘人数
    child_monthly_yen: int = 20000 #子の月間製品購入費
    grand_monthly_yen: int = 20000 #孫の月間製品購入費
    cont_rate: float = 0.9439 #ダウン会員継続率
    grace_months: int = 2 #初期会員残留猶予期間
    child_activity_rate: float = 0.3 
