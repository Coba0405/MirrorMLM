from decimal import Decimal, ROUND_HALF_UP
from backend.domain.constants import PV_PER_YEN, BV_PER_PV, BONUS_TABLE

def rint(x: Decimal) -> int:
    # 四捨五入で整数化
    return int(x.quantize(Decimal("0"), rounding=ROUND_HALF_UP))

def pv_to_rate(pv: int) -> Decimal:
    """グループ PVから還元率を返す"""
    for threshold, rate in BONUS_TABLE:
        if pv >= threshold:
            return rate
    return Decimal("0.0")

def calc_bonus(purchases: dict, members: dict, root_id: str):
    """
    purchases: {"A":50000, "B":30000, "C":20000}
    root_id:   "A" 固定（今回は常にAと明示）

    返り値は root_id だけの dict
    """
    info = {}
    # 1. 個人値(personal)
    for mid, yen in purchases.items():
        pv = PV_PER_YEN * Decimal(yen)
        bv = pv * BV_PER_PV
        info[mid] = {
            "personal_pv": rint(pv),
            "personal_bv": rint(bv),
            "children": []
        }

    # 2. 親子リンク
    for cid, meta in members.items():
        parent = meta.get("parent")
        if parent and cid in info:
            info.setdefault(parent, {"children": [], "personal_pv": 0, "personal_bv": 0})
            info[parent]["children"].append(cid)
            # info.setdefault(parent, {"children": []})
            # info[parent].setdefault("children", []).append(cid)

    # 3. 会員ID(mid)を受取、全groupのPV/BVを計算する再帰関数を定義
    def accum(mid):
        total_pv = info[mid].get("personal_pv", 0) #自分が購入した分だけのPVを取得
        total_bv = info[mid].get("personal_bv", 0) #自分が購入した分だけのBVを取得
        for child in info[mid].get("children", []): #midの直下に登録された子を順番に取得。子がいなければ空リストでスキップ
            cpv, cbv = accum(child) #子会員ごとにaccum(child)を読んで子のグループPV/BVを受け取る
            total_pv += cpv #自分+全ダウンのPV合計まで取得
            total_bv += cbv
        info[mid]["group_pv"] = total_pv #グループPVをinfo[mid]に記録
        info[mid]["group_bv"] = total_bv
        info[mid]["rate"] = pv_to_rate(total_pv) #pv_to_rateを元にグループPVから各会員の還元率を決定
        return total_pv, total_bv #親の呼び出し元に向けてグループPV/BVを返す
    accum(root_id)

    # 4. 差額ボーナス（top-down）
    def diff_bonus(mid):
        subtotal = Decimal(info[mid]["group_bv"]) * info[mid]["rate"] #総ボーナス額を返す（子に奪われる前の額）
        child_sub = Decimal("0") #子会員たちが受け取る総ボーナスの和を格納する変数を初期化
        for child in info[mid].get("children", []):
            child_sub += diff_bonus(child) #子のdiff_bonus(child)を読んで子のボーナス分(subtotal)をchild_subに足す
        info[mid]["bonus"] = rint(subtotal - child_sub) #
        return subtotal

    diff_bonus(root_id)

    # 5. 親だけ返す
    parent_only = {
        root_id: {
            "personal_pv": info[root_id]["personal_pv"],
            "personal_bv": info[root_id]["personal_bv"],
            "group_pv":    info[root_id]["group_pv"],
            "group_bv":    info[root_id]["group_bv"],
            "rate":        float(info[root_id]["rate"]),  # JSON化で小数→float
            "bonus":       info[root_id]["bonus"],
        }
    }
    return parent_only

    # 5. 全員分返す（test_bonus.py親、子、孫を返す時はこっちをアクティブ化）
    # Decimal は JSON 化しづらいので float にしたい項目があれば変換
    # for d in info.values():
    #     if isinstance(d.get("rate"), Decimal):
    #         d["rate"] = float(d["rate"])
    # return info
