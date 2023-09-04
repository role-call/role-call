import { defineStore } from 'pinia';

import {fetchWrapper} from "@/helpers/fetchwrapper";
import {formatter} from "@/helpers/formatter";
export const useInstallationStore = defineStore('useInstallationStore', {
    state: () => ({   occupants:[],installations:[], chosenInstallation: '95d99610-91f4-4321-9ab2-41a7f82e916c' }),
    actions: {

        async getInstallations() {

            const installationsResp = await fetchWrapper.get(import.meta.env.VITE_API_BASE+"/i/");
            let installations = [];


            installationsResp.forEach(e=>{installations.push({id:e.external_id,name: e.name, selected: false})});
            this.installations = installations;
            return this.installations;
        },
        async getChosenInstallation() {
            return this.chosenInstallation

        },

        async getOccupants() {
            const occupantsResp = await fetchWrapper.get(import.meta.env.VITE_API_BASE+"/i/"+this.chosenInstallation+"/occupants/");

            this.occupants = occupantsResp;

            return this.occupants;
        }


    },

})
