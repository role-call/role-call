
import { defineStore } from 'pinia'
import {fetchWrapper} from "@/helpers/fetchwrapper";

export const useOccupantStore = defineStore('useOccupantStore', {
    state: () => ({  occupants: [] }),
    actions: {

        async getOccupants() {
            const occupantsResp = await fetchWrapper.get("http://localhost:8000/occupanteros/");

            console.log(occupantsResp);
            this.occupants =  occupantsResp;
        }
    },

})