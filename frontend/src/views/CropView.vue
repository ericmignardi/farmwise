<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { axiosInstance } from '@/services/api'
import type { Crop } from '@/types/farm/types'

const crops = ref<Crop[]>([])
const loading = ref<boolean>(false)

onMounted(async () => {
  loading.value = true
  try {
    const response = await axiosInstance.get('/crops')
    crops.value = response.data
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
          <li v-if="loading">Loading crops...</li>
          <li v-else-if="!loading && crops.length === 0">No crops</li>
          <li v-else v-for="crop in crops" :key="crop.id">{{ crop.name }}</li>
        </ul>
      </div>
    </div>
  </main>
</template>

<style scoped></style>
