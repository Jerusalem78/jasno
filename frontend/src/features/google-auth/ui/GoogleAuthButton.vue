<script setup>
const emit = defineEmits(['select'])
</script>

<template>
  <button class="google-signin" type="button" @click="emit('select')">
    <img src="https://developers.google.com/static/identity/images/g-logo.png" alt="" />
    <span>Продолжить с Google</span>
  </button>
</template>
