<template>
  <div
    class="rounded-xl overflow-hidden"
    style="background-color: var(--bg-card); border: 1px solid var(--border);"
  >
    <!-- ヘッダー -->
    <div
      class="px-6 py-4 flex items-center gap-3"
      style="border-bottom: 1px solid var(--border); background-color: var(--bg-surface);"
    >
      <div class="w-1 h-5 rounded-full" style="background-color: var(--grade-b);"></div>
      <h2 class="text-sm font-bold tracking-widest uppercase" style="color: var(--text-primary);">数値の根拠・前提条件</h2>
    </div>

    <div class="p-6 space-y-6">

      <!-- セクション1: AmwayのBP/PVシステム -->
      <div>
        <h3 class="text-xs font-bold uppercase tracking-widest mb-3 flex items-center gap-2" style="color: var(--grade-b);">
          <span>01</span><span>Amway BP・ボーナス計算</span>
        </h3>
        <div class="space-y-2">
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
            <div class="rounded-lg p-3" style="background-color: var(--bg-surface); border: 1px solid var(--border);">
              <div class="text-xs font-semibold mb-1" style="color: var(--text-primary);">PV換算レート</div>
              <div class="mono text-sm font-bold" style="color: var(--grade-b);">1円 ≈ 0.652 PV</div>
              <div class="text-xs mt-1" style="color: var(--text-muted);">Amway公式の価格体系（約¥1.5345/PV）に基づく。製品小売価格をPVに換算する際に使用。</div>
            </div>
            <div class="rounded-lg p-3" style="background-color: var(--bg-surface); border: 1px solid var(--border);">
              <div class="text-xs font-semibold mb-1" style="color: var(--text-primary);">BV換算レート</div>
              <div class="mono text-sm font-bold" style="color: var(--grade-b);">1 PV = 1.395 BV</div>
              <div class="text-xs mt-1" style="color: var(--text-muted);">Amway JapanのビジネスボリュームはPVの約1.395倍。ボーナス額の算出基礎。</div>
            </div>
          </div>

          <!-- ボーナステーブル -->
          <div class="rounded-lg p-3" style="background-color: var(--bg-surface); border: 1px solid var(--border);">
            <div class="text-xs font-semibold mb-2" style="color: var(--text-primary);">Amway差額ボーナス率テーブル（Amway Japan 公式報酬プラン準拠）</div>
            <div class="overflow-x-auto">
              <table class="w-full text-xs">
                <thead>
                  <tr style="border-bottom: 1px solid var(--border);">
                    <th class="text-left pb-1 pr-4 font-semibold" style="color: var(--text-muted);">グループPV</th>
                    <th class="text-right pb-1 font-semibold" style="color: var(--text-muted);">ボーナス率</th>
                  </tr>
                </thead>
                <tbody class="mono">
                  <tr v-for="row in bonusTable" :key="row.pv" style="border-bottom: 1px solid var(--border);">
                    <td class="py-1 pr-4" style="color: var(--text-primary);">{{ row.pv }}</td>
                    <td class="py-1 text-right font-bold" :style="{ color: row.color }">{{ row.rate }}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          <!-- 加入初月購入 -->
          <div class="rounded-lg p-3" style="background-color: var(--bg-surface); border: 1px solid var(--border);">
            <div class="text-xs font-semibold mb-1" style="color: var(--text-primary);">加入初月の購入額: <span class="mono" style="color: var(--grade-d);">¥560,000</span></div>
            <div class="text-xs" style="color: var(--text-muted);">
              Amwayで360,000PV（21%ボーナス率の下限）を達成するために必要な金額。スターターキットや初期在庫として一括購入するケースを想定。約560,000円 × 0.652 ≒ 360,000PV。
            </div>
          </div>
        </div>
      </div>

      <!-- セクション2: 継続率・退会モデル -->
      <div>
        <h3 class="text-xs font-bold uppercase tracking-widest mb-3 flex items-center gap-2" style="color: var(--grade-c);">
          <span>02</span><span>継続率・退会モデル</span>
        </h3>
        <div class="space-y-2">
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
            <div class="rounded-lg p-3" style="background-color: var(--bg-surface); border: 1px solid var(--border);">
              <div class="text-xs font-semibold mb-1" style="color: var(--text-primary);">月次継続率</div>
              <div class="mono text-sm font-bold" style="color: var(--grade-c);">97.5% / 月</div>
              <div class="text-xs mt-1" style="color: var(--text-muted);">
                0.975¹² ≈ 0.74 → 年間約74%が残存。業界調査「1年後に約70%に収束」と整合。
                <a href="https://wayroo.com/the-high-cost-of-low-mlm-representative-retention/" target="_blank" class="underline underline-offset-2 ml-1" style="color: var(--grade-b);">出典↗</a>
              </div>
            </div>
            <div class="rounded-lg p-3" style="background-color: var(--bg-surface); border: 1px solid var(--border);">
              <div class="text-xs font-semibold mb-1" style="color: var(--text-primary);">入会猶予期間</div>
              <div class="mono text-sm font-bold" style="color: var(--grade-c);">2ヶ月間は退会なし</div>
              <div class="text-xs mt-1" style="color: var(--text-muted);">加入直後は製品購入・勧誘に積極的な傾向。2ヶ月間は離脱確率をゼロとして設定。</div>
            </div>
          </div>
          <div class="rounded-lg p-3" style="background-color: var(--bg-surface); border: 1px solid var(--border);">
            <div class="text-xs font-semibold mb-1" style="color: var(--text-primary);">退会判定ロジック（乱数使用）</div>
            <div class="mono text-xs p-2 rounded my-1" style="background-color: var(--bg-card); color: var(--grade-c);">if random.random() >= 0.975 → 退会</div>
            <div class="text-xs" style="color: var(--text-muted);">毎月各会員に対し乱数（0〜1の一様分布）を生成。0.975未満なら継続、以上なら退会。これにより同じ条件でも毎回微妙に異なる結果となる。</div>
          </div>
        </div>
      </div>

      <!-- セクション3: 勧誘・加入モデル -->
      <div>
        <h3 class="text-xs font-bold uppercase tracking-widest mb-3 flex items-center gap-2" style="color: var(--grade-d);">
          <span>03</span><span>勧誘・加入モデル（乱数）</span>
        </h3>
        <div class="space-y-2">
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
            <div class="rounded-lg p-3" style="background-color: var(--bg-surface); border: 1px solid var(--border);">
              <div class="text-xs font-semibold mb-1" style="color: var(--text-primary);">勧誘成功率</div>
              <div class="mono text-sm font-bold" style="color: var(--grade-d);">1 / 20人 (5%)</div>
              <div class="text-xs mt-1" style="color: var(--text-muted);">
                SSC研究報告書「勧誘20人で1人が加入」に基づく。
                <a href="https://www.iieej.org/public/committees/ssc/confs/ssc3/ssc3-2.pdf" target="_blank" class="underline underline-offset-2 ml-1" style="color: var(--grade-b);">出典↗</a>
              </div>
            </div>
            <div class="rounded-lg p-3" style="background-color: var(--bg-surface); border: 1px solid var(--border);">
              <div class="text-xs font-semibold mb-1" style="color: var(--text-primary);">子のアクティブ率</div>
              <div class="mono text-sm font-bold" style="color: var(--grade-d);">40%（乱数判定）</div>
              <div class="text-xs mt-1" style="color: var(--text-muted);">
                継続会員のうち積極的に勧誘するのは30〜40%。
                <a href="https://www.fundera.com/resources/mlm-statistics" target="_blank" class="underline underline-offset-2 ml-1" style="color: var(--grade-b);">出典↗</a>
              </div>
            </div>
            <div class="rounded-lg p-3" style="background-color: var(--bg-surface); border: 1px solid var(--border);">
              <div class="text-xs font-semibold mb-1" style="color: var(--text-primary);">月間勧誘数（子）</div>
              <div class="mono text-sm font-bold" style="color: var(--grade-d);">0〜3人（乱数）</div>
              <div class="text-xs mt-1" style="color: var(--text-muted);">
                積極ユーザーの実際の月間勧誘数は0〜3人でランダム決定。
                <a href="https://www.mlm.com/corporate-feature-busting-mlm-myths/" target="_blank" class="underline underline-offset-2 ml-1" style="color: var(--grade-b);">出典↗</a>
              </div>
            </div>
          </div>
          <div class="rounded-lg p-3" style="background-color: var(--bg-surface); border: 1px solid var(--border);">
            <div class="text-xs font-semibold mb-1" style="color: var(--text-primary);">月額購入費（子・孫）</div>
            <div class="mono text-sm font-bold" style="color: var(--grade-d);">¥15,000 / 月</div>
            <div class="text-xs mt-1" style="color: var(--text-muted);">Amway ABOの平均的な月次自己購入費。自己消費・サンプル配布を合わせた実態に近い水準として設定。</div>
          </div>
        </div>
      </div>

      <!-- セクション4: 地域別活動費 -->
      <div>
        <h3 class="text-xs font-bold uppercase tracking-widest mb-3 flex items-center gap-2" style="color: var(--grade-f);">
          <span>04</span><span>地域別活動費の内訳</span>
        </h3>
        <div class="rounded-lg overflow-hidden" style="border: 1px solid var(--border);">
          <table class="w-full text-xs">
            <thead style="background-color: var(--bg-surface);">
              <tr>
                <th class="text-left px-4 py-2 font-semibold" style="color: var(--text-muted);">地域</th>
                <th class="text-right px-4 py-2 font-semibold" style="color: var(--text-muted);">勧誘費/人</th>
                <th class="text-right px-4 py-2 font-semibold" style="color: var(--text-muted);">交通費/人</th>
                <th class="text-right px-4 py-2 font-semibold" style="color: var(--text-muted);">イベント費/月</th>
                <th class="text-right px-4 py-2 font-semibold" style="color: var(--text-muted);">合計（n人/月）</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-top: 1px solid var(--border);">
                <td class="px-4 py-2 font-medium" style="color: var(--text-primary);">都心部</td>
                <td class="px-4 py-2 text-right mono" style="color: var(--text-primary);">¥1,200</td>
                <td class="px-4 py-2 text-right mono" style="color: var(--text-primary);">¥500</td>
                <td class="px-4 py-2 text-right mono" style="color: var(--text-primary);">¥10,000</td>
                <td class="px-4 py-2 text-right mono font-semibold" style="color: var(--text-primary);">¥1,700×n + ¥10,000</td>
              </tr>
              <tr style="border-top: 1px solid var(--border);">
                <td class="px-4 py-2 font-medium" style="color: var(--text-primary);">地方都市</td>
                <td class="px-4 py-2 text-right mono" style="color: var(--text-primary);">¥1,000</td>
                <td class="px-4 py-2 text-right mono" style="color: var(--text-primary);">¥300</td>
                <td class="px-4 py-2 text-right mono" style="color: var(--text-primary);">¥5,000</td>
                <td class="px-4 py-2 text-right mono font-semibold" style="color: var(--text-primary);">¥1,300×n + ¥5,000</td>
              </tr>
              <tr style="border-top: 1px solid var(--border);">
                <td class="px-4 py-2 font-medium" style="color: var(--text-primary);">地方</td>
                <td class="px-4 py-2 text-right mono" style="color: var(--text-primary);">¥900</td>
                <td class="px-4 py-2 text-right mono" style="color: var(--text-primary);">¥200</td>
                <td class="px-4 py-2 text-right mono" style="color: var(--text-primary);">¥4,000</td>
                <td class="px-4 py-2 text-right mono font-semibold" style="color: var(--text-primary);">¥1,100×n + ¥4,000</td>
              </tr>
            </tbody>
          </table>
          <div class="px-4 py-2 text-xs" style="background-color: var(--bg-surface); border-top: 1px solid var(--border); color: var(--text-muted);">
            勧誘費：カフェ代・食事代などの接待費用。交通費：1回あたりの移動費の概算。イベント費：セミナー・研修・月例ミーティングへの参加費。
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
const bonusTable = [
  { pv: '1,500,000 PV 以上', rate: '21%', color: 'var(--grade-a)' },
  { pv: '1,000,000 PV 以上', rate: '18%', color: 'var(--grade-b)' },
  { pv: '600,000 PV 以上',   rate: '15%', color: 'var(--grade-b)' },
  { pv: '360,000 PV 以上',   rate: '12%', color: 'var(--grade-c)' },
  { pv: '180,000 PV 以上',   rate: '9%',  color: 'var(--grade-c)' },
  { pv: '90,000 PV 以上',    rate: '6%',  color: 'var(--grade-d)' },
  { pv: '30,000 PV 以上',    rate: '3%',  color: 'var(--grade-d)' },
  { pv: '30,000 PV 未満',    rate: '0%',  color: 'var(--grade-f)' },
];
</script>
