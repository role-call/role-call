<style scoped>
.profile {
  height: 150px;
}
</style>


<template>



  <div class="container text-center">
  <div class="row">
        <div class="col">
     <img v-if="occupantStore.occupant?.picture" v-bind:src="occupantStore.occupant.picture[0].img"
          class="profile"
          >
    </div>
    <div class="col">
      {{ occupantStore.occupant.lastName  }}
    </div>
    <div class="col">
      {{ occupantStore.occupant.firstName  }}
    </div>

  </div>
</div>
</template>
<script setup>

</script>
<script>
import {useOccupantStore} from "@/store/occupantstore";
export default {
  setup() {
    const occupantStore = useOccupantStore();
    return { occupantStore };
  },
  mounted() {
     const occupantStore = useOccupantStore();
    occupantStore?.getOccupant(this.$route.params.installationId,this.$route.params.externalId);
  }
};
</script>
