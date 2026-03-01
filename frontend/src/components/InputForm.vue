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
    <div class="bg-slate-800 border border-slate-700 rounded-2xl shadow-xl p-8">
      <div class="mb-7">
        <h2 class="text-xl font-bold text-white">シミュレーション設定</h2>
        <p class="text-slate-400 text-sm mt-1">条件を入力して収支をシミュレーションします</p>
      </div>

      <div class="space-y-5">
        <!-- 活動期間 -->
        <div class="flex flex-col gap-1.5">
          <label for="months" class="text-sm font-medium text-slate-300">
            📅 活動期間
          </label>
          <div class="relative">
            <input
              id="months"
              v-model="months"
              type="number"
              class="w-full bg-slate-900 border border-slate-600 text-white px-4 py-2.5 pr-12 rounded-lg
                     focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500
                     transition-colors placeholder-slate-500"
              required
            />
            <span class="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 text-sm pointer-events-none">ヶ月</span>
          </div>
        </div>

        <!-- 月額購入金額 -->
        <div class="flex flex-col gap-1.5">
          <label for="selfMonthlyYen" class="text-sm font-medium text-slate-300">
            💰 月額購入金額
          </label>
          <div class="relative">
            <span class="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 pointer-events-none">¥</span>
            <input
              id="selfMonthlyYen"
              v-model="selfMonthlyYen"
              type="number"
              placeholder="15000"
              class="w-full bg-slate-900 border border-slate-600 text-white pl-8 pr-4 py-2.5 rounded-lg
                     focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500
                     transition-colors placeholder-slate-500"
              required
            />
          </div>
        </div>

        <!-- 勧誘人数 -->
        <div class="flex flex-col gap-1.5">
          <label for="invitePerMonth" class="text-sm font-medium text-slate-300">
            👥 月間勧誘人数
          </label>
          <div class="relative">
            <input
              id="invitePerMonth"
              v-model="invitePerMonth"
              type="number"
              placeholder="0"
              class="w-full bg-slate-900 border border-slate-600 text-white px-4 py-2.5 pr-16 rounded-lg
                     focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500
                     transition-colors placeholder-slate-500"
              required
            />
            <span class="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 text-sm pointer-events-none">人/月</span>
          </div>
        </div>

        <!-- 活動地域 -->
        <div class="flex flex-col gap-1.5">
          <label for="area" class="text-sm font-medium text-slate-300">
            📍 活動地域
          </label>
          <select
            id="area"
            v-model="area"
            class="w-full bg-slate-900 border border-slate-600 text-white px-4 py-2.5 rounded-lg
                   focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500
                   transition-colors cursor-pointer"
            required
          >
            <option value="city_center">🏙️ 都心部</option>
            <option value="local_city">🏘️ 地方都市</option>
            <option value="local_town">🌾 地方</option>
          </select>
        </div>

        <!-- 目標年商 -->
        <div class="flex flex-col gap-1.5">
          <label for="targetAnnualIncome" class="text-sm font-medium text-slate-300">
            🎯 目標年商 <span class="text-slate-500 font-normal text-xs">(任意)</span>
          </label>
          <div class="relative">
            <span class="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 pointer-events-none">¥</span>
            <input
              id="targetAnnualIncome"
              v-model.number="targetAnnualIncome"
              type="number"
              placeholder="0"
              class="w-full bg-slate-900 border border-slate-600 text-white pl-8 pr-4 py-2.5 rounded-lg
                     focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500
                     transition-colors placeholder-slate-500"
            />
          </div>
        </div>
      </div>

      <div class="mt-8">
        <button
          type="submit"
          class="w-full bg-indigo-600 hover:bg-indigo-500 active:bg-indigo-700 text-white font-semibold
                 py-3 px-6 rounded-lg transition-colors duration-200
                 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 focus:ring-offset-slate-800"
        >
          シミュレーション実行
        </button>
      </div>
    </div>
  </form>
</template>
