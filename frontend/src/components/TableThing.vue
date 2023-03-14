<script  setup>
import DataTable from 'datatables.net-vue3';
import DataTablesCore from 'datatables.net';
import {useOccupantStore} from "@/store/occupantstore";


DataTable.use(DataTablesCore);

const data = [
  [1, 2],
  [3, 4],
];
</script>
<script>


// const occupantStore = useOccupantStore();


export default {
  name : "TableThing",
  setup() {
// return {occupantStore};
}
}
</script>



<template>
  <DataTable :data="data" class="display">
    <thead>
    <tr>
      <th>A</th>
      <th>B</th>
    </tr>
    </thead>
  </DataTable>
</template>
<style>
@import 'datatables.net-dt';
</style>





