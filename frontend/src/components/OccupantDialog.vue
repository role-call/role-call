<style scoped>
.profile {
  height: 150px;
}
</style>


<template>

 <v-btn
      color="primary"
    >
      Open Dialog

      <v-dialog
        v-model="dialog"
        activator="parent"
        width="auto"
      >
        <v-card>
          <v-card-text>

      {{ occupantStore.occupant.lastName  }}
    -
      {{ occupantStore.occupant.firstName  }}


          </v-card-text>
          <v-card-actions>
            <v-btn color="primary" block @click="dialog = false">Close Dialog</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-btn>



</template>

<script>
import {useOccupantStore} from "@/store/occupantstore";
import {ref} from "vue";

export default {
  name: "OccupantDialog",
  data: ()=>({

    dialog: false
  }),
  props: ["installation", "occupant"],
  setup(props) {
    const occupantStore = useOccupantStore();
    const installId=ref(props.installation);
    const externalId= ref(props.occupant);
    const dialog = ref(false);
    return { occupantStore,dialog, installId, externalId };
  },
  mounted() {
    console.log(this.externalId);
     const occupantStore = useOccupantStore();
    occupantStore?.getOccupant(this.installId,this.externalId);
  }
};
</script>
