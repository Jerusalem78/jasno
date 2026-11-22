<script setup>
import BrandLogo from '../../../shared/ui/BrandLogo.vue'

defineProps({ activeSection: { type: String, default: 'today' } })
const emit = defineEmits(['navigate', 'select'])

const sections = [
  { id: 'today', label: 'Сегодня', icon: '/figma/house.svg' },
  { id: 'skills', label: 'Навыки', icon: '/figma/chart-combined.svg' },
  { id: 'review', label: 'Повторение', icon: '/figma/repeat-dashboard.svg' },
  { id: 'tasks', label: 'Задания', icon: '/figma/list-checks.svg' },
  { id: 'progress', label: 'Прогресс', icon: '/figma/chart-line.svg' },
  { id: 'profile-card', label: 'Профиль', icon: '/figma/user-round.svg' },
]
</script>

<template>
  <header class="dashboard-header">
    <BrandLogo href="/" navigate-to="landing" label="Вернуться на главную" @navigate="emit('navigate', $event)" />
    <div class="dashboard-user">
      <button class="notification-button" type="button" aria-label="Уведомления"><img src="/figma/bell.svg" alt="" /></button>
      <button class="avatar-button" type="button" @click="emit('select', 'profile-card')" aria-label="Открыть профиль">А</button>
    </div>
  </header>

  <nav class="dashboard-nav" aria-label="Разделы кабинета">
    <button v-for="section in sections" :key="section.id" type="button" :class="{ selected: activeSection === section.id }" @click="emit('select', section.id)">
      <img :src="section.icon" alt="" /><span>{{ section.label }}</span>
    </button>
  </nav>
</template>
