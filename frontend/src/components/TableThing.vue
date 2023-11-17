
<script>


import OccupantDialog from "@/components/OccupantDialog.vue";
import {useInstallationStore} from "@/store/installationstore";
export default {
  name: "TableThing",
  setup() {
    const installationStore = useInstallationStore();
    installationStore.getOccupants();
    return {installationStore};
  },
  mounted() {
  },
  components: {OccupantDialog}


}
</script>


<template>
  <v-card
    class="mx-auto"
    max-width="90%"
  >
    <v-card-title>
      Occupant
    </v-card-title>

    <v-divider></v-divider>

    <v-virtual-scroll
      :items="installationStore.occupants"

      height="1000"
      item-height="48"
    >
      <template v-slot:default="{item}">
        <v-list-item
        >
          <template v-slot:prepend>
            <img v-if="item.picture[0]" v-bind:src="item.picture[0]?.img"
          class="profile" style="{max-width: 200px }"
          >
            <v-icon v-else class="profile"  >mdi-account</v-icon>
          </template>
          <v-list-item-title>
            <router-link
              :to="{name:'detail', params: {installationId: installationStore.chosenInstallation, externalId: item.external_id}}">
              {{ item.firstName }} - {{ item.lastName }}
            </router-link>
          </v-list-item-title>
          <template v-slot:append>
            <OccupantDialog :installation="installationStore.chosenInstallation"  :occupant="item.external_id" />

          </template>
        </v-list-item>
      </template>
    </v-virtual-scroll>
  </v-card>
</template>
<style>
.profile {

  max-width: 200px;
  min-width: 200px;
}
</style>





