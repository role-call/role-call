import { defineStore } from 'pinia'
import {fetchWrapper} from "@/helpers/fetchwrapper";

export const useBarcodeStore = defineStore('barcode', {
    state: () => ({ barcode: null, occupant: {}, progress: 0 ,max:5, timer: null }),
    actions: {
       async store(barcode) {
           this.barcode = barcode;

        },
        async getOccupant() {
            console.log(this.barcode);
            const user = await fetchWrapper.get("http://localhost:8000/occupanteros/"+ this.barcode);
            this.occupant = user;

            this.occupant["img"] = user.picture[0].img;
            this.progress = 0;
            this.barcode = null;
            this.timer =setInterval(() => {

                this.progress++;
                console.log(this.progress);
                if ( this.progress >= 11) {
                    this.occupant = {};
                    this.progress = 0;
                    clearInterval(this.timer);
                    this.timer = null;
                }

            },1000);
        }
    },

})
