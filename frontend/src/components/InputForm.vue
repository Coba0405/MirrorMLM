<script setup>
import { ref } from 'vue';
const emit = defineEmits(['submit'])

const months = ref(24);
const selfMonthlyYen = ref(null);
const invitePerMonth = ref(null);
const area = ref('city_center');
const targetAnnualIncome = ref(null);

function onSubmit() {
    emit('submit', {
        months: months.value,
        self_monthly_yen: selfMonthlyYen.value,
        invite_per_month: invitePerMonth.value,
        area: area.value,
        target_annual_income: targetAnnualIncome.value,
    });
}
</script>

<template>
    <form @submit.prevent="onSubmit" class="flex flex-col gap-4 max-w-md">
        <label class="block">
        期間（月）:
        <input v-model="months" type="number" class="border ml-2 px-2 py-1" required/>
        </label>

        <label class="block">
        月額購入金額（円）:
        <input v-model="selfMonthlyYen" type="number" placeholder="15000" class="border ml-2 px-2 py-1" required/>
        </label>

        <label class="block">
        勧誘人数/月:
        <input v-model="invitePerMonth" type="number" placeholder="0" class="border ml-2 px-2 py-1" required/>
        </label>

        <label class="block">
        地域:
        <select v-model="area" class="border ml-2 px-2 py-1" required>
            <option value="city_center">都心部</option>
            <option value="local_city">地方都市</option>
            <option value="local_town">地方</option>
        </select>
        </label>

        <label class="block">
        目標年商（円）:
        <input v-model="targetAnnualIncome" type="number" placeholder="0" class="border ml-2 px-2 py-1" />
        </label>
        <!-- 各入力フィールド（省略） -->
        <button class="bg-blue-600 text-white px-4 py-2 rounded">計算</button>
    </form>
</template>