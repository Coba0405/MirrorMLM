<script setup>
import Header from './components/Header.vue';
import SimulatorPage from './components/SimulatorPage.vue';
import Footer from './components/Footer.vue';
</script>

<template>
  <div class="min-h-screen" style="background-color: var(--bg-root)">
    <Header />
    <main class="max-w-4xl mx-auto px-4 py-10">
      <SimulatorPage />
    </main>
    <Footer />
  </div>
</template>
