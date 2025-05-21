<template>
  <router-view/>
</template>

<script>
import LoginPage from '@/views/LoginPage.vue'
export default {
  components: { LoginPage }
}
</script>

<style>
body {
  margin: 0;
  font-family: 'Comic Sans MS', cursive, sans-serif;
  background-color: #f2f2f2;
}
</style>
