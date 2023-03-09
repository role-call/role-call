import { defineStore } from 'pinia'
import {fetchWrapper} from "@/helpers/fetchwrapper";

export const useBarcodeStore = defineStore('barcode', {
    state: () => ({ barcode: null, occupant: {} }),
    actions: {
       async store(barcode) {
           this.barcode = barcode;
        },
        async getOccupant() {
            const user = await fetchWrapper.get("http://localhost:8000/occupanteros/");
            console.log(user);
            this.occupant = user[0];
            this.barcode = null;
            setTimeout(() => {
                this.occupant = {};
            },5000);
        }
    },

})
