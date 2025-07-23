from flask import Flask, jsonify, request
from flask_cors import CORS
from decimal import Decimal, RO
from backend.domain.constants import PV_PER_YEN
from backend.domain.distribution import distribute_pv
from backend.domain.bonus import calc_bonus
from backend.simulation.month_loop import simulate
from backend.simulation.params import SimParams

app = Flask(__name__)

# Vite の dev サーバ (http://localhost:5173) だけ許可
CORS(
    app,
    resources={r"/api/*": {"origins": "http://localhost:5173"}},
    supports_credentials=True,
)

# ────────── 階層 ──────────
members = {
    "A": {"parent": None},
    "B": {"parent": "A"},
    "C": {"parent": "B"},
}

@app.route("/api/bonus", methods=["POST"])
def bonus():
    data = request.json
    purchases = data["purchases"]
    result = calc_bonus(purchases, members, root_id="A")
    # result = calc_bonus(purchases, members)
    return jsonify(result)

@app.route("/api/distribute", methods=["POST"])
def distribute():
    data = request.json
    purchaser = data["purchaser"]
    amount_yen = float(data["amount_yen"])
    total_pv = float(amount_yen / PV_PER_YEN)

    result = distribute_pv(purchaser, total_pv, members, max_depth=2)

    return jsonify({
        "purchaser": purchaser,
        "amount_yen": amount_yen,
        "total_pv": total_pv,
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