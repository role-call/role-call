<template>
  <h1>Barcode Scanner</h1>
<div>
  {{barcodeStore.occupant?.firstName}}
<!--  {{barcodeStore.getOccupant()}}-->
</div>
</template>

<script>
import {useBarcodeStore} from "../store/barcode";
export default {
  name: "HardwareBarcode",
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
          console.log(code);
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

<style scoped>

</style>