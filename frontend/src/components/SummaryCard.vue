<script setup>
const props = defineProps(['data']);
const fmt = (n) => n.toLocaleString('ja-JP');
</script>

<template>
<div class="w-full max-w-4xl mx-auto bg-green-500 p-4 m-4 rounded-lg shadow-md">
<h2 class="text-xl font-semibold mb-2">シミュレーション結果</h2>
    <ul class="space-y-1">
        <li>
            目標年商：
            <span class="font-bold">
                {{ fmt(props.data.target_annual_income) }} 円
            </span>
        </li>
        <li v-if="props.data.target_reached_year">
            目標達成年のボーナス総額：
            <span class="font-bold">
                {{ fmt(props.data.target_year_bonus) }} 円
            </span>
        </li>
        <li v-if="props.data.target_reached_year !== null">
            目標達成年：
            <span class="font-bold">
                {{ props.data.target_reached_year }} 年目
            </span>
        </li>
        <li v-else class="text-red-600 font-bold">活動期間内に目標年商に達しませんでした</li>
    </ul>

    <div class="flex flex-col lg:flex-row gap-4">
        <div class="w-full lg:w-1/2 bg-blue-400 p-4 m-1 rounded-lg shadow-md">
            <h3 class="text-xl font-semibold mb-2">最終年Summary</h3>
            <ul class="space-y-1">
                <li>
                    最終年のボーナス総額：
                    <span class="font-bold">
                        {{ fmt(props.data.last_year_summary.annual_income) }} 円
                    </span>
                </li>
                <li>
                    最終年の費用総額：
                    <span class="font-bold">
                        {{ fmt(props.data.last_year_summary.total_activity_cost + props.data.last_year_summary.total_self_purchases) }} 円
                    </span>
                </li>
                <li>
                    最終年の純利益・純損失：
                    <span class="font-bold">
                        {{ fmt(props.data.last_year_summary.net_profit) }} 円
                    </span>
                </li>
            </ul>
        </div>
        <div class="w-full lg:w-1/2 bg-blue-400 p-4 m-1 rounded-lg shadow-md">
            <h3 class="text-xl font-semibold mb-2">全期間Summary</h3>
            <ul class="space-y-1">
                <li>
                    全期間のボーナス総額：
                    <span class="font-bold">
                        {{ fmt(props.data.bonus) }} 円
                    </span>
                </li>
                <li>
                    全期間の純利益/純損失：
                    <span class="font-bold">
                        {{ fmt(props.data.net_profit) }} 円
                    </span>
                </li>
            </ul>
        </div>
    </div>
</div>
</template>