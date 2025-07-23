from flask import Flask, jsonify, request
from flask_cors import CORS
from pv_distribution import distribute_pv

app = Flask(__name__)

# Vite の dev サーバ (http://localhost:5173) だけ許可
CORS(
    app,
    resources={r"/api/*": {"origins": "http://localhost:5173"}},
    supports_credentials=True,
)

# ────────── サンプル階層 ──────────
members = {
    "A": {"parent": None},
    "B": {"parent": "Myself"},
    "C": {"parent": "Down "},   # ← ここまでが 2 段階
    "D": {"parent": "Down of down"},   # 3 段目以降はコピー対象外
}

YEN_PER_PV = 1.5345  # 固定換算レート

@app.route("/api/distribute", methods=["POST"])
def distribute():
    data = request.json
    purchaser = data["purchaser"]
    amount_yen = float(data["amount_yen"])
    total_pv = round(amount_yen / YEN_PER_PV, 2)

    result = distribute_pv(purchaser, total_pv, members, max_depth=2)

    return jsonify({
        "purchaser": purchaser,
        "amount_yen": amount_yen,
        "total_pv": total_pv,
        "distribution": result
    })

if __name__ == "__main__":
    app.run(debug=True, port=8000)