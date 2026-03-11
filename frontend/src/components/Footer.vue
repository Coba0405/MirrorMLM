<script setup>
import AssumptionsPanel from './AssumptionsPanel.vue';
</script>

<template>
  <footer
    class="py-12 px-6 mt-4"
    style="
      border-top: 1px solid var(--border);
      background-color: var(--bg-surface);
      color: var(--text-muted);
    "
  >
    <div class="max-w-4xl mx-auto space-y-8">

      <AssumptionsPanel />

      <!-- コピーライト -->
      <div class="text-center space-y-1" style="border-top: 1px solid var(--border); padding-top: 1.5rem;">
        <p class="text-xs" style="color: var(--text-muted);">
          このシミュレーターは参考情報であり、実際の報酬・費用とは異なる場合があります。個別の投資判断は自己責任でお願いいたします。
        </p>
        <p class="text-xs" style="color: var(--border);">© 2025 MirrorMLM. All rights reserved. Ver. 1.0.1</p>
      </div>

    </div>
  </footer>
</template>
