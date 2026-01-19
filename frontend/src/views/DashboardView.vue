<script setup lang="ts">
import { onMounted, ref, computed } from 'vue'
import { axiosInstance } from '@/services/api'
import KPICard from '@/components/dashboard/KPICard.vue'
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

const totalAcreage = computed(() =>
  farms.value.reduce((sum, farm) => sum + Number(farm.total_acreage), 0),
)
const totalCrops = computed(() => farms.value.reduce((sum, farm) => sum + farm.crop_count, 0))
const totalAssets = computed(() => farms.value.reduce((sum, farm) => sum + farm.asset_count, 0))
</script>

<template>
  <main class="overflow-y-auto">
    <div>
      <p v-if="loading">Loading farms...</p>
      <div>
        <KPICard title="Total Farms" :value="farms.length" />
        <KPICard title="Total Acreage" :value="totalAcreage" />
        <KPICard title="Active Crops" :value="totalCrops" />
        <KPICard title="Total Assets" :value="totalAssets" />
      </div>
    </div>
  </main>
</template>

<style scoped></style>
