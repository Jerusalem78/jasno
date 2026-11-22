<script setup>
const props = defineProps({
  href: { type: String, default: '#top' },
  label: { type: String, default: 'Ясно — английский' },
  navigateTo: { type: String, default: '' },
})

const emit = defineEmits(['navigate'])

function handleClick(event) {
  if (!props.navigateTo) return
  event.preventDefault()
  emit('navigate', props.navigateTo)
}
</script>

<template>
  <a class="brand" :href="href" :aria-label="label" @click="handleClick">
    <span class="brand-mark"><img src="/figma/audio-lines.svg" alt="" /></span>
    <span class="brand-name">ясно</span>
    <span class="brand-caption">английский</span>
  </a>
</template>
