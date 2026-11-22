<script setup>
import { ref } from 'vue'

const activeQuestion = ref(0)
const menuOpen = ref(false)

const tasks = [
  { icon: '/figma/repeat.svg', title: 'Повторить 12 слов', note: 'Интервальное повторение', time: '5 мин' },
  { icon: '/figma/headphones.svg', title: 'Разобрать разговор в кафе', note: 'Аудирование · уровень B1', time: '8 мин' },
  { icon: '/figma/mic.svg', title: 'Рассказать о своих планах', note: 'Говорение · запись ответа', time: '7 мин' },
]

const skills = [
  { name: 'Грамматика', score: 68 },
  { name: 'Словарный запас', score: 74 },
  { name: 'Аудирование', score: 42 },
  { name: 'Чтение', score: 71 },
  { name: 'Говорение', score: 56 },
]

const benefits = [
  {
    icon: '/figma/compass.svg',
    quote: '«Не понимаю, что подтянуть»',
    title: 'Знайте свою точку роста',
    body: 'Грамматика, слова, аудирование, чтение и говорение — в одной карте навыков. План подскажет, с чего начать.',
    tag: 'Фокус: аудирование',
    result: 'Больше практики там, где она нужна',
  },
  {
    icon: '/figma/repeat-card.svg',
    quote: '«Я ведь уже учила это слово»',
    title: 'Помните, а не переучивайте',
    body: 'Интервальное повторение возвращает слова до того, как они забудутся. Никаких случайных пробелов.',
    tag: 'Сегодня: 12 слов',
    result: 'Вовремя повторить — надолго запомнить',
  },
  {
    icon: '/figma/calendar-check.svg',
    quote: '«Что делать до следующего урока?»',
    title: 'Открывайте готовый план',
    body: 'Три конкретных задания на день свяжут занятия с преподавателем. 20 минут практики вместо долгого выбора.',
    tag: 'Ваш план: 20 минут',
    result: 'Слова → слушать → говорить',
  },
]

const steps = [
  { title: 'Расскажите о себе', text: 'Выберите цель и пройдите три коротких вопроса. Получите первую оценку уровня.' },
  { title: 'Получите свой маршрут', text: 'Увидьте навыки, точку роста и посильный план. Всё подстраивается под вашу цель.' },
  { title: 'Практикуйтесь понемногу', text: 'Выполняйте задания, повторяйте слова и наблюдайте за прогрессом.' },
]

const questions = [
  { question: 'С какого уровня можно начать?', answer: 'С любого: от A1 до C2. Короткий тест даст примерную отправную точку, а задания помогут уточнить её со временем.' },
  { question: 'Платформа заменяет преподавателя?', answer: 'Нет. Она помогает заниматься самостоятельно между уроками: закреплять материал, повторять слова и приходить к преподавателю с вопросами.' },
  { question: 'Как вы помогаете не забывать слова?', answer: 'Слова возвращаются через увеличивающиеся интервалы. Сложные встречаются чаще, знакомые — реже. Список на сегодня уже собран за вас.' },
  { question: 'Сколько времени нужно в день?', answer: 'Начните с 20 минут. Это три небольших задания; можно выполнить их сразу или разделить в течение дня.' },
  { question: 'Можно попробовать бесплатно?', answer: 'Да. Регистрация, короткий тест и первый персональный план доступны бесплатно. Банковская карта для старта не нужна.' },
]

function requestAuth(intent) {
  // Public event hook for connecting the future sign-in and onboarding API.
  window.dispatchEvent(new CustomEvent('jasno:auth', { detail: { intent } }))
}
</script>

<template>
  <main>
    <section id="top" class="hero-shell">
      <header class="site-header page-width">
        <a class="brand" href="#top" aria-label="Ясно — английский, на главную">
          <span class="brand-mark"><img src="/figma/audio-lines.svg" alt="" /></span>
          <span class="brand-name">ясно</span>
          <span class="brand-caption">английский</span>
        </a>
        <nav class="main-nav" :class="{ 'nav-open': menuOpen }" aria-label="Главное меню">
          <a href="#features">Возможности</a>
          <a href="#how-it-works">Как это работает</a>
          <a href="#questions">Вопросы</a>
        </nav>
        <button class="text-button login-button" type="button" @click="requestAuth('login')">Войти</button>
        <button class="menu-button" type="button" aria-label="Открыть меню" :aria-expanded="menuOpen" @click="menuOpen = !menuOpen">
          <span></span><span></span><span></span>
        </button>
      </header>

      <div class="hero-content page-width">
        <div class="hero-copy">
          <span class="eyebrow-pill">Персональный маршрут к английскому</span>
          <h1>Не просто учите.<br />Понимайте,<br />что учить дальше.</h1>
          <p class="hero-description">Узнайте свои сильные стороны, не забывайте слова и двигайтесь вперёд между занятиями с преподавателем.</p>
          <div class="hero-action">
            <button class="button button-primary" type="button" @click="requestAuth('signup')">
              Начать бесплатно <img src="/figma/arrow-right.svg" alt="" />
            </button>
            <span>Тест за 3 минуты · Без банковской карты</span>
          </div>
          <p class="hero-trust"><img src="/figma/circle-check.svg" alt="" /> Ваш уровень. Ваш темп. Понятный план.</p>
        </div>

        <div class="hero-preview">
          <div class="preview-kicker">МЕНЬШЕ ХАОСА — БОЛЬШЕ ЯСНОСТИ</div>
          <div class="plan-card">
            <div class="plan-topline"><span>ЯСНО / СЕГОДНЯ</span><span class="streak-pill">7 дней подряд</span></div>
            <div class="plan-greeting"><h2>Анна, всё по плану</h2><p>20 минут для вашего английского</p></div>
            <div class="task-list">
              <div v-for="task in tasks" :key="task.title" class="task-row">
                <span class="skill-icon"><img :src="task.icon" alt="" /></span>
                <span class="task-copy"><strong>{{ task.title }}</strong><small>{{ task.note }}</small></span>
                <span class="task-time">{{ task.time }}</span>
              </div>
            </div>
            <div class="focus-callout">
              <img src="/figma/headphones-focus.svg" alt="" />
              <span><strong>Точка роста — аудирование</strong><small>Учимся понимать живую речь</small></span>
            </div>
          </div>
          <div class="preview-stats">
            <div><strong>B1</strong><span>Примерная оценка</span></div>
            <div><strong>20 минут</strong><span>План на каждый день</span></div>
          </div>
        </div>
      </div>

      <div class="principles page-width">
        <span><img src="/figma/sparkles.svg" alt="" /> Все 5 навыков в фокусе</span>
        <span><img src="/figma/sparkles.svg" alt="" /> Слова остаются с вами</span>
        <span><img src="/figma/sparkles.svg" alt="" /> Между уроками есть план</span>
      </div>
    </section>

    <section id="features" class="section page-width features-section">
      <div class="section-heading">
        <span class="eyebrow">УЧИТЬСЯ СТАНОВИТСЯ ПРОЩЕ</span>
        <h2>Меньше «а что дальше?».<br />Больше движения вперёд.</h2>
        <p>Три знакомые трудности. Один понятный маршрут.</p>
      </div>
      <div class="benefit-grid">
        <article v-for="benefit in benefits" :key="benefit.title" class="benefit-card">
          <span class="benefit-icon"><img :src="benefit.icon" alt="" /></span>
          <p class="benefit-quote">{{ benefit.quote }}</p>
          <h3>{{ benefit.title }}</h3>
          <p class="benefit-body">{{ benefit.body }}</p>
          <div class="benefit-result"><span class="eyebrow-pill">{{ benefit.tag }}</span><small>{{ benefit.result }}</small></div>
        </article>
      </div>
    </section>

    <section id="how-it-works" class="product-section">
      <div class="page-width product-inner">
        <div class="how-block">
          <h2>Как это работает</h2>
          <div class="steps-grid">
            <article v-for="(step, index) in steps" :key="step.title" class="step-card">
              <span class="step-number">0{{ index + 1 }}</span>
              <h3>{{ step.title }}</h3>
              <p>{{ step.text }}</p>
            </article>
          </div>
        </div>

        <div class="showcase-block">
          <div class="section-heading">
            <span class="eyebrow">НЕ НАДО ДЕРЖАТЬ ВСЁ В ГОЛОВЕ</span>
            <h2>Ваш следующий шаг<br />уже на экране.</h2>
            <p>План, навыки и повторение связаны друг с другом.</p>
          </div>
          <div class="showcase-grid">
            <div class="showcase-plan plan-card">
              <div class="plan-topline"><span>ЯСНО / СЕГОДНЯ</span><span class="streak-pill">7 дней подряд</span></div>
              <div class="plan-greeting"><h2>Анна, всё по плану</h2><p>20 минут для вашего английского</p></div>
              <div class="task-list">
                <div v-for="task in tasks" :key="`showcase-${task.title}`" class="task-row">
                  <span class="skill-icon"><img :src="task.icon" alt="" /></span>
                  <span class="task-copy"><strong>{{ task.title }}</strong><small>{{ task.note }}</small></span>
                  <span class="task-time">{{ task.time }}</span>
                </div>
              </div>
              <div class="focus-callout"><img src="/figma/headphones-focus.svg" alt="" /><span><strong>Точка роста — аудирование</strong><small>Учимся понимать живую речь</small></span></div>
            </div>
            <div class="skills-card">
              <div class="skills-heading"><h3>Баланс навыков</h3><span>B1</span></div>
              <p>Пример карты после нескольких занятий</p>
              <div v-for="skill in skills" :key="skill.name" class="skill-meter">
                <div><span>{{ skill.name }}</span><span>{{ skill.score }} / 100</span></div>
                <span class="meter-track"><span :style="{ width: `${skill.score}%` }"></span></span>
              </div>
              <p class="skills-note"><img src="/figma/headphones-focus.svg" alt="" /> Сегодня уделим больше внимания аудированию</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="questions" class="faq-section page-width">
      <div class="faq-inner">
        <div class="section-heading">
          <span class="eyebrow">ОСТАЛИСЬ ВОПРОСЫ?</span>
          <h2>Всё по полочкам</h2>
        </div>
        <div class="faq-list">
          <article v-for="(item, index) in questions" :key="item.question" class="faq-item">
            <button class="faq-question" type="button" :aria-expanded="activeQuestion === index" @click="activeQuestion = activeQuestion === index ? -1 : index">
              <span>{{ item.question }}</span>
              <img :src="activeQuestion === index ? '/figma/minus.svg' : '/figma/plus.svg'" alt="" />
            </button>
            <p v-if="activeQuestion === index" class="faq-answer">{{ item.answer }}</p>
          </article>
        </div>
      </div>
    </section>

    <section class="cta-section page-width">
      <div class="cta-card">
        <span class="eyebrow">ПЕРВЫЙ ШАГ — САМЫЙ ВАЖНЫЙ</span>
        <h2>Пусть в английском<br />станет ясно.</h2>
        <p>Узнайте свой уровень и получите план на сегодня.</p>
        <button class="button button-primary" type="button" @click="requestAuth('signup')">Начать бесплатно <img src="/figma/arrow-right.svg" alt="" /></button>
        <small>3 минуты на тест. И вы уже в пути.</small>
      </div>
    </section>

    <footer class="site-footer">
      <div class="page-width footer-main">
        <a class="brand" href="#top" aria-label="Ясно — на главную">
          <span class="brand-mark"><img src="/figma/audio-lines.svg" alt="" /></span><span class="brand-name">ясно</span><span class="brand-caption">английский</span>
        </a>
        <nav class="footer-nav" aria-label="Ссылки в подвале"><a href="#features">О платформе</a><a href="#questions">Поддержка</a><a href="#questions">Вопросы</a></nav>
      </div>
      <div class="page-width footer-legal"><span>© 2026 Ясно. Учитесь в своём темпе.</span><span>Конфиденциальность · Условия использования</span></div>
    </footer>
  </main>
</template>
