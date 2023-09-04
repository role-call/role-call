<template>
  <div class="home">
      <OccupantDisplayer/>
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