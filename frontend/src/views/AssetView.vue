<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { axiosInstance } from '@/services/api'
import type { Asset } from '@/types/farm/types'

const assets = ref<Asset[]>([])
const loading = ref<boolean>(false)

onMounted(async () => {
  loading.value = true
  try {
    const response = await axiosInstance.get('/assets')
    assets.value = response.data
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
          <li v-if="loading">Loading assets...</li>
          <li v-else-if="!loading && assets.length === 0">No assets</li>
          <li v-else v-for="asset in assets" :key="asset.id">{{ asset.name }}</li>
        </ul>
      </div>
    </div>
  </main>
</template>

<style scoped></style>
