<script setup>
const props = defineProps(['data']);
const fmt = (n) => n.toLocaleString('ja-JP');
const fmtSigned = (n) => (n >= 0 ? '+' : '') + n.toLocaleString('ja-JP');
</script>

<template>
<div class="w-full space-y-4">
  <div class="bg-slate-800 border border-slate-700 rounded-2xl shadow-xl p-6">
    <h2 class="text-xl font-bold text-white mb-5">シミュレーション結果</h2>

    <!-- 目標達成バナー -->
    <div
      class="flex items-start gap-3 p-4 rounded-xl mb-5 border"
      :class="props.data.target_reached_year
        ? 'bg-emerald-500/10 border-emerald-500/30'
        : 'bg-rose-500/10 border-rose-500/30'"
    >
      <span class="text-2xl leading-none mt-0.5">
        {{ props.data.target_reached_year ? '✅' : '❌' }}
      </span>
      <div>
        <p class="font-semibold" :class="props.data.target_reached_year ? 'text-emerald-400' : 'text-rose-400'">
          {{ props.data.target_reached_year
            ? `${props.data.target_reached_year} 年目に目標達成`
            : '活動期間内に目標年商に達しませんでした' }}
        </p>
        <p class="text-slate-400 text-sm mt-1">
          目標年商：<span class="text-white font-semibold">{{ fmt(props.data.target_annual_income) }} 円</span>
        </p>
        <p v-if="props.data.target_reached_year" class="text-slate-400 text-sm">
          達成年のボーナス：<span class="text-white font-semibold">{{ fmt(props.data.target_year_bonus) }} 円</span>
        </p>
      </div>
    </div>

    <!-- サマリーカード -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <!-- 最終年 -->
      <div class="bg-slate-900 border border-slate-700 rounded-xl p-5">
        <h3 class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-4">最終年サマリー</h3>
        <div class="space-y-3">
          <div class="flex justify-between items-center">
            <span class="text-slate-400 text-sm">ボーナス総額</span>
            <span class="font-bold text-white">{{ fmt(props.data.last_year_summary.annual_income) }} 円</span>
          </div>
          <div class="flex justify-between items-center">
            <span class="text-slate-400 text-sm">費用総額</span>
            <span class="font-bold text-rose-400">
              {{ fmt(props.data.last_year_summary.total_activity_cost + props.data.last_year_summary.total_self_purchases) }} 円
            </span>
          </div>
          <div class="border-t border-slate-700 pt-3 flex justify-between items-center">
            <span class="text-slate-300 font-medium text-sm">純利益 / 純損失</span>
            <span
              class="font-bold text-lg"
              :class="props.data.last_year_summary.net_profit >= 0 ? 'text-emerald-400' : 'text-rose-400'"
            >
              {{ fmtSigned(props.data.last_year_summary.net_profit) }} 円
            </span>
          </div>
        </div>
      </div>

      <!-- 全期間 -->
      <div class="bg-slate-900 border border-slate-700 rounded-xl p-5">
        <h3 class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-4">全期間サマリー</h3>
        <div class="space-y-3">
          <div class="flex justify-between items-center">
            <span class="text-slate-400 text-sm">ボーナス総額</span>
            <span class="font-bold text-white">{{ fmt(props.data.bonus) }} 円</span>
          </div>
          <div class="border-t border-slate-700 pt-3 flex justify-between items-center">
            <span class="text-slate-300 font-medium text-sm">純利益 / 純損失</span>
            <span
              class="font-bold text-lg"
              :class="props.data.net_profit >= 0 ? 'text-emerald-400' : 'text-rose-400'"
            >
              {{ fmtSigned(props.data.net_profit) }} 円
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>
