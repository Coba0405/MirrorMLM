# 差額ボーナス計算モジュール
PV_RATE = 1 / 1.5345    # 円→PV
BV_RATE = 1.395     # PB→BV
# 成績別ボーナス表（PV下限、還元率を大きい順にする
BONUS_TABLE = [
    (1_500_000, 0.21),
    (1_000_000, 0.18),
    (600_000, 0.15),
    (360_000, 0.12),
    (180_000, 0.09),
    (90_000, 0.06),
    (30_000, 0.03),
    (0, 0.00)
]

def pv_to_rate(pv: float) -> float:
    """グループ PVから還元率を返す"""
    for threshold, rate in BONUS_TABLE:
        if pv >= threshold:
            return rate
    return 0.0

def calc_bonus(purchases: dict, members: dict, *, max_depth: int = 2):
# 1. 個人PV/BV 計算
    """購入金額(円)辞書 -> 各人のPV/BV/率/ボーナスを返す"""
    # info = { m: { … } for m, amt in purchases.items() }　内包表記で各購入者ごとにネスト辞書を生成
    # mがID、amtが購入金額
    info = {m: {
        # 自分が購入した金額（円）を PVへ換算
        "personal_pv": round(amt * PV_RATE, 2),
        # 自分が購入した金額（円）を BVへ換算
        "personal_bv": round(amt * PV_RATE * BV_RATE, 2),
        "children": []
    } for m, amt in purchases.items()}
    # cidは子ID、meta はその辞書
    for cid, meta in members.items():
        parent = meta.get("parent")
        # parentが存在し、且つ子(cid)が購入を行った場合処理が走る
        if parent and cid in info:
            # infoに親エントリがなければ空dict作成。親dictに"children"リストがなければ空リストを追加し、それに子IDを追加
            info.setdefault(parent, {}).setdefault("children", []).append(cid)

# 2. グループ集計（post_order）
    def accumulate(mid):
        # info[mid]でmidというキーを持つメンバー情報を取得。info[mid]では辞書内の全てを取得するので["personal_pv"]で取得するものを指定する
        total_pv = info[mid]["personal_pv"]
        total_bv = info[mid]["personal_bv"]
        # その会員(mid)のダウン(children)を順番に処理
        for child in info[mid]["children"]:
            # 子のグループ合計PV/BVを計算して戻り値として受け取る
            cpv, cbv = accumulate(child)
            total_pv += cpv
            total_bv += cbv
        # その会員のグループPV（自分 + 前ダウンのPV合計）を記録
        info[mid]["group_pv"] = round(total_pv, 2)
        info[mid]["group_bv"] = round(total_bv, 2)
        # グループPVに応じた還元率をテーブルから取得
        info[mid]["rate"] = pv_to_rate(total_pv)
        # グループのPV/BVをタプルで親に返す
        return total_pv, total_bv

    # ルート候補を探して再起する
    roots = [m for m, meta in members.items() if meta["parent"] is None]
    # 全てのルートから計算を開始するループ
    for r in roots:
        # infoに購入データが含まれている場合だけ計算する
        if r in info:
            accumulate(r)

# 3. 差額ボーナス計算（トップダウン）
    def diff_bonus(mid):
        my_rate = info[mid]["rate"]
        my_group_bv = info[mid]["group_bv"]
        subtotal = my_group_bv * my_rate
        child_sum = 0
        for child in info[mid]["children"]:
            child_sum += diff_bonus(child)
        info[mid]["bonus"] = round(subtotal - child_sum, 2)
        return subtotal

    for r in roots:
        if r in info:
            diff_bonus(r)

    return info
