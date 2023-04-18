
import { defineStore } from 'pinia'
import {fetchWrapper} from "@/helpers/fetchwrapper";

export const useOccupantStore = defineStore('useOccupantStore', {
    state: () => ({  occupants: [] }),
    actions: {

        async getOccupants() {
            const occupantsResp = await fetchWrapper.get("http://localhost:8000/occupanteros/");
            let occupants = [];
            console.log(occupantsResp);

            this.occupants =  occupantsResp.forEach(e=>{occupants.push([e.firstName, e.lastName])});
            this.occupants = occupants;
            console.log(this.occupants);
        }
    },

})