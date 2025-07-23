from decimal import Decimal, ROUND_HALF_UP
from params import SimParams, cont_rate, grace_months

def rint(x: float) -> int:
    return int(Decimal(str(x)).quantize(Decimal("0"),rounding=ROUND_HALF_UP))

# 加入ロジック
人口ロジック用モジュールの用意
backend/simulation/population.py に、calc_join_and_remainder(invites_pool) 関数を実装。
単体で動くか、REPL や簡易スクリプトで確かめる。
単体テストを書く
backend/tests/test_population.py を作成。
calc_join_and_remainder(0–19)→(0,余り)、(20→1,0), (45→2,5) などケースを列挙して検証。
月次ループへの組み込み
backend/simulation/month_loop.py のループ冒頭で、
# invites_pool_child を前月から持ち越し
invites_pool_child += params.invite_per_month
new_child, invites_pool_child = calc_join_and_remainder(invites_pool_child)
のように呼び出し、new_child を next_counts に渡す。
シミュレーション結果の確認
POST /api/simulate で JSON が正しく返ってくるか curl やブラウザでチェック。
テスト用 JSON に対して人数が想定どおり増減しているか確認。
UIへの反映

フロント側で「子人数」「孫人数」の表示を追加。

シミュレーション実行ボタンで結果が反映されるか動作確認。

境界・異常系テスト

0人勧誘、100人勧誘などの極端ケースで破綻しないか試す。

grace（2ヶ月100%継続）との組み合わせも確認。
# 離脱ロジック

# month_loop.pyに人数を反映→・api/simulatoでJSON確認

def next_counts(prev_count, joins, month_index, cont_rate, grace_months):
    """
    prev_count: 全月末の人数
    joins: 今月加入人数
    month_index: 1始まり
    全員一律の近似モデル
    """
    # 加入して2ヶ月は100％残留（残留はその人のみが対象）
    if month_index <= grace_months:
        stayed = prev_count + joins
    else:
        stayed =rint((prev_count) * cont_rate) + joins
    return stayed
