<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { axiosInstance } from '@/services/api'
import type { Farm } from '@/types/farm/types'

const farms = ref<Farm[]>([])
const loading = ref<boolean>(false)

onMounted(async () => {
  loading.value = true
  try {
    const response = await axiosInstance.get('/farms')
    farms.value = response.data
  } catch (error) {
    console.error(error)
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <main class="overflow-y-auto">
    <div>
      <div>
        <ul>
          <li v-if="loading">Loading farms...</li>
          <li v-else-if="!loading && farms.length === 0">No farms</li>
          <li v-else v-for="farm in farms" :key="farm.id">{{ farm.name }}</li>
        </ul>
      </div>
    </div>
  </main>
</template>

<style scoped></style>
