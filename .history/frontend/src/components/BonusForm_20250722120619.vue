<template>
    <form @submit.prevent="submit" class="space-y-2 border p-4 rounded">
        <h2 class="text-xl font-semibold mb-2">差額ボーナス</h2>
        <div v-for="(row, idx) in rows" :key="idx" class="flex gap-2 items-center">
            <input v-model="row.if" placeholder="ID" class="border px-2 py-1 w-24" />
            <input v-model.number="row.yen" placeholder="金額（円）" type>
        </div>
    </form>
</template>