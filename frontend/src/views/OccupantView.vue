<template>
  <div class="home">
      <OccupantDisplayer :installation-id="this.$route.params.installationId" :occupant-id="this.$route.params.externalId"/>
  </div>
</template>
<script>
// @ is an alias to /src
import OccupantDisplayer from "@/components/OccupantDisplayer.vue";
export default {
  name: 'OccupantView',
  components: {

  OccupantDisplayer
  }
}
</script>
