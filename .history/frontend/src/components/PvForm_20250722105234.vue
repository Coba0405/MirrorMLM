<template>
    <form @submit.prevent="submit" class="flex flex-col gap-2">
    <label>
        購入者ID：
        <input v-model="purchaser" class="border px-2 py-1" />
    </label>
    <label>
        購入金額（円）：
        <input
        v-model.number="amount"
        type="number"
        class="border px-2 py-1"
        />
    </label>
    <button class="bg-blue-600 text-white px-4 py-1 rounded">
        計算
    </button>
    </form>
</template>

<script setup>
import { ref } from "vue";

const purchaser = ref("C");
const amount = ref(10000);
const emit = defineEmits(["result"]);

async function submit() {
    const res = await fetch("http://localhost:8000/api/distribute", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            purchaser: purchaser.value,
            amount_yen: amount.value,
        })
    });
    emit("result", await res.json());
}
</script>