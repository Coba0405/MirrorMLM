<script setup>
import { ref } from 'vue';
import axios from 'axios';

import InputForm from './InputForm.vue';
import SummaryCard from './SummaryCard.vue';
import ResultsTable from './ResultsTable.vue';

const summary = ref(null)
const records = ref([])
const isLoading = ref(false)

const API_URL = import.meta.env.VITE_API_URL;

const runSimulation = async (params) => {
  isLoading.value = true;
  try {
    const res = await axios.post(`${API_URL}/api/simulate`, params);
    summary.value = res.data.summary;
    records.value = res.data.records;
  } catch (err) {
    console.error("通信エラー:", err);
  } finally {
    isLoading.value = false;
  }
};
</script>

<template>
  <div class="space-y-8">
    <InputForm @submit="runSimulation" />

    <div v-if="isLoading" class="flex items-center justify-center py-16">
      <div class="flex items-center gap-3 text-slate-400">
        <svg class="animate-spin h-5 w-5 text-indigo-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
          <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
        </svg>
        <span>シミュレーション実行中...</span>
      </div>
    </div>

    <template v-else>
      <SummaryCard v-if="summary" :data="summary" />
      <ResultsTable v-if="records.length" :rows="records" />
    </template>
  </div>
</template>
