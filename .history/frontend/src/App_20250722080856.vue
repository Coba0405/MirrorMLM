<template>
    <div class="p-4 max-w-xl mx-auto">
    <h1 class="text-2xl font-bold mb-4">PVコピーシミュレーター</h1>
    <PvForm @result="handleResult" />
    <ResultList
        v-if="result"
        :data="result"
        class="mt-6"
    />
    </div>
</template>

<script>
import { ref } from "vue";
import PvForm from "./components/PvForm.vue";
import ResultList from "./components/ResultList.vue";

export default {
    name: "App",
    components: { PvForm },
    setup() {
        const result = ref(null);
        const handleResult = (res) => (result.value = res);
        return { result, handleResult };
    },
};
</script>