<script setup>
const props = defineProps(['rows']);

const fmt = (n) => {
    if (n === undefined || n === null || isNaN(n)) return '0';
    // 3桁区切りの日本語表記にして返す
    return n.toLocaleString('ja-JP');
};
</script>

<template>
<table class="max-w-5xl w-full mx-auto text-sm border">
<thead class="bg-green-500">
    <tr>
    <th class="p-1 border">月</th>
    <th class="p-1 border">ボーナス</th>
    <th class="p-1 border">純利益/<br>純損失</th>
    <th class="p-1 border">ダウン人数</th>
    <th class="p-1 border">自己購入費</th>
    <th class="p-1 border">勧誘活動費</th>
    <th class="p-1 border">ボーナス利率</th>
    <th class="p-1 border">グループBV</th>
    <th class="b-1 border">グループPV</th>

    </tr>
</thead>
<tbody>
    <tr
        v-for="row in props.rows"
        :key="row.month"
        :class="[
            'text-gray-900',
            (row.bonus - row.activity_cost_monthly - row.self_purchase) > 0
            ? 'bg-blue-300' : 'bg-slate-50', 'odd:bg0gray-100'
        ]"
    >
        <td class="p-3 border text-center">{{ row.month }}</td>
        <td class="p-3 border text-center">{{ fmt(row.bonus) }} 円</td>
        <td class="p-3 border text-center">{{ fmt(row.bonus - row.activity_cost_monthly - row.self_purchase) }} 円</td>
        <td class="p-3 border text-center">{{ fmt(row.count_child + row.count_grand) }} 人</td>
        <td class="p-3 border text-center">{{ fmt(row.self_purchase) }} 円</td>
        <td class="p-3 border text-center">{{ fmt(row.activity_cost_monthly) }} 円</td>
        <td class="p-3 border text-center">{{ fmt(row.rate * 100) }} %</td>
        <td class="p-3 border text-center">{{ fmt(row.group_bv) }} BV</td>
        <td class="p-3 border text-center">{{ fmt(row.group_pv) }} PV</td>
    </tr>
</tbody>
</table>
</template>