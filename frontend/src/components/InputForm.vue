<script setup>
import { ref } from 'vue';
// emitできるイベントを宣言
const emit = defineEmits(['submit'])

const months = ref(60);
const selfMonthlyYen = ref(null);
const invitePerMonth = ref(null);
const area = ref('city_center');
const targetAnnualIncome = ref(null);

function onSubmit() {
    // async (params)のparams
    const params = {
        months: Number(months.value),
        self_monthly_yen: Number(selfMonthlyYen.value),
        invite_per_month: Number(invitePerMonth.value),
        area: area.value,
        target_annual_income: Number(targetAnnualIncome.value),
    };
    // 親コンポーネント(SimulatorPage.vue)にイベントと値を送る
    emit('submit', params);
}
</script>

<template>
    <form @submit.prevent="onSubmit" class="w-full max-w-4xl mx-auto rounded-lg shadow-lg space-y-5 bg-gray-100 p-10">
        <div class="flex items-center gap-4">
            <label for="months" class="w-40 text-gray-900 text-right">活動期間（月）: </label>
            <input id="months" v-model="months" type="number" class="flex-1 text-gray-900 border bg-white px-2 py-1 rounded" required />
        </div>

        <div class="flex items-center gap-4">
            <label for="selfMonthlyYen" class="w-40 text-gray-900 text-right">月額購入金額（円）: </label>
            <input id="selfMonthlyYen" v-model="selfMonthlyYen" type="number" placeholder="15,000" class="flex-1 text-gray-900 border bg-white px-2 py-1 rounded" required />
        </div>

        <div class="flex items-center gap-4">
            <label for="invitePerMonth" class="w-40 text-gray-900 text-right">勧誘人数（月）: </label>
            <input id="invitePerMonth" v-model="invitePerMonth" type="number" placeholder="0" class="flex-1 text-gray-900 border bg-white px-2 py-1 rounded" required />
        </div>

        <div class="flex items-center gap-4">
            <label for="area" class="w-40 text-gray-900 text-right">活動地域： </label>
            <select id="area" v-model="area" class="flex-1 text-gray-900 border bg-white px-2 py-1 rounded" required>
                <option value="city_center">都心部</option>
                <option value="local_city">地方都市</option>
                <option value="local_town">地方</option>
            </select>
        </div>

        <div class="flex items-center gap-4">
            <label for="targetAnnualIncome" class="w-40 text-gray-900 text-right">目標年商（円）: </label>
            <input id="targetAnnualIncome" v-model.number="targetAnnualIncome" type="number" placeholder="0" class="flex-1 text-gray-900 border bg-white px-2 py-1 rounded" />
        </div>

        <div class="text-center pt-4">
        <button class="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-6 py-2 rounded">
            計算
        </button>
        </div>
    </form>
</template>
