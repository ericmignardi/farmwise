<script setup lang="ts">
defineProps<{
  title: string
  value: number
}>()
</script>

<template>
  <div
    class="p-4 border border-gray-300 rounded-lg bg-white text-stone-950 w-40 flex flex-col items-start gap-2 shadow-md"
  >
    <p class="text-sm font-normal">{{ title }}</p>
    <p class="text-4xl font-bold">{{ value }}</p>
  </div>
</template>

<style scoped></style>
