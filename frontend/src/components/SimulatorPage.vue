<script setup>
import { ref } from 'vue';
import axios from 'axios';

import InputForm from './InputForm.vue';
import SummaryCard from './SummaryCard.vue';
import ResultsTable from './ResultsTable.vue';

// 単一のオブジェクトが入るのでリアクティブをnullで初期化
const summary = ref(null)
// 配列として初期化
const records = ref([])

// Viteの場合　環境変数は原則VITE_を使用
const API_URL = import.meta.env.VITE_API_URL;

// InputFormから受け取ったparamsを引数にバックエンドへリクエスト
const runSimulation = async (params) => {
    // console.log("API送信パラメータ:", params);
    // console.log("送信先URL:", API_URL);

    try {
        // ここのparamsはFlaskがrequest.jsonとして受け取るもの
        const res = await axios.post(`${API_URL}/api/simulate`, params);
        // console.log("レスポンス:", res.data);
        // 返ってきたsummaryとrecordsを格納
        summary.value = res.data.summary;
        records.value = res.data.records;
    } catch (err) {
        console.error("通信エラー:", err);
    }
    };
</script>

<template>
    <div>
        <section>
            <!-- 入力フォーム -->
            <InputForm @submit="runSimulation" />
            <!-- summary が取れたら表示 -->
            <SummaryCard v-if="summary" :data="summary" />
            <!-- 月別テーブル -->
            <ResultsTable v-if="records.length" :rows="records" />
        </section>
    </div>
</template>
