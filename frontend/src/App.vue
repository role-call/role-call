<template>
    <v-card>
    <v-layout>
      <navigation-handler v-if=" this.$route.meta?.showMenu"></navigation-handler>
      <v-main >
      <router-view />
        </v-main>
    </v-layout>
  </v-card>
</template>



<script >
  import NavigationHandler from "@/components/NavigationHandler.vue";
  export default {
    components: {
      NavigationHandler
    }
  }
</script>
