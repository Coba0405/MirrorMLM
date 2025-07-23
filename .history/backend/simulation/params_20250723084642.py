from dataclasses import dataclass

@dataclass
class Simparams:
    months: int
    self_monthly_yen: int
    invite_per_month: int
    chile_monthly_yen: int = 20000
    
