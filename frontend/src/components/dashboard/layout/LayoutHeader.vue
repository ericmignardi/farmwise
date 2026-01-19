<script setup lang="ts">
import { Menu } from 'lucide-vue-next'
import { useRoute } from 'vue-router'
import { computed } from 'vue'

const route = useRoute()

const pageTitle = computed(() => {
  const path = route.path.slice(1) // Remove leading "/"
  if (!path) return 'Dashboard' // Handle "/" route
  // Capitalize first letter: "farms" → "Farms"
  return path.charAt(0).toUpperCase() + path.slice(1)
})
</script>

<template>
  <header class="p-8 border-b border-b-gray-200 flex items-center gap-8">
    <button
      class="p-3 rounded-xl hover:bg-gray-100 focus:ring-2 focus:ring-offset-2 focus:outline-none transition-colors md:hidden"
    >
      <Menu class="size-6" />
    </button>
    <h1 class="text-2xl font-semibold">{{ pageTitle }}</h1>
  </header>
</template>

<style scoped></style>
