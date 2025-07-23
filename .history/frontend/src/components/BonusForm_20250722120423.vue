<template>
    <form @submit.prevent="submit" class="space-y-2 border p-4 rounded">
        <h2 class="text-xl font-semibold mb-2">差額ボーナス</h2>
        <div v-for="(row, idx) in rows" :key="idx" class="flex gap-2 items-center"></div>
    </form>
</template>