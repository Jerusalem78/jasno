<script setup>
import { computed, ref, watch } from 'vue'
import GoogleAuthButton from '../../../features/google-auth/ui/GoogleAuthButton.vue'
import BrandLogo from '../../../shared/ui/BrandLogo.vue'
import AuthIntro from '../../../widgets/auth-intro/ui/AuthIntro.vue'

const props = defineProps({ mode: { type: String, default: 'login' } })
const emit = defineEmits(['navigate'])
const currentView = computed(() => props.mode)
const authNotice = ref('')
const showPassword = ref(false)
const authForm = ref({ name: '', email: '', password: '', acceptedTerms: false })

watch(() => props.mode, () => { authNotice.value = '' })

function navigateTo(view) {
  emit('navigate', view)
}

function requestAuth(intent) {
  window.dispatchEvent(new CustomEvent('jasno:auth', { detail: { intent, flow: props.mode } }))
  if (intent === 'google') authNotice.value = 'Вход через Google подключим после настройки авторизации.'
  if (intent === 'email-login' || intent === 'register') navigateTo('today')
}
</script>
<template>
<main class="auth-page">
    <header class="auth-header">
      <BrandLogo href="/" navigate-to="landing" label="Ясно — на главную" @navigate="navigateTo" />
      <span class="auth-header-note">Ваш английский. Ваш маршрут.</span>
    </header>
    <div class="auth-layout">
      <AuthIntro />

      <section class="auth-card" aria-labelledby="auth-title">
        <span class="eyebrow">{{ currentView === 'register' ? 'ШАГ 1 ИЗ 3 · ЗНАКОМСТВО' : 'С ВОЗВРАЩЕНИЕМ' }}</span>
        <h2 id="auth-title">{{ currentView === 'register' ? 'Начнём знакомство' : 'С возвращением' }}</h2>
        <p class="auth-description">{{ currentView === 'register' ? 'Ваш первый шаг к понятному английскому.' : 'Войдите, чтобы продолжить свой маршрут.' }}</p>

        <form id="auth-form" class="auth-form" @submit.prevent="requestAuth(currentView === 'register' ? 'register' : 'email-login')">
          <label v-if="currentView === 'register'" class="auth-field">
            <span>Как вас зовут</span><input v-model.trim="authForm.name" name="name" type="text" autocomplete="name" placeholder="Анна" required />
          </label>
          <label class="auth-field">
            <span>Электронная почта</span><input v-model.trim="authForm.email" name="email" type="email" autocomplete="email" placeholder="anna@example.ru" required />
          </label>
          <label class="auth-field">
            <span>Пароль</span>
            <span class="password-input-wrap"><input v-model="authForm.password" name="password" :type="showPassword ? 'text' : 'password'" :autocomplete="currentView === 'register' ? 'new-password' : 'current-password'" :placeholder="currentView === 'register' ? 'Не менее 8 символов' : 'Введите пароль'" :minlength="currentView === 'register' ? 8 : undefined" required /><button type="button" class="password-toggle" :aria-label="showPassword ? 'Скрыть пароль' : 'Показать пароль'" @click="showPassword = !showPassword">{{ showPassword ? 'Скрыть' : 'Показать' }}</button></span>
            <small v-if="currentView === 'register'">Не менее 8 символов</small>
            <button v-else type="button" class="forgot-password" @click="authNotice = 'Сброс пароля можно будет подключить вместе с API авторизации.'">Забыли пароль?</button>
          </label>
          <label v-if="currentView === 'register'" class="auth-consent"><input v-model="authForm.acceptedTerms" type="checkbox" required /><span>Принимаю <a href="#terms">условия использования</a> и <a href="#privacy">политику конфиденциальности</a>.</span></label>
        </form>
        <div class="auth-divider auth-divider-google"><span>или</span></div>
        <GoogleAuthButton @select="requestAuth('google')" />
        <p class="auth-switch">{{ currentView === 'register' ? 'Уже учитесь с нами?' : 'Ещё нет аккаунта?' }} <button type="button" @click="navigateTo(currentView === 'register' ? 'login' : 'register')">{{ currentView === 'register' ? 'Войти' : 'Создать аккаунт' }}</button></p>
        <p v-if="authNotice" class="auth-notice auth-google-notice" role="status">{{ authNotice }}</p>
        <button class="button button-primary auth-submit" type="submit" form="auth-form">{{ currentView === 'register' ? 'Создать аккаунт' : 'Войти' }}<img src="/figma/arrow-right.svg" alt="" /></button>
      </section>
    </div>
    <footer class="auth-footer">© 2026 Ясно. Учитесь в своём темпе.</footer>
  </main>
</template>

