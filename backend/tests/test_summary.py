from backend.simulation.summary import calc_totals

def test_calc_totals():
    total_all, total_1year = calc_totals(24, 30000, 8, 0)
    assert total_all == 24 * 30000
    assert total_1year == 12 * 30000