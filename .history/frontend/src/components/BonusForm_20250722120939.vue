<template>
    <form @submit.prevent="submit" class="space-y-2 border p-4 rounded">
        <h2 class="text-xl font-semibold mb-2">差額ボーナス</h2>
        <div v-for="(row, idx) in rows" :key="idx" class="flex gap-2 items-center">
            <input v-model="row.if" placeholder="ID" class="border px-2 py-1 w-24" />
            <input v-model.number="row.yen" placeholder="金額（円）" type="number" class="border px-2 py-1 w-36" />
            <button type="button" @click="remove(idx)" class="bg-gray-300 px-2 py-0.5 rounded">❌</button>
        </div>
        <button type="button" @click="add" class="bg-gray-300 px-2 py-0.5 rounded">+行</button>
        
    </form>
</template>