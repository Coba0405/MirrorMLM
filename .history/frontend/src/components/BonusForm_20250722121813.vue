<template>
    <form @submit.prevent="submit" class="space-y-2 border p-4 rounded">
        <h2 class="text-xl font-semibold mb-2">差額ボーナス</h2>
        <div v-for="(row, idx) in rows" :key="idx" class="flex gap-2 items-center">
            <input v-model="row.if" placeholder="ID" class="border px-2 py-1 w-24" />
            <input v-model.number="row.yen" placeholder="金額（円）" type="number" class="border px-2 py-1 w-36" />
            <button type="button" @click="remove(idx)" class="bg-gray-300 px-2 py-0.5 rounded">❌</button>
        </div>
        <button type="button" @click="add" class="bg-gray-300 px-2 py-0.5 rounded">+行</button>
        <button class="bg-blue-600 text-while px-4 py-1 rounded">計算</button>
    </form>
</template>

<script setup>
import { reactive } from 'vue';

const emit = defineEmits(["bonus"]);
const rows = reactive([{ id: "A", yen: 47000 }]);

function add() {
    rows.push({ id: "", yen: 0});
}
function remove(i) {
    rows.splice(i, 1);
}
async function submit() {
    const purchases = rows.reduce((acc, r) => {
        if (r.id && r.yen > 0) acc[r.id] = r.yen;
        return acc;
    }, {});
    const res = await fetch("http://localhost:8000/api/bonus", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ purchases }),
    });
    emit("bonus", )
}
</script>
