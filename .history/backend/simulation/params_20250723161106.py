from dataclasses import dataclass

@dataclass
class SimParams:
    months: int
    self_monthly_yen: int   
    invite_per_month: int
    child_monthly_yen: int = 20000
    grand_monthly_yen: int = 20000
    cont_rate: float = 0.9439
    grace_months: int = 2
