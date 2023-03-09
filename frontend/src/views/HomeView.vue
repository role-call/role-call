<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
       <UserGreeter />
    <HardwareBarcode />
  </div>
</template>

<script>
// @ is an alias to /src
import UserGreeter from "@/components/UserGreeter.vue";
import HardwareBarcode from "@/components/HardwareBarcode.vue";
export default {
  name: 'HomeView',
  components: {
    UserGreeter,
    HardwareBarcode
  }
}
</script>
