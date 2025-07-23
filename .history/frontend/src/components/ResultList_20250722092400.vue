<script setup>
defineProps({ data: Object });
</script>

<template>
    <div>
    <h2 class="text-xl font-semibold mb-2">結果</h2>
    <ul class="border p-2">
        <li v-for="(pv, member) in data.distribution" :key="member">
        {{ member }} : {{ pv }} PV
        </li>
    </ul>
    </div>
</template>
