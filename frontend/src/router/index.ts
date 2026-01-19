import AssetView from '@/views/AssetView.vue'
import ChatView from '@/views/ChatView.vue'
import CropView from '@/views/CropView.vue'
import DashboardView from '@/views/DashboardView.vue'
import FarmView from '@/views/FarmView.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: DashboardView,
    },
    {
      path: '/farms',
      component: FarmView,
    },
    {
      path: '/crops',
      component: CropView,
    },
    {
      path: '/assets',
      component: AssetView,
    },
    {
      path: '/chat',
      component: ChatView,
    },
  ],
})

export default router
