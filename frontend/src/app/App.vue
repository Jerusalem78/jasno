<script setup>
import { computed, onMounted, onUnmounted, ref } from 'vue'
import AuthPage from '../pages/auth/ui/AuthPage.vue'
import LandingPage from '../pages/landing/ui/LandingPage.vue'
import TodayPage from '../pages/today/ui/TodayPage.vue'

const currentPath = ref(window.location.pathname)
const currentPage = computed(() => {
  if (currentPath.value === '/today') return 'today'
  if (currentPath.value === '/login') return 'login'
  if (currentPath.value === '/register') return 'register'
  return 'landing'
})

function syncPath() {
  currentPath.value = window.location.pathname
}

function navigate(page) {
  const routes = { landing: '/', today: '/today', login: '/login', register: '/register' }
  const nextPath = routes[page] || '/'
  window.history.pushState({}, '', nextPath)
  currentPath.value = nextPath
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

onMounted(() => window.addEventListener('popstate', syncPath))
onUnmounted(() => window.removeEventListener('popstate', syncPath))
</script>

<template>
  <AuthPage v-if="currentPage === 'login' || currentPage === 'register'" :mode="currentPage" @navigate="navigate" />
  <TodayPage v-else-if="currentPage === 'today'" @navigate="navigate" />
  <LandingPage v-else @navigate="navigate" />
</template>
