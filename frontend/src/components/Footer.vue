<template>
  <footer class=" text-gray-900 py-12 px-6">
    <div class="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-10 shadow-md">

      <!-- 左カラム：説明 -->
      <div class="space-y-6 text-left">
        <p class="text-sm leading-relaxed text-gray-800 border-l-4 border-blue-400 pl-4">
          ボーナス金額は<br>「グループBV × ボーナス利率 − ダウン会員へのボーナス」で算出。
        </p>
        <p class="text-sm leading-relaxed text-gray-800 border-l-4 border-blue-400 pl-4">
          ダウン人数の増加率は
          <a
            href="https://www.iieej.org/public/committees/ssc/confs/ssc3/ssc3-2.pdf"
            target="_blank"
            class="text-blue-400 hover:underline"
          >
            SSC研究報告書
          </a>
          に基づき、5%を前提とし算出。
        </p>
        <p class="text-sm leading-relaxed text-gray-800 border-l-4 border-blue-400 pl-4">
          一人加入毎にグループPVに360,000PVが加算。
        </p>
        <p class="text-sm leading-relaxed text-gray-800 border-l-4 border-blue-400 pl-4">
          加入後2ヶ月は継続率100%、以降は年間30%の退会を想定。
        </p>
      </div>

      <!-- 右カラム：費用・注意 -->
      <div class="space-y-6 text-left">
        <div class="text-sm text-gray-800 space-y-2 border-l-4 border-blue-400 pl-4">
          <span>活動費：地域ごとに設定</span>
          <p>（一人当たりの勧誘費 + 一人当たりの交通費）× 勧誘人数月間のイベント費</p>
          <ul class="list-disc list-inside">
            <li>都心部：(¥1,200 + ¥500) × 勧誘人数 + ¥10,000</li>
            <li>地方都市：(¥1,000 + ¥300) × 勧誘人数 + ¥5,000</li>
            <li>地方：(¥900 + ¥200) × 勧誘人数 + ¥4,000</li>
          </ul>
        </div>

        <div class="text-sm text-gray-800 border-l-4 border-blue-400 pl-4">
          純利益 = ボーナス − 購入金額 − 活動費
          <br /> ※ 青背景の行が「純利益あり」の月です。
        </div>
      </div>
    </div>

    <div class="max-w-6xl mx-auto grid grid-cols-1 gap-1 mt-3 shadow-md">
      <div>
        <h2 class="text-lg font-semibold text-gray-900 mb-2">
          本シミュレーションのランダム性について
        </h2>
        <p class="text-sm leading-relaxed text-gray-700">
          MirrorMLMでは、現実のマルチ商法に近い
          <span class="font-medium">“人間の心理状況”や“不確実性”</span>
          を再現するために、一部の項目に乱数を使用しています。
          <br />
          そのため、同じ条件であってもシミュレーション結果が多少変動することがあります。
        </p>
      </div>

      <!-- ランダム性の詳細リスト -->
      <div class="bg-white p-4 rounded-md border-gray-200">
        <h3 class="text-sm font-semibold text-gray-800 mb-2">乱数が使われている箇所（出典元リンク）</h3>
        <ul class="list-disc list-inside text-sm space-y-2 text-gray-700">
          <li>
            <a href="https://wayroo.com/the-high-cost-of-low-mlm-representative-retention/?utm_source=chatgpt.com"
              target="_blank"
              class="hover:underline"
            >
              加入後、ユーザーの継続率が段階的に減少し、
              <span class="font-semibold">1年後に約70％</span>
              に収束するように調整しています（例：100% → 97.5% → 95.0% → …）。
            </a>
          </li>
          <li>
            <a href="https://www.fundera.com/resources/mlm-statistics?utm_source=chatgpt.com"
              target="_blank"
              class="hover:underline"
            >
              継続しているユーザーのうち、
              <span class="font-semibold">積極的に勧誘活動を行うのは約40％</span>
              という想定でランダム化しています。
            </a>
          </li>
          <li>
            <a href="https://www.mlm.com/corporate-feature-busting-mlm-myths/?utm_source=chatgpt.com"
              target="_blank"
              class="hover:underline"
            >
              積極勧誘ユーザーが1ヶ月間に勧誘する人数は、
              <span class="font-semibold">0〜3人の範囲</span>
              でランダムに決定されます。
            </a>
          </li>
        </ul>
      </div>
    </div>

    <!-- コピーライト -->
    <div class="mt-12 text-center text-xs text-gray-500 border-t border-gray-700 pt-4">
      <p class="text-xs text-gray-500 pt-4">
        このシミュレーターは参考情報であり、実際の報酬・費用とは異なる場合があります。個別の投資判断は自己責任でお願いいたします。
      </p>
      <span>© 2025 MirrorMLM. All rights reserved.</span><br>
      <span class="mr-3">Ver. 1.0.1</span>
    </div>
  </footer>
</template>