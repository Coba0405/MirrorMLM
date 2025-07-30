from backend.simulation.summary import calc_summary

def test_calc_totals():
    records, summary = calc_summary(24, 30000, 0, 0)
    assert summary["total_self_purchases 全期間の自己購入費"] == 24 * 30000
