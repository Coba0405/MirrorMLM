<script setup>
const props = defineProps(['rows']);

const fmt = (n) => new Intl.NumberFormat('ja-JP').format(n);
</script>

<template>
<table class="w-full text-sm border">
<thead class="bg-gray-600">
    <tr>
    <th class="p-2 border">月</th>
    <th class="p-5  border">ボーナス</th>
    <th class="p-5 border">純利益</th>
    <th class="p-2 border">ダウン人数</th>
    <th class="p-5 border">勧誘活動費</th>
    <th class="p-1 border">ボーナス利率</th>
    <th class="p-7 border">グループBV</th>
    <th class="p-7 border">グループPV</th>

    </tr>
</thead>
<tbody>
    <tr v-for="row in props.rows" :key="row.month" class="odd:bg-gray :bg-slate-50">
    <td class="p-3 border text-center">{{ row.month }}</td>
    <td class="p-3 border text-center">{{ fmt(row.bonus) }} 円</td>
    <td class="p-3 border text-center">{{ fmt(row.net_profit) }} 円</td>
    <td class="p-3 border text-center">{{ fmt(row.count_child + row.count_grand) }} 人</td>
    <td class="p-3 border text-center">{{ fmt(row.activity_cost_monthly) }} 円</td>
    <td class="p-3 border text-center">{{ fmt(row.rate * 100) }} %</td>
    <td class="p-3 border text-center">{{ fmt(row.group_bv) }} BV</td>
    <td class="p-3 border text-center">{{ fmt(row.group_pv) }} PV</td>
    </tr>
</tbody>
</table>
</template>