<template>
  <div class="home">
      <OccupantTable/>
  </div>
</template>

<script>

// @ is an alias to /src
import OccupantTable from "@/components/OccupantTable.vue";
export default {
  name: 'OccupantListView',
  components: {
    OccupantTable,


  }
}
</script>
