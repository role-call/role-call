<template>
  <div class="home">
    <HardwareBarcode />
  </div>
</template>

<script>
// @ is an alias to /src

import HardwareBarcode from "@/components/HardwareBarcode.vue";
export default {
  name: 'BarcodeView',
  components: {

    HardwareBarcode
  }
}
</script>
