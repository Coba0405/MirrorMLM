<script setup>
import { ref } from 'vue';
import axios from 'axios';

import InputForm from './InputForm.vue';
import SummaryCard from './SummaryCard.vue';
import ResultsTable from './ResultsTable.vue';

const summary = ref(null)
const records = ref([])

const API_URL = import.meta.env.VITE_API_URL;

const runSimulation = async (params) => {
    const res = await axios.post(`${API_URL}/api/simulate`, params);
    summary.value = res.data.summary;
    records.value = res.data.records;
};
</script>

<template>
    <section>
        <!-- 入力フォーム -->
        <InputForm @submit="runSimulation" />
        <!-- summary が取れたら表示 -->
        <SummaryCard v-if="summary" :data="summary" />
        <!-- 月別テーブル -->
        <ResultsTable v-if="records.length" :rows="records" />
    </section>
</template>
