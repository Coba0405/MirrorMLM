<template>
  <div>
    <header></header>
    <body>
      <div>
        <div>
          <span class="text-gray-900">
            ボーナス金額はグループBV × ボーナス利率で算出された金額からダウンのディストリビューションを差し引いた金額
          </span>
        </div>

        <div>
          <span class="text-gray-900">
            ダウン人数の増加数計算は
            <a href="https://www.iieej.org/public/committees/ssc/confs/ssc3/ssc3-2.pdf?utm_source=chatgpt.com">勧誘限界説による集団内マルチ商法拡散のシミュレーション </a>
            を参照<br>
            無作為な声かけ（友人・知人など）:約1 % <br>
            ターゲット絞り込みあり（興味ある層）:約2~5 % <br>
            有料リード購入など興味前提あり :約8~15 % <br>
            上記調査結果から勧誘からの勧誘成功率を5％として増加率を算出
          </span>
        </div>

        <div>
          <span class="text-gray-900">
            ダウンの継続率<br>
            年間で30%のダウンメンバーの退会を想定（加入後2ヶ月は継続率100％）
          </span>
        </div>

        <div>
          <p class="text-gray-900">活動費（勧誘費用、交通費、イベント参加費）</p>
          <p class="text-gray-900">勧誘費用（1人当たり）: 都心部:1,200円, 地方都市:1,000円, 地方:900円</p>
          <p class="text-gray-900">交通費（1人当たり）: 都心部:500円, 地方都市:300円, 地方:200円</p>
          <p class="text-gray-900">イベント参加費(1ヶ月当たり): 都心部:10,000円, 地方都市:5,000円, 地方:4,000円</p>
        </div>

        <div>
          <span class="text-gray-900">
            純利益/純損失はボーナスから月間購入金額と勧誘活動費を差し引いた差額となる<br>
            純利益となった月は青い列で表示される
          </span>
        </div>

        <div>
          <span class="text-gray-900">
            計算詳細や端数処理は各金融機関によって異なる場合があります。<br>
            ※計算結果や情報等に関して当サイトは一切責任を負いません。また個別相談は一切対応しません。
          </span>
        </div>
      </div>
    </body>
    <footer class="text-center py-4 text-gray-500">
      © 2025 MirrorMLM
    </footer>
  </div>
</template>