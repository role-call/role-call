<template>
  <v-form @submit.prevent="logIn">
    <v-text-field v-model="login" label="Username" />

    <v-text-field type="password" v-model="password" label="Password" />
    <v-btn type="submit">Login</v-btn>
  </v-form>
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
