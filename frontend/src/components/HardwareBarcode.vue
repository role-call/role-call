<template>
  <h1>Barcode Scanner</h1>
<div class="container">

  <div class="row">
  <div class="col-md" >
  <img v-if="barcodeStore.occupant?.img" v-bind:src="barcodeStore.occupant?.img"  width="200" height="200">
  </div><div class="col-md"><p>{{barcodeStore.occupant.firstName}}</p><p>{{barcodeStore.occupant.lastName}}</p></div>

    <v-progress-linear v-if="barcodeStore.occupant?.img" :buffer-value="barcodeStore.progress*10" :show-text="false" ></v-progress-linear>
</div></div>

</template>
<script>

import {useBarcodeStore} from "../store/barcode";

export default {
  name: "HardwareBarcode",
  components: {

  },
  setup() {
    const barcodeStore = useBarcodeStore();
    return {barcodeStore};
  },
  mounted() {

    let code = "";
    let reading = false;
    let self = this;
    const barcodeStore = useBarcodeStore();
    window.addEventListener('keypress', e => {
      //usually scanners throw an 'Enter' key at the end of read
      if (e.keyCode === 13) {
        if(code.length > 10) {
          barcodeStore.store(code);
          barcodeStore.getOccupant();
          /// code ready to use
          code = "";
        }
      } else {
        code += e.key; //while this is not an 'enter' it stores the every key
      }

      //run a timeout of 200ms at the first read and clear everything
      if(!reading) {
        reading = true;
        setTimeout(() => {
          code = "";
          reading = false;
        }, 200);  //200 works fine for me but you can adjust it
      }
    });
  }

}
</script>

<style >
</style>
