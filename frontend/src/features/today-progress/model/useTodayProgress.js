import { computed, onMounted, ref } from 'vue'
import { vocabulary } from '../../../entities/learning/model/demo-data.js'

export function useTodayProgress() {
  const completedTasks = ref([])
  const reviewedWords = ref([])
  const showTranslation = ref(false)
  const goalComplete = ref(false)

  const visibleWords = computed(() => vocabulary.filter((_, index) => !reviewedWords.value.includes(index)))
  const completedCount = computed(() => completedTasks.value.length)
  const nextWord = computed(() => visibleWords.value[0] || vocabulary[0])
  const remainingWords = computed(() => visibleWords.value.length)

  onMounted(() => {
    try {
      completedTasks.value = JSON.parse(localStorage.getItem('jasno:today:completed') || '[]')
      reviewedWords.value = JSON.parse(localStorage.getItem('jasno:today:reviewed') || '[]')
      goalComplete.value = localStorage.getItem('jasno:today:goal') === 'true'
    } catch {
      completedTasks.value = []
      reviewedWords.value = []
    }
  })

  function toggleTask(index) {
    completedTasks.value = completedTasks.value.includes(index)
      ? completedTasks.value.filter((task) => task !== index)
      : [...completedTasks.value, index]
    localStorage.setItem('jasno:today:completed', JSON.stringify(completedTasks.value))
  }

  function markWordReviewed(remembered) {
    const index = vocabulary.indexOf(nextWord.value)
    if (!remembered) {
      showTranslation.value = false
      return
    }
    if (!reviewedWords.value.includes(index)) reviewedWords.value = [...reviewedWords.value, index]
    localStorage.setItem('jasno:today:reviewed', JSON.stringify(reviewedWords.value))
    showTranslation.value = false
  }

  function toggleGoal() {
    goalComplete.value = !goalComplete.value
    localStorage.setItem('jasno:today:goal', String(goalComplete.value))
  }

  return { completedTasks, reviewedWords, showTranslation, goalComplete, completedCount, nextWord, remainingWords, toggleTask, markWordReviewed, toggleGoal }
}
