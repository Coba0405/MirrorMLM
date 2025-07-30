<script setup>
const props = defineProps(['data']);
const fmt = (n) => new Intl.NumberFormat('ja-JP').format(n);
</script>

<template>
<div class="bg-gray-500 p-4 rounded-lg shadow-md">
<h2 class="text-xl font-semibold mb-2">シミュレーション結果（年間まとめ）</h2>
<ul class="space-y-1">
    <li>
    総ボーナス：
    <span class="font-bold">
        {{ fmt(props.data.total_bonus_yen) }} 円
    </span>
    </li>
    <li>
    総純利益：
    <span class="font-bold">
        {{ fmt(props.data.total_net_profit_yen) }} 円
    </span>
    </li>
    <li>
    目標年商：
    <span class="font-bold">
        {{ fmt(props.data.target_annual_income) }} 円
    </span>
    </li>
    <li v-if="props.data.year_achieved !== null">
    目標達成年：
    <span class="font-bold">
        {{ props.data.year_achieved }} 年目
    </span>
    </li>
    <li v-else class="text-red-600 font-bold">※期間内に未達</li>
</ul>
</div>
</template>