<script setup>
import Header from './components/Header.vue';
import SimulatorPage from './components/SimulatorPage.vue';
</script>

<template>
    <div class="w-full min-h-screen text-white block flex-col items-center justify-start p-8">
        <header class="header">
            <Header />
        </header>
        <main class="main">
            <SimulatorPage />
        </main>
        <footer class="footer">footer</footer>
    </div>
</template>
