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
  <div class="bg-slate-800 border border-slate-700 rounded-2xl shadow-xl overflow-hidden">
    <div class="px-6 py-4 border-b border-slate-700 flex flex-col sm:flex-row sm:items-center gap-2">
      <h3 class="font-bold text-white">月別詳細</h3>
      <div class="flex items-center gap-4 text-xs text-slate-400 sm:ml-auto">
        <span class="flex items-center gap-1.5">
          <span class="inline-block w-3 h-3 rounded bg-emerald-500/40 border border-emerald-500/30"></span>
          黒字月
        </span>
        <span class="flex items-center gap-1.5">
          <span class="inline-block w-3 h-3 rounded bg-slate-700/80 border border-slate-600"></span>
          赤字月
        </span>
      </div>
    </div>

    <div class="overflow-x-auto">
      <table class="w-full text-sm">
        <thead class="bg-slate-900/80 border-b border-slate-700">
          <tr>
            <th class="px-4 py-3 text-left text-xs font-semibold text-slate-400 uppercase tracking-wider whitespace-nowrap">月</th>
            <th class="px-4 py-3 text-right text-xs font-semibold text-slate-400 uppercase tracking-wider whitespace-nowrap">ボーナス</th>
            <th class="px-4 py-3 text-right text-xs font-semibold text-slate-400 uppercase tracking-wider whitespace-nowrap">純利益/損失</th>
            <th class="px-4 py-3 text-right text-xs font-semibold text-slate-400 uppercase tracking-wider whitespace-nowrap">ダウン人数</th>
            <th class="px-4 py-3 text-right text-xs font-semibold text-slate-400 uppercase tracking-wider whitespace-nowrap">自己購入費</th>
            <th class="px-4 py-3 text-right text-xs font-semibold text-slate-400 uppercase tracking-wider whitespace-nowrap">活動費</th>
            <th class="px-4 py-3 text-right text-xs font-semibold text-slate-400 uppercase tracking-wider whitespace-nowrap">利率</th>
            <th class="px-4 py-3 text-right text-xs font-semibold text-slate-400 uppercase tracking-wider whitespace-nowrap">グループBV</th>
            <th class="px-4 py-3 text-right text-xs font-semibold text-slate-400 uppercase tracking-wider whitespace-nowrap">グループPV</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-slate-700/40">
          <tr
            v-for="row in props.rows"
            :key="row.month"
            class="transition-colors"
            :class="netProfit(row) > 0
              ? 'bg-emerald-500/10 hover:bg-emerald-500/15'
              : 'hover:bg-slate-700/30'"
          >
            <td class="px-4 py-3 font-medium text-slate-300 whitespace-nowrap">{{ row.month }}</td>
            <td class="px-4 py-3 text-right text-white whitespace-nowrap">{{ fmt(row.bonus) }}</td>
            <td
              class="px-4 py-3 text-right font-semibold whitespace-nowrap"
              :class="netProfit(row) > 0 ? 'text-emerald-400' : 'text-rose-400'"
            >
              {{ netProfit(row) > 0 ? '+' : '' }}{{ fmt(netProfit(row)) }}
            </td>
            <td class="px-4 py-3 text-right text-slate-300 whitespace-nowrap">{{ fmt(row.count_child + row.count_grand) }} 人</td>
            <td class="px-4 py-3 text-right text-slate-300 whitespace-nowrap">{{ fmt(row.self_purchase) }}</td>
            <td class="px-4 py-3 text-right text-slate-300 whitespace-nowrap">{{ fmt(row.activity_cost_monthly) }}</td>
            <td class="px-4 py-3 text-right text-slate-300 whitespace-nowrap">{{ fmt(row.rate * 100) }}%</td>
            <td class="px-4 py-3 text-right text-slate-400 text-xs whitespace-nowrap">{{ fmt(row.group_bv) }}</td>
            <td class="px-4 py-3 text-right text-slate-400 text-xs whitespace-nowrap">{{ fmt(row.group_pv) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
</template>
