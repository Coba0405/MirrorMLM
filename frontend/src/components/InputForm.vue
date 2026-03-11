<script setup>
import { ref } from 'vue';
const emit = defineEmits(['submit'])

const months = ref(60);
const selfMonthlyYen = ref(null);
const invitePerMonth = ref(null);
const area = ref('city_center');
const targetAnnualIncome = ref(null);

function onSubmit() {
  const params = {
    months: Number(months.value),
    self_monthly_yen: Number(selfMonthlyYen.value),
    invite_per_month: Number(invitePerMonth.value),
    area: area.value,
    target_annual_income: Number(targetAnnualIncome.value),
  };
  emit('submit', params);
}
</script>

<template>
  <form @submit.prevent="onSubmit" class="w-full max-w-2xl mx-auto">
    <div
      class="rounded-xl p-8"
      style="background-color: var(--bg-card); border: 1px solid var(--border);"
    >
      <!-- ヘッダー：縦アクセントライン付き -->
      <div class="mb-7 flex items-start gap-3">
        <div class="w-1 self-stretch rounded-full" style="background-color: var(--grade-c);"></div>
        <div>
          <h2 class="text-lg font-bold" style="color: var(--text-primary);">シミュレーション設定</h2>
          <p class="text-xs mt-1" style="color: var(--text-muted);">条件を入力して収支をシミュレーションします</p>
        </div>
      </div>

      <div class="space-y-5">
        <!-- 01 活動期間 -->
        <div class="flex flex-col gap-1.5">
          <label for="months" class="text-sm font-medium flex items-center gap-2" style="color: var(--text-primary);">
            <span class="mono text-xs" style="color: var(--text-muted);">01</span>
            活動期間
          </label>
          <div class="relative">
            <input
              id="months"
              v-model="months"
              type="number"
              class="w-full px-4 py-2.5 pr-12 rounded-lg mono text-sm focus:outline-none transition-colors"
              style="
                background-color: var(--bg-card);
                border: 1px solid var(--border);
                color: var(--text-primary);
              "
              required
            />
            <span class="absolute right-3 top-1/2 -translate-y-1/2 text-sm pointer-events-none" style="color: var(--text-muted);">ヶ月</span>
          </div>
        </div>

        <!-- 02 月額購入金額 -->
        <div class="flex flex-col gap-1.5">
          <label for="selfMonthlyYen" class="text-sm font-medium flex items-center gap-2" style="color: var(--text-primary);">
            <span class="mono text-xs" style="color: var(--text-muted);">02</span>
            月額購入金額
          </label>
          <div class="relative">
            <span class="absolute left-3 top-1/2 -translate-y-1/2 pointer-events-none mono text-sm" style="color: var(--text-muted);">¥</span>
            <input
              id="selfMonthlyYen"
              v-model="selfMonthlyYen"
              type="number"
              placeholder="15000"
              class="w-full pl-8 pr-4 py-2.5 rounded-lg mono text-sm focus:outline-none transition-colors"
              style="
                background-color: var(--bg-card);
                border: 1px solid var(--border);
                color: var(--text-primary);
              "
              required
            />
          </div>
        </div>

        <!-- 03 月間勧誘人数 -->
        <div class="flex flex-col gap-1.5">
          <label for="invitePerMonth" class="text-sm font-medium flex items-center gap-2" style="color: var(--text-primary);">
            <span class="mono text-xs" style="color: var(--text-muted);">03</span>
            月間勧誘人数
          </label>
          <div class="relative">
            <input
              id="invitePerMonth"
              v-model="invitePerMonth"
              type="number"
              placeholder="0"
              class="w-full px-4 py-2.5 pr-16 rounded-lg mono text-sm focus:outline-none transition-colors"
              style="
                background-color: var(--bg-card);
                border: 1px solid var(--border);
                color: var(--text-primary);
              "
              required
            />
            <span class="absolute right-3 top-1/2 -translate-y-1/2 text-sm pointer-events-none" style="color: var(--text-muted);">人/月</span>
          </div>
        </div>

        <!-- 04 活動地域 -->
        <div class="flex flex-col gap-1.5">
          <label for="area" class="text-sm font-medium flex items-center gap-2" style="color: var(--text-primary);">
            <span class="mono text-xs" style="color: var(--text-muted);">04</span>
            活動地域
          </label>
          <select
            id="area"
            v-model="area"
            class="w-full px-4 py-2.5 rounded-lg text-sm focus:outline-none transition-colors cursor-pointer"
            style="
              background-color: var(--bg-card);
              border: 1px solid var(--border);
              color: var(--text-primary);
            "
            required
          >
            <option value="city_center">都心部</option>
            <option value="local_city">地方都市</option>
            <option value="local_town">地方</option>
          </select>
        </div>

        <!-- 05 目標年商 -->
        <div class="flex flex-col gap-1.5">
          <label for="targetAnnualIncome" class="text-sm font-medium flex items-center gap-2" style="color: var(--text-primary);">
            <span class="mono text-xs" style="color: var(--text-muted);">05</span>
            目標年商
            <span class="text-xs font-normal" style="color: var(--text-muted);">(任意)</span>
          </label>
          <div class="relative">
            <span class="absolute left-3 top-1/2 -translate-y-1/2 pointer-events-none mono text-sm" style="color: var(--text-muted);">¥</span>
            <input
              id="targetAnnualIncome"
              v-model.number="targetAnnualIncome"
              type="number"
              placeholder="0"
              class="w-full pl-8 pr-4 py-2.5 rounded-lg mono text-sm focus:outline-none transition-colors"
              style="
                background-color: var(--bg-card);
                border: 1px solid var(--border);
                color: var(--text-primary);
              "
            />
          </div>
        </div>
      </div>

      <div class="mt-8">
        <button
          type="submit"
          class="w-full font-bold py-3 px-6 rounded-lg transition-colors duration-200 tracking-wider text-sm"
          style="
            background-color: var(--text-primary);
            color: var(--bg-root);
          "
          onmouseover="this.style.backgroundColor='var(--grade-c)'; this.style.color='var(--bg-root)';"
          onmouseout="this.style.backgroundColor='var(--text-primary)'; this.style.color='var(--bg-root)';"
        >
          シミュレーション実行
        </button>
      </div>
    </div>
  </form>
</template>
