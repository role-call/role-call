<script setup>
import { RouterLink, RouterView } from 'vue-router';
import { useAuthStore } from './store/auth';
const authStore = useAuthStore();
// authStore.getUser().then()
// console.log();
</script>

<template>
  <div class="app-container bg-light">
    <nav v-if="authStore.user" class="navbar navbar-expand navbar-dark bg-dark">
      <div class="navbar-nav">
        <RouterLink to="/" class="nav-item nav-link">Home</RouterLink>
        <RouterLink to="/barcode" class="nav-item nav-link">Wache</RouterLink>
        <a @click="authStore.logout()" class="nav-item nav-link">Logout</a>
      </div>
    </nav>
    <div class="container pt-4 pb-4">
      <RouterView />
    </div>
  </div>
</template>

<style>
/*@import '@/assets/base.css';*/
</style>