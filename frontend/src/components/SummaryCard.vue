<script setup>
import { computed } from 'vue';

const props = defineProps(['data', 'params']);

const fmt = (n) => n.toLocaleString('ja-JP');
const fmtSigned = (n) => (n >= 0 ? '+' : '') + n.toLocaleString('ja-JP');

// 収益性グレード — 純損失率ベース
function profitGrade(summary) {
  const cost = summary.total_self_purchases + summary.total_activity_cost;
  if (cost === 0) return { grade: 'N/A', bars: 0, label: '計測不能' };
  const ratio = summary.net_profit / cost;
  if (ratio >= 0)    return { grade: 'B', bars: 4, label: `+${Math.round(ratio * 100)}%` };
  if (ratio >= -0.3) return { grade: 'D', bars: 2, label: `${Math.round(ratio * 100)}%` };
  return               { grade: 'F', bars: 1, label: `${Math.round(ratio * 100)}%` };
}

// 継続可能性グレード — 目標達成有無ベース
function sustainGrade(summary) {
  if (summary.target_reached_year) return { grade: 'C', bars: 3, label: `${summary.target_reached_year}年目達成` };
  return { grade: 'F', bars: 1, label: '未達成' };
}

// 時間単価グレード — 1人勧誘2時間前提
function timeValueGrade(summary, params) {
  if (!params) return { grade: 'N/A', bars: 0, label: '計測不能' };
  const totalHours = params.months * params.invite_per_month * 2;
  if (totalHours === 0) return { grade: 'N/A', bars: 0, label: '計測不能' };
  const hourlyWage = summary.net_profit / totalHours;
  if (hourlyWage >= 1100) return { grade: 'B', bars: 4, label: `¥${Math.round(hourlyWage)}/h` };
  if (hourlyWage >= 0)    return { grade: 'D', bars: 2, label: `¥${Math.round(hourlyWage)}/h` };
  return { grade: 'F', bars: 1, label: `¥${Math.round(hourlyWage)}/h` };
}

// 勧誘1人あたり純損益グレード
function lossPerRecruitGrade(summary) {
  if (!summary.invites || summary.invites === 0)
    return { grade: 'F', bars: 1, label: '勧誘なし' };
  const lossPerPerson = Math.round(summary.net_profit / summary.invites);
  if (lossPerPerson >= 0)      return { grade: 'B', bars: 4, label: `+¥${lossPerPerson}/人` };
  if (lossPerPerson >= -10000) return { grade: 'D', bars: 2, label: `¥${lossPerPerson.toLocaleString('ja-JP')}/人` };
  return { grade: 'F', bars: 1, label: `¥${lossPerPerson.toLocaleString('ja-JP')}/人` };
}

// 総合評定 — 最悪グレードを採用
function calcOverallGrade(...grades) {
  const order = ['F', 'D', 'C', 'B', 'A'];
  return grades.filter(g => g !== 'N/A')
    .reduce((worst, g) => order.indexOf(g) < order.indexOf(worst) ? g : worst, 'A');
}

// グレードカラー
function gradeColor(grade) {
  const map = {
    'A': 'var(--grade-a)',
    'B': 'var(--grade-b)',
    'C': 'var(--grade-c)',
    'D': 'var(--grade-d)',
    'F': 'var(--grade-f)',
    'N/A': 'var(--text-muted)',
  };
  return map[grade] || 'var(--text-muted)';
}

const grades = computed(() => {
  if (!props.data) return null;
  const profit   = profitGrade(props.data);
  const sustain  = sustainGrade(props.data);
  const timeVal  = timeValueGrade(props.data, props.params);
  const perRecruit = lossPerRecruitGrade(props.data);
  const overall  = calcOverallGrade(profit.grade, sustain.grade, timeVal.grade, perRecruit.grade);
  return { profit, sustain, timeVal, perRecruit, overall };
});
</script>

<template>
<div class="w-full space-y-4" v-if="props.data">

  <!-- REPORT CARD メイン -->
  <div
    class="rounded-xl overflow-hidden"
    style="background-color: var(--bg-card); border: 1px solid var(--border);"
  >
    <!-- カードヘッダー -->
    <div
      class="px-6 py-4 flex justify-between items-center"
      style="border-bottom: 1px solid var(--border);"
    >
      <div>
        <span class="grade-text text-lg tracking-widest" style="color: var(--text-muted);">REPORT CARD</span>
      </div>
      <div class="text-sm font-medium" style="color: var(--text-muted);">シミュレーション結果</div>
    </div>

    <div class="p-6 space-y-6">
      <!-- グレード評価リスト -->
      <div class="space-y-3">

        <!-- 収益性 -->
        <div class="flex items-center gap-4">
          <span class="text-sm w-28 shrink-0" style="color: var(--text-muted);">収益性</span>
          <div class="flex gap-1 flex-1">
            <span
              v-for="i in 6"
              :key="i"
              class="h-2 flex-1 rounded-sm"
              :style="{
                backgroundColor: i <= grades.profit.bars ? gradeColor(grades.profit.grade) : 'var(--border)'
              }"
            ></span>
          </div>
          <span class="text-xs mono w-20 text-right" style="color: var(--text-muted);">{{ grades.profit.label }}</span>
          <span
            class="grade-text text-2xl w-8 text-center"
            :style="{ color: gradeColor(grades.profit.grade) }"
          >{{ grades.profit.grade }}</span>
        </div>

        <!-- 継続可能性 -->
        <div class="flex items-center gap-4">
          <span class="text-sm w-28 shrink-0" style="color: var(--text-muted);">継続可能性</span>
          <div class="flex gap-1 flex-1">
            <span
              v-for="i in 6"
              :key="i"
              class="h-2 flex-1 rounded-sm"
              :style="{
                backgroundColor: i <= grades.sustain.bars ? gradeColor(grades.sustain.grade) : 'var(--border)'
              }"
            ></span>
          </div>
          <span class="text-xs mono w-20 text-right" style="color: var(--text-muted);">{{ grades.sustain.label }}</span>
          <span
            class="grade-text text-2xl w-8 text-center"
            :style="{ color: gradeColor(grades.sustain.grade) }"
          >{{ grades.sustain.grade }}</span>
        </div>

        <!-- 時間単価 -->
        <div class="flex items-center gap-4">
          <span class="text-sm w-28 shrink-0" style="color: var(--text-muted);">時間単価</span>
          <div class="flex gap-1 flex-1">
            <span
              v-for="i in 6"
              :key="i"
              class="h-2 flex-1 rounded-sm"
              :style="{
                backgroundColor: i <= grades.timeVal.bars ? gradeColor(grades.timeVal.grade) : 'var(--border)'
              }"
            ></span>
          </div>
          <span class="text-xs mono w-20 text-right" style="color: var(--text-muted);">{{ grades.timeVal.label }}</span>
          <span
            class="grade-text text-2xl w-8 text-center"
            :style="{ color: gradeColor(grades.timeVal.grade) }"
          >{{ grades.timeVal.grade }}</span>
        </div>

        <!-- 勧誘あたり損益 -->
        <div class="flex items-center gap-4">
          <span class="text-sm w-28 shrink-0" style="color: var(--text-muted);">勧誘損益/人</span>
          <div class="flex gap-1 flex-1">
            <span
              v-for="i in 6"
              :key="i"
              class="h-2 flex-1 rounded-sm"
              :style="{
                backgroundColor: i <= grades.perRecruit.bars ? gradeColor(grades.perRecruit.grade) : 'var(--border)'
              }"
            ></span>
          </div>
          <span class="text-xs mono w-20 text-right" style="color: var(--text-muted);">{{ grades.perRecruit.label }}</span>
          <span
            class="grade-text text-2xl w-8 text-center"
            :style="{ color: gradeColor(grades.perRecruit.grade) }"
          >{{ grades.perRecruit.grade }}</span>
        </div>

      </div>

      <!-- 総合評定 -->
      <div
        class="rounded-lg p-5 flex items-center justify-between"
        :style="{
          background: grades.overall === 'F' ? 'var(--danger-bg)' : 'rgba(59,130,246,0.05)',
          border: `1px solid ${grades.overall === 'F' ? 'var(--danger-border)' : 'rgba(59,130,246,0.2)'}`,
        }"
      >
        <div>
          <div class="text-xs tracking-widest mb-1" style="color: var(--text-muted);">OVERALL GRADE</div>
          <div class="text-sm font-medium" style="color: var(--text-primary);">総合評定</div>
        </div>
        <div
          class="grade-text"
          style="font-size: 6rem; line-height: 1;"
          :style="{ color: gradeColor(grades.overall) }"
        >{{ grades.overall }}</div>
      </div>

      <!-- 数値サマリー -->
      <div class="grid grid-cols-2 gap-3">
        <!-- 最終年 -->
        <div
          class="rounded-lg p-4"
          style="background-color: var(--bg-surface); border: 1px solid var(--border);"
        >
          <div class="text-xs tracking-wider mb-3" style="color: var(--text-muted);">最終年サマリー</div>
          <div class="space-y-2">
            <div class="flex justify-between items-center">
              <span class="text-xs" style="color: var(--text-muted);">ボーナス</span>
              <span class="mono text-sm" style="color: var(--text-primary);">{{ fmt(props.data.last_year_summary.annual_income) }}</span>
            </div>
            <div class="flex justify-between items-center">
              <span class="text-xs" style="color: var(--text-muted);">費用</span>
              <span class="mono text-sm" style="color: var(--grade-f);">
                {{ fmt(props.data.last_year_summary.total_activity_cost + props.data.last_year_summary.total_self_purchases) }}
              </span>
            </div>
            <div
              class="pt-2 flex justify-between items-center"
              style="border-top: 1px solid var(--border);"
            >
              <span class="text-xs font-medium" style="color: var(--text-primary);">純損益</span>
              <span
                class="mono font-bold text-base"
                :style="{ color: props.data.last_year_summary.net_profit >= 0 ? 'var(--grade-a)' : 'var(--grade-f)' }"
              >
                {{ fmtSigned(props.data.last_year_summary.net_profit) }}
              </span>
            </div>
          </div>
        </div>

        <!-- 全期間 -->
        <div
          class="rounded-lg p-4"
          style="background-color: var(--bg-surface); border: 1px solid var(--border);"
        >
          <div class="text-xs tracking-wider mb-3" style="color: var(--text-muted);">全期間サマリー</div>
          <div class="space-y-2">
            <div class="flex justify-between items-center">
              <span class="text-xs" style="color: var(--text-muted);">ボーナス計</span>
              <span class="mono text-sm" style="color: var(--text-primary);">{{ fmt(props.data.bonus) }}</span>
            </div>
            <div class="flex justify-between items-center">
              <span class="text-xs" style="color: var(--text-muted);">勧誘累計</span>
              <span class="mono text-sm" style="color: var(--text-primary);">{{ fmt(props.data.invites || 0) }} 人</span>
            </div>
            <div
              class="pt-2 flex justify-between items-center"
              style="border-top: 1px solid var(--border);"
            >
              <span class="text-xs font-medium" style="color: var(--text-primary);">純損益</span>
              <span
                class="mono font-bold text-base"
                :style="{ color: props.data.net_profit >= 0 ? 'var(--grade-a)' : 'var(--grade-f)' }"
              >
                {{ fmtSigned(props.data.net_profit) }}
              </span>
            </div>
          </div>
        </div>
      </div>

      <!-- 目標達成状況 -->
      <div
        class="rounded-lg p-4 flex items-start gap-3"
        :style="{
          background: props.data.target_reached_year ? 'rgba(16,185,129,0.08)' : 'var(--danger-bg)',
          border: `1px solid ${props.data.target_reached_year ? 'rgba(16,185,129,0.25)' : 'var(--danger-border)'}`,
        }"
      >
        <div>
          <p
            class="font-semibold text-sm"
            :style="{ color: props.data.target_reached_year ? 'var(--grade-a)' : 'var(--grade-f)' }"
          >
            {{ props.data.target_reached_year
              ? `${props.data.target_reached_year} 年目に目標達成`
              : '活動期間内に目標年商に達しませんでした' }}
          </p>
          <p class="text-xs mt-1" style="color: var(--text-muted);">
            目標年商：<span class="mono" style="color: var(--text-primary);">{{ fmt(props.data.target_annual_income) }} 円</span>
          </p>
          <p v-if="props.data.target_reached_year" class="text-xs" style="color: var(--text-muted);">
            達成年ボーナス：<span class="mono" style="color: var(--text-primary);">{{ fmt(props.data.target_year_bonus) }} 円</span>
          </p>
        </div>
      </div>

    </div>
  </div>

</div>
</template>
