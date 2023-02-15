<template>
  <form @submit.prevent="logIn">
    <label>Username</label>
    <input type="text" v-model="login" />
    <label>Password</label>
    <input type="password" v-model="password" />
    <button type="submit">Login</button>
  </form>
</template>

<script>
import { useAuthStore } from "../store/auth";
export default {
  setup() {
    const userStore = useAuthStore();
    return { userStore };
  },
  data() {
    return {
      login: "",
      password: "",
    };
  },
  methods: {
    async logIn() {
      await this.userStore.signIn(this.login, this.password);

    },
  },
};
</script>