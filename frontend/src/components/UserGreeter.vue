<template>
  <h2>Welcome, {{ userStore?.user?.user }}</h2>
</template>

<script>


import { useAuthStore } from "../store/auth";
export default {
  setup() {
    const userStore = useAuthStore();
    return { userStore };
  },
};
</script>