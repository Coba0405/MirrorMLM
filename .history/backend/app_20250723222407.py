import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from flask import Flask, jsonify, request
from flask_cors import CORS
from decimal import Decimal, ROUND_HALF_UP

from backend.domain.constants import PV_PER_YEN, BV_PER_PV
from backend.domain.distribution import distribute_pv
from backend.domain.bonus import calc_bonus
from backend.simulation.month_loop import simulate
from backend.simulation.params import SimParams

# from domain.constants     import PV_PER_YEN, BV_PER_PV
# from domain.distribution  import distribute_pv
# from domain.bonus         import calc_bonus
# from simulation.month_loop import simulate
# from simulation.params     import SimParams

app = Flask(__name__)

# Vite の dev サーバ (http://localhost:5173) だけ許可
CORS(
    app,
    resources={r"/api/*": {"origins": "http://localhost:5173"}},
    supports_credentials=True,
)

# ────────── 階層 ──────────
members = {
    
}

@app.route("/api/bonus", methods=["POST"])
def bonus():
    data = request.json
    purchases = data["purchases"]
    result = calc_bonus(purchases, members, root_id="A")
    return jsonify(result)

@app.route("/api/distribute", methods=["POST"])
def distribute():
    data = request.json
    purchaser = data["purchaser"]
    amount_yen = float(data["amount_yen"])
    total_pv = int(amount_yen * PV_PER_YEN)
    total_bv = int(Decimal(total_pv) * BV_PER_PV)

    result = distribute_pv(purchaser, total_pv, members, max_depth=2)

    return jsonify({
        "purchaser": purchaser,
        "amount_yen": amount_yen,
        "total_pv": total_pv,
        "total_bv": total_bv,
        "distribution": result
    })

@app.route("/api/simulate", methods=["POST"])
def run_sim():
    p = request.json
    params = SimParams(**p)
    recs = simulate(params, members)
    return jsonify(recs)

if __name__ == "__main__":
    app.run(debug=True, port=8000)