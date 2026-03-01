<script setup>
import Header from './components/Header.vue';
import SimulatorPage from './components/SimulatorPage.vue';
import Footer from './components/Footer.vue';
</script>

<template>
  <div class="min-h-screen bg-slate-900">
    <Header />
    <main class="max-w-5xl mx-auto px-4 py-10">
      <SimulatorPage />
    </main>
    <Footer />
  </div>
</template>
