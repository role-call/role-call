<template>
  <h1>Barcode Scanner</h1>
<div class="container">

  <div class="row">
  <div class="col-md" >
  <img v-if="barcodeStore.occupant?.img" v-bind:src="barcodeStore.occupant?.img"  width="200" height="200">
  </div><div class="col-md"><span>{{barcodeStore.occupant.firstName}}</span></div>



    <!--  <b-progress :value="barcodeStore.progress" :max="barcodeStore.max" show-progress animated></b-progress>-->
<!--  {{ // barcodeStore.occupant?.img}}-->
<!--  {{barcodeStore.getOccupant()}}-->
  </div></div>
  <div class="progress">
    <div class="progress-bar" ></div>
  </div>
</template>

<script>
//v-bind:aria-valuenow="barcodeStore.progress"
import {useBarcodeStore} from "../store/barcode";
import lv-progressbar from 'lightvue/progressbar';
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
  #progress-bar {
    width: v-bind('barcodeStore.progress');
  }
</style>