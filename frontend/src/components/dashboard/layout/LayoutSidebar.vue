<script setup lang="ts">
import { Brain, Grid2X2, HelpCircle, Settings, Factory, Wheat, Banknote } from 'lucide-vue-next'
import { RouterLink } from 'vue-router'
import { markRaw } from 'vue'

const navLinks = [
  { to: '/', icon: markRaw(Grid2X2), label: 'Dashboard' },
  { to: '/farms', icon: markRaw(Factory), label: 'Farms' },
  { to: '/crops', icon: markRaw(Wheat), label: 'Crops' },
  { to: '/assets', icon: markRaw(Banknote), label: 'Assets' },
  { to: '/chat', icon: markRaw(Brain), label: 'Chat' },
]

const bottomLinks = [
  { to: '/settings', icon: markRaw(Settings), label: 'Settings' },
  { to: '/help', icon: markRaw(HelpCircle), label: 'Help' },
]
</script>

<template>
  <aside
    class="shadow-sm hidden fixed left-0 top-0 bottom-0 w-16 md:w-64 p-2 border-r border-r-gray-200 bg-white md:flex flex-col justify-between"
  >
    <div>
      <div class="border-b border-b-gray-200 p-4 w-full flex justify-center md:justify-start">
        <RouterLink
          to="/"
          class="p-3 rounded-xl flex items-center gap-2 w-fit md:w-full text-sm hover:bg-gray-100 focus:ring-2 focus:ring-offset-2 focus:outline-none transition-colors"
        >
          <Wheat class="size-4 shrink-0 text-green-500" />
          <h1 class="hidden md:inline text-3xl font-bold italic">
            farm<span class="text-green-500">wise</span>
          </h1>
        </RouterLink>
      </div>

      <nav class="flex flex-col items-center md:items-start gap-4 p-4 w-full">
        <RouterLink
          v-for="link in navLinks"
          :key="link.to"
          :to="link.to"
          :title="link.label"
          class="p-3 rounded-xl hover:bg-gray-100 focus:ring-2 focus:ring-offset-2 focus:outline-none transition-colors flex items-center gap-2 w-fit md:w-full text-base font-medium"
          active-class="focus:ring-2 focus:ring-offset-2 focus:outline-none bg-stone-950 text-stone-50 font-semibold hover:bg-stone-900 transition-colors"
        >
          <component :is="link.icon" class="size-4" />
          <p class="hidden md:inline">{{ link.label }}</p>
        </RouterLink>
      </nav>
    </div>

    <div
      class="border-t border-t-gray-200 p-4 w-full flex flex-col items-center md:items-start gap-4"
    >
      <RouterLink
        v-for="link in bottomLinks"
        :key="link.to"
        :to="link.to"
        :title="link.label"
        class="p-3 rounded-xl hover:bg-gray-100 focus:ring-2 focus:ring-offset-2 focus:outline-none transition-colors flex items-center gap-2 w-fit md:w-full text-base font-medium"
        active-class="focus:ring-2 focus:ring-offset-2 focus:outline-none bg-stone-950 text-stone-50 font-semibold hover:bg-stone-900 transition-colors"
      >
        <component :is="link.icon" class="size-4" />
        <p class="hidden md:inline">{{ link.label }}</p>
      </RouterLink>
    </div>
  </aside>
</template>

<style scoped></style>
