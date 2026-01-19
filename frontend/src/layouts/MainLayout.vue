<script setup lang="ts">
import LayoutHeader from '@/components/dashboard/layout/LayoutHeader.vue'
import LayoutSidebar from '@/components/dashboard/layout/LayoutSidebar.vue'
</script>

<template>
  <div>
    <LayoutSidebar />
    <div class="ml-0 md:ml-64 overflow-y-auto">
      <LayoutHeader />
      <slot />
    </div>
  </div>
</template>

<style scoped></style>
