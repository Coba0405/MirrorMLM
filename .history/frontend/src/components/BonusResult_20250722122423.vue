<template>
    <div class="border p-4 rounded">
        <h2 class="text-xl font-semibold mb-2">差額ボーナス結果</h2>
        <table class="min-w-full border">
            <thead class="bg-gray-100">
                <tr>
                    <td>ID</td>
                    <td>Rate</td>
                    <td>Bonus（円）</td>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(info, mumber) in data" :key="mumber">
                    <td>{{ member }}</td>
                    <td>{{  (info.rate * 100).toFixed(0) }}%</td>
                    <td>{{ info.bonus. }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>