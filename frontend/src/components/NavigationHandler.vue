<template>
      <v-navigation-drawer
        expand-on-hover
        rail
      >
        <v-list>
          <v-list-item
            prepend-avatar="https://randomuser.me/api/portraits/women/85.jpg"
            title="christian"
          ></v-list-item>
        </v-list>

        <v-divider></v-divider>

        <v-list density="compact" nav >
          <template  v-for="route in menuItems">
            <v-list-item v-bind="route"></v-list-item>
          </template>
          <v-list-item prepend-icon="mdi-account-multiple" ><InstallationChooser @changedV="changed" /></v-list-item>
          <v-list-item ><v-btn @click="authStore.logout()" color="primary">Logout</v-btn></v-list-item>
        </v-list>
      </v-navigation-drawer>
</template>
<script setup>
import {useAuthStore} from "@/store/auth";
const changed =  async function changed(e) {
};
const authStore = useAuthStore();
</script>
<script>
import InstallationChooser from "@/components/InstallationChooser.vue";
import {useInstallationStore} from "@/store/installationstore";
import {ref} from "vue";


export default {
  name: "NavigationHandler",
  data: ()=>({
    menuItems: [],
    chosen: 0
  }),
  components: {
    InstallationChooser
  },
  setup() {
    const installationStore = useInstallationStore();
    console.log("here");
    return {installationStore};
  },

  mounted() {

    this.buildMenu()

  },
  methods: {

    async buildMenu() {
          const installationStore = useInstallationStore();
          if (installationStore.installations.length < 1){
            await installationStore.getInstallations();
          }
            this.chosen = ref(installationStore.chosenInstallation);
    this.menuItems = this.$router.getRoutes().filter((r) => r.meta.inMenu).map((r) => {
        return {
          name: r.name,
          active: this.$route.name === r.name,
          'prepend-icon': r.meta.icon,
          title: r.meta.title,
          to: {name: r.name}
        }
      });
    console.log(installationStore.chosenInstallation);
      console.log(this.$route);
      if (installationStore.chosenInstallation) {
        console.log(installationStore.chosenInstallation);

      this.menuItems.push({
        name: 'Occupant List',

        active: this.$route.name === 'occupantlist',
        'prepend-icon': 'mdi-star',
        title:'Occupants',
        to: {name: 'occupantlist', params: {installationId: installationStore.chosenInstallation}}

      })
    }

    }
  }
}
</script>

<style scoped>

</style>
