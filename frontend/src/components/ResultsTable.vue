<script setup>
const props = defineProps(['rows']);

const fmt = (n) => {
  if (n === undefined || n === null || isNaN(n)) return '0';
  return n.toLocaleString('ja-JP');
};

const netProfit = (row) => row.bonus - row.activity_cost_monthly - row.self_purchase;
</script>

<template>
<div class="w-full">
  <div
    class="rounded-xl overflow-hidden"
    style="background-color: var(--bg-card); border: 1px solid var(--border);"
  >
    <!-- テーブルヘッダー -->
    <div
      class="px-6 py-4 flex flex-col sm:flex-row sm:items-center gap-2"
      style="border-bottom: 1px solid var(--border);"
    >
      <h3 class="font-bold text-sm tracking-wider" style="color: var(--text-primary);">MONTHLY DETAIL</h3>
      <div class="flex items-center gap-4 text-xs sm:ml-auto" style="color: var(--text-muted);">
        <span class="flex items-center gap-1.5">
          <span class="inline-block w-2 h-4 rounded-sm" style="background-color: var(--grade-a); opacity: 0.6;"></span>
          黒字月
        </span>
        <span class="flex items-center gap-1.5">
          <span class="inline-block w-2 h-4 rounded-sm" style="background-color: var(--grade-f); opacity: 0.3;"></span>
          赤字月
        </span>
      </div>
    </div>

    <div class="overflow-x-auto">
      <table class="w-full text-sm">
        <thead style="background-color: var(--bg-surface); border-bottom: 1px solid var(--border);">
          <tr>
            <th class="px-4 py-3 text-left text-xs font-semibold uppercase tracking-widest whitespace-nowrap" style="color: var(--text-muted);">月</th>
            <th class="px-4 py-3 text-right text-xs font-semibold uppercase tracking-widest whitespace-nowrap" style="color: var(--text-muted);">ボーナス</th>
            <th class="px-4 py-3 text-right text-xs font-semibold uppercase tracking-widest whitespace-nowrap" style="color: var(--text-muted);">純損益</th>
            <th class="px-4 py-3 text-right text-xs font-semibold uppercase tracking-widest whitespace-nowrap" style="color: var(--text-muted);">ダウン人数</th>
            <th class="px-4 py-3 text-right text-xs font-semibold uppercase tracking-widest whitespace-nowrap" style="color: var(--text-muted);">自己購入費</th>
            <th class="px-4 py-3 text-right text-xs font-semibold uppercase tracking-widest whitespace-nowrap" style="color: var(--text-muted);">活動費</th>
            <th class="px-4 py-3 text-right text-xs font-semibold uppercase tracking-widest whitespace-nowrap" style="color: var(--text-muted);">利率</th>
            <th class="px-4 py-3 text-right text-xs font-semibold uppercase tracking-widest whitespace-nowrap" style="color: var(--text-muted);">BV</th>
            <th class="px-4 py-3 text-right text-xs font-semibold uppercase tracking-widest whitespace-nowrap" style="color: var(--text-muted);">PV</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="row in props.rows"
            :key="row.month"
            class="transition-colors"
            :style="{
              backgroundColor: netProfit(row) > 0 ? 'rgba(16,185,129,0.05)' : 'transparent',
              borderBottom: '1px solid var(--border)',
            }"
            onmouseover="this.style.backgroundColor = 'rgba(242,242,248,0.03)'"
            onmouseout="this.style.backgroundColor = this.dataset.bg"
          >
            <td
              class="px-4 py-3 mono text-sm whitespace-nowrap"
              :style="{
                color: 'var(--text-primary)',
                borderLeft: `2px solid ${netProfit(row) > 0 ? 'var(--grade-a)' : 'var(--grade-f)'}`,
              }"
            >{{ row.month }}</td>
            <td class="px-4 py-3 text-right mono text-sm whitespace-nowrap" style="color: var(--text-primary);">{{ fmt(row.bonus) }}</td>
            <td
              class="px-4 py-3 text-right mono font-semibold text-sm whitespace-nowrap"
              :style="{ color: netProfit(row) > 0 ? 'var(--grade-a)' : 'var(--grade-f)' }"
            >
              {{ netProfit(row) > 0 ? '+' : '' }}{{ fmt(netProfit(row)) }}
            </td>
            <td class="px-4 py-3 text-right mono text-sm whitespace-nowrap" style="color: var(--text-muted);">{{ fmt(row.count_child + row.count_grand) }} 人</td>
            <td class="px-4 py-3 text-right mono text-sm whitespace-nowrap" style="color: var(--text-muted);">{{ fmt(row.self_purchase) }}</td>
            <td class="px-4 py-3 text-right mono text-sm whitespace-nowrap" style="color: var(--text-muted);">{{ fmt(row.activity_cost_monthly) }}</td>
            <td class="px-4 py-3 text-right mono text-sm whitespace-nowrap" style="color: var(--text-muted);">{{ fmt(row.rate * 100) }}%</td>
            <td class="px-4 py-3 text-right mono text-xs whitespace-nowrap" style="color: var(--text-muted);">{{ fmt(row.group_bv) }}</td>
            <td class="px-4 py-3 text-right mono text-xs whitespace-nowrap" style="color: var(--text-muted);">{{ fmt(row.group_pv) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
</template>
