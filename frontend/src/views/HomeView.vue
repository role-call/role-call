<template>
  <div class="home">
      <TableThing/>
  </div>
</template>

<script>
// @ is an alias to /src
import TableThing from "@/components/TableThing.vue";
export default {
  name: 'HomeView',
  components: {
    TableThing

  }
}
</script>
