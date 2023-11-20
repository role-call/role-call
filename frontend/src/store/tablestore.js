import {defineStore} from "pinia";
import {fetchWrapper} from "@/helpers/fetchwrapper";

export  const useTableStore =defineStore('useTableStore', {
    state: () => ({  items: [], itemsLength:0}),
    actions: {
        async getOccupants(installation, params) {
          if (!installation ) {
            return 0;
          }
          if (params && params.page==0 ){
            params.page =1;
          }
          var queryString='';
          if (params) {
             queryString = '?'+ new URLSearchParams(params).toString()

            }
          try {
            var buffer = await fetchWrapper.get(import.meta.env.VITE_API_BASE+"/i/"+installation+"/occupants/"+queryString);

          } catch (e) {
            console.log("error")
            console.log(e)
          }
          if (buffer.results) {
            this.items = buffer.results;
            this.itemsLength = buffer.count;
          }
          console.log(buffer)
          return this.itemsLength;
        }
  }
})
