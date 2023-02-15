<script  setup>
import DataTable from 'datatables.net-vue3';
import DataTablesCore from 'datatables.net';
import DataTablesLib from 'datatables.net';
import {useOccupantStore} from "@/store/occupantstore";
import 'datatables.net-select';
import 'datatables.net-buttons';
import 'datatables.net-buttons/js/buttons.html5';
import jszip from 'jszip';
import pdfmake from 'pdfmake';


DataTable.use(DataTablesCore);
DataTablesLib.Buttons.jszip(jszip);
DataTablesLib.Buttons.pdfMake(pdfmake);

useOccupantStore().getOccupants();
const data = useOccupantStore().occupants;
</script>
<script>


// const occupantStore = useOccupantStore();


export default {
  name : "TableThing",
  setup() {
    const occupantStore = useOccupantStore();
    return {occupantStore};
  },
  mounted() {

  }
}
</script>



<template>
  <h2>BewohnerInnen Übersicht</h2>
  <DataTable :data="data" class="display">
    <thead>
    <tr>
      <th>Vorname</th>
      <th>Nachname</th>
    </tr>
    </thead>
  </DataTable>
</template>
<style>
@import 'datatables.net-dt';
</style>





