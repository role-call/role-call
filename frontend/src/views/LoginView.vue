<script setup>
import { Form, Field } from 'vee-validate';
import * as Yup from 'yup';

import { useAuthStore } from '@/store/auth';




</script>
<script>
  import LogIn from "@/components/LogIn.vue";
  export default {
    name: "LogIn",
    components: {
      LogIn
    }
  }
</script>

<template>
  <v-container class="fill-height">
    <v-responsive class="align-center text-center fill-height">
<LogIn/>
    </v-responsive>
  </v-container>
</template>
