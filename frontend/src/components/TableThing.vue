<script  setup>




</script>
<script>

import {useInstallationStore} from "@/store/installationstore";



export default {
  name : "TableThing",
  setup() {
            const installationStore = useInstallationStore();
            installationStore.getOccupants();
            return {installationStore};
  },
  mounted() {
  },


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

      height="320"
      item-height="48"
    >
      <template v-slot:default="{item}" >
        <v-list-item
        >
          <template v-slot:prepend>
            <v-icon class="bg-primary">mdi-account</v-icon>
          </template>
          <v-list-item-title><router-link :to="{name:'detail', params: {installationId: installationStore.chosenInstallation, externalId: item.external_id}}">
            {{ item.firstName }}</router-link></v-list-item-title>
          <template v-slot:append>
            <v-btn
              icon="mdi-pencil"
              size="x-small"
              variant="tonal"
            ></v-btn>
          </template>
        </v-list-item>
      </template>
    </v-virtual-scroll>
  </v-card>
</template>
<style>

</style>





