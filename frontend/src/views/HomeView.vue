<template>
  <div class="home">
      <InstallationChooser/>
      <TableThing/>
  </div>
</template>

<script>
// @ is an alias to /src
import TableThing from "@/components/TableThing.vue";
import InstallationChooser from "@/components/InstallationChooser.vue";
export default {
  name: 'HomeView',
  components: {
    TableThing,
    InstallationChooser

  }
}
</script>
