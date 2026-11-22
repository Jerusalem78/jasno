<script setup>
import { ref } from 'vue'
import { dashboardTasks, skills, weekDays } from '../../../entities/learning/model/demo-data.js'
import { useTodayProgress } from '../../../features/today-progress/model/useTodayProgress.js'
import DashboardNavigation from '../../../widgets/dashboard-navigation/ui/DashboardNavigation.vue'

const emit = defineEmits(['navigate'])
const activeDashboardSection = ref('today')
const { completedTasks, reviewedWords, showTranslation, goalComplete, completedCount, nextWord, remainingWords, toggleTask, markWordReviewed, toggleGoal } = useTodayProgress()
function openDashboardSection(id) {
  activeDashboardSection.value = id
  document.getElementById(id)?.scrollIntoView({ behavior: 'smooth', block: 'start' })
}
function navigateTo(view) { emit('navigate', view) }
</script>
<template>
<main class="dashboard-shell">
    <DashboardNavigation :active-section="activeDashboardSection" @select="openDashboardSection" @navigate="navigateTo" />

    <div class="dashboard-content">
      <section id="today" class="dashboard-welcome">
        <div class="welcome-level"><span class="eyebrow-pill">B1 · Средний</span><span>Ваша первая неделя</span></div>
        <h1>Анна, всё по плану</h1>
        <p>Сегодня не нужно выбирать, что учить. Просто начните.</p>
      </section>

      <div class="dashboard-columns">
        <div class="dashboard-primary-column">
          <section id="tasks" class="dashboard-card today-plan">
            <div class="dashboard-card-heading">
              <div><h2>План на сегодня</h2><p>{{ dashboardTasks.length }} задания · 20 минут · {{ completedCount }} из {{ dashboardTasks.length }} выполнено</p></div>
              <img class="heading-icon" src="/figma/list-checks-card.svg" alt="" />
            </div>
            <div class="dashboard-task-list">
              <button v-for="(task, index) in dashboardTasks" :key="task.title" class="dashboard-task" :class="{ completed: completedTasks.includes(index) }" type="button" :aria-pressed="completedTasks.includes(index)" @click="toggleTask(index)">
                <span class="dashboard-task-icon"><img :src="task.icon" alt="" /></span>
                <span class="dashboard-task-copy"><strong>{{ task.title }}</strong><small>{{ task.note }}</small></span>
                <span class="dashboard-task-time">{{ task.time }}</span>
                <span class="task-check" aria-hidden="true"><img v-if="completedTasks.includes(index)" src="/figma/check.svg" alt="" /></span>
              </button>
            </div>
            <button class="button button-primary dashboard-wide-button" type="button" @click="openDashboardSection('review')">Начать с повторения <img src="/figma/arrow-dashboard.svg" alt="" /></button>
          </section>

          <section class="dashboard-card weak-card">
            <div class="weak-card-top"><img src="/figma/focus-headphones.svg" alt="" /><strong>СЛАБОЕ МЕСТО</strong><span class="score-pill">42 / 100</span></div>
            <h2>Слышать — и понимать</h2>
            <p>В диалогах на слух пока сложнее, чем в тексте. Сегодня разберём заказ в кафе: сначала без подсказок, затем с расшифровкой.</p>
            <button class="button button-primary dashboard-wide-button" type="button" @click="toggleTask(1)">Тренировать аудирование <img src="/figma/arrow-dashboard.svg" alt="" /></button>
          </section>
        </div>

        <div class="dashboard-secondary-column">
          <section id="progress" class="dashboard-card streak-card">
            <div class="streak-heading"><img src="/figma/flame.svg" alt="" /><strong>7</strong><b>дней подряд</b></div>
            <p>Вы занимаетесь регулярно — так знания лучше остаются с вами.</p>
            <div class="week-strip" aria-label="Занятия за неделю">
              <span v-for="day in weekDays" :key="day.label" class="week-day"><i :class="{ 'day-done': day.done }"><img v-if="day.done" src="/figma/check.svg" alt="" /><img v-else src="/figma/circle.svg" alt="" /></i><small>{{ day.label }}</small></span>
            </div>
            <small class="week-caption">Ещё один короткий шаг сегодня — и серия продолжится</small>
          </section>

          <section id="review" class="dashboard-card vocabulary-card">
            <div class="dashboard-card-heading"><h2>Слова на повторение</h2><img class="heading-icon" src="/figma/repeat-vocab.svg" alt="" /></div>
            <div class="vocabulary-progress"><strong>{{ remainingWords }}</strong><span>слов ждут повторения сегодня</span></div>
            <p class="vocabulary-hint">Интервальное повторение помогает вспомнить слово как раз вовремя.</p>
            <button class="word-card" type="button" :aria-label="showTranslation ? 'Скрыть перевод' : 'Показать перевод'" @click="showTranslation = !showTranslation">
              <span>{{ nextWord.word }}</span><small>{{ showTranslation ? nextWord.translation : 'Нажмите, чтобы увидеть перевод' }}</small>
            </button>
            <div class="word-actions"><button type="button" class="word-action secondary" @click="markWordReviewed(false)">Повторить ещё</button><button type="button" class="word-action" @click="markWordReviewed(true)">Помню</button></div>
            <small class="vocabulary-footer">Сегодня уже повторено: {{ reviewedWords.length }} из 12</small>
          </section>

          <section class="dashboard-card lesson-card">
            <div class="lesson-heading"><img src="/figma/calendar-days.svg" alt="" /><span>МЕЖДУ УРОКАМИ</span></div>
            <h2>Следующий урок — в четверг</h2>
            <p>До встречи с преподавателем осталось два дня. Можно подготовить вопросы и повторить слова из последнего занятия.</p>
            <a href="#review" @click.prevent="openDashboardSection('review')">Посмотреть слова <img src="/figma/arrow-dashboard.svg" alt="" /></a>
          </section>
        </div>
      </div>

      <section class="dashboard-card goal-card">
        <span class="eyebrow">ВАША ЦЕЛЬ</span>
        <h2>Уверенно общаться в поездках</h2>
        <p>Небольшие занятия между уроками постепенно приближают вас к этой цели.</p>
        <button type="button" :class="['goal-button', { done: goalComplete }]" @click="toggleGoal">{{ goalComplete ? 'Цель на сегодня выполнена' : 'Отметить занятие за сегодня' }}</button>
      </section>

      <section id="skills" class="dashboard-card dashboard-skills">
        <div class="dashboard-card-heading"><h2>Карта навыков</h2><span class="score-pill">B1</span></div>
        <p>Примерная оценка на основе ваших занятий</p>
        <div v-for="skill in skills" :key="skill.name" class="dashboard-skill-meter">
          <div><span>{{ skill.name }}</span><span>{{ skill.score }} / 100</span></div><span class="meter-track"><span :style="{ width: `${skill.score}%` }"></span></span>
        </div>
        <p class="dashboard-skill-note"><img src="/figma/focus-headphones.svg" alt="" /> Сегодня уделим больше внимания аудированию</p>
      </section>

      <section id="profile-card" class="profile-summary"><span class="avatar-button">А</span><span><strong>Анна</strong><small>Уровень B1 · Средний</small></span><button type="button" @click="navigateTo('landing')">На главную</button></section>
    </div>
  </main>
</template>

