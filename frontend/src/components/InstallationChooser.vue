<script setup>
import {useInstallationStore} from "@/store/installationstore";
import {useOccupantStore} from "@/store/occupantstore";


const changed = function changed() {
      console.log(installationStore.chosenInstallation);
      installationStore.getOccupants();
    };
const installationStore = useInstallationStore();

</script>
<script>

export  default {
  name: "InstallationChooser",
   mounted() {
    const installationStore = useInstallationStore();
    installationStore.getInstallations();
  }



}
</script>
<template>
<div><v-select v-model="installationStore.chosenInstallation" @update:menu="changed" :items="installationStore.installations" item-value="id" item-title="name" >

</v-select></div>
</template>
