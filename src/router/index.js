import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from '@/views/LoginPage.vue'
import TaskMonitoringPage from '@/views/MonitoringPage.vue' 

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: LoginPage
  },
  {
    path: '/taskMonitoring', 
    name: 'TaskMonitoring',
    component: TaskMonitoringPage
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router