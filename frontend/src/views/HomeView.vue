<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
       <UserGreeter />
      <TableThing/>
  </div>
</template>

<script>
// @ is an alias to /src
import UserGreeter from "@/components/UserGreeter.vue";
import TableThing from "@/components/TableThing.vue";
export default {
  name: 'HomeView',
  components: {
    UserGreeter,
    TableThing

  }
}
</script>
