<template>
  <footer class="border-t border-slate-700/50 bg-slate-900/60 text-slate-400 py-12 px-6 mt-4">
    <div class="max-w-5xl mx-auto space-y-8">

      <!-- 情報グリッド -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <!-- 計算ロジック -->
        <div class="space-y-3">
          <h3 class="text-white font-semibold text-sm uppercase tracking-wider">計算ロジック</h3>
          <ul class="space-y-2.5">
            <li class="flex gap-2.5 text-sm">
              <span class="text-indigo-400 mt-0.5 shrink-0">▸</span>
              <span>ボーナス = グループBV × ボーナス利率 − ダウン会員へのボーナス</span>
            </li>
            <li class="flex gap-2.5 text-sm">
              <span class="text-indigo-400 mt-0.5 shrink-0">▸</span>
              <span>
                ダウン人数の増加率は
                <a href="https://www.iieej.org/public/committees/ssc/confs/ssc3/ssc3-2.pdf" target="_blank" class="text-indigo-400 hover:text-indigo-300 underline underline-offset-2">
                  SSC研究報告書
                </a>
                に基づき5%を前提
              </span>
            </li>
            <li class="flex gap-2.5 text-sm">
              <span class="text-indigo-400 mt-0.5 shrink-0">▸</span>
              <span>一人加入毎にグループPVに360,000PV加算</span>
            </li>
            <li class="flex gap-2.5 text-sm">
              <span class="text-indigo-400 mt-0.5 shrink-0">▸</span>
              <span>加入後2ヶ月は継続率100%、以降は年間30%の退会を想定</span>
            </li>
          </ul>
        </div>

        <!-- 地域別活動費 -->
        <div class="space-y-3">
          <h3 class="text-white font-semibold text-sm uppercase tracking-wider">地域別活動費</h3>
          <p class="text-xs text-slate-500">（勧誘費 + 交通費）× 勧誘人数 + 月間イベント費</p>
          <div class="bg-slate-800 border border-slate-700 rounded-xl p-4 space-y-2.5 text-sm">
            <div class="flex justify-between gap-4">
              <span>🏙️ 都心部</span>
              <span class="text-slate-300 text-xs font-mono">(¥1,200 + ¥500) × n + ¥10,000</span>
            </div>
            <div class="flex justify-between gap-4">
              <span>🏘️ 地方都市</span>
              <span class="text-slate-300 text-xs font-mono">(¥1,000 + ¥300) × n + ¥5,000</span>
            </div>
            <div class="flex justify-between gap-4">
              <span>🌾 地方</span>
              <span class="text-slate-300 text-xs font-mono">(¥900 + ¥200) × n + ¥4,000</span>
            </div>
          </div>
          <p class="text-xs text-slate-500">純利益 = ボーナス − 購入金額 − 活動費</p>
        </div>
      </div>

      <!-- ランダム性 -->
      <div class="bg-slate-800/50 border border-slate-700 rounded-xl p-5 space-y-3">
        <h3 class="text-white font-semibold">本シミュレーションのランダム性について</h3>
        <p class="text-sm text-slate-400">
          MirrorMLMでは、現実のマルチ商法に近い
          <span class="text-white font-medium">"人間の心理状況"や"不確実性"</span>
          を再現するために乱数を使用しています。同じ条件でも結果が多少変動することがあります。
        </p>
        <ul class="space-y-2 text-sm">
          <li>
            <a
              href="https://wayroo.com/the-high-cost-of-low-mlm-representative-retention/?utm_source=chatgpt.com"
              target="_blank"
              class="flex gap-2 text-slate-400 hover:text-indigo-400 transition-colors"
            >
              <span class="text-indigo-500 shrink-0">①</span>
              継続率が段階的に減少し、<span class="text-white font-medium mx-1">1年後に約70%</span>に収束
            </a>
          </li>
          <li>
            <a
              href="https://www.fundera.com/resources/mlm-statistics?utm_source=chatgpt.com"
              target="_blank"
              class="flex gap-2 text-slate-400 hover:text-indigo-400 transition-colors"
            >
              <span class="text-indigo-500 shrink-0">②</span>
              継続ユーザーのうち<span class="text-white font-medium mx-1">積極的に勧誘するのは約40%</span>
            </a>
          </li>
          <li>
            <a
              href="https://www.mlm.com/corporate-feature-busting-mlm-myths/?utm_source=chatgpt.com"
              target="_blank"
              class="flex gap-2 text-slate-400 hover:text-indigo-400 transition-colors"
            >
              <span class="text-indigo-500 shrink-0">③</span>
              積極勧誘ユーザーの月間勧誘数は<span class="text-white font-medium mx-1">0〜3人</span>でランダム決定
            </a>
          </li>
        </ul>
      </div>

      <!-- コピーライト -->
      <div class="border-t border-slate-700/50 pt-6 text-center space-y-1">
        <p class="text-xs text-slate-500">
          このシミュレーターは参考情報であり、実際の報酬・費用とは異なる場合があります。個別の投資判断は自己責任でお願いいたします。
        </p>
        <p class="text-xs text-slate-600">© 2025 MirrorMLM. All rights reserved. Ver. 1.0.1</p>
      </div>

    </div>
  </footer>
</template>
