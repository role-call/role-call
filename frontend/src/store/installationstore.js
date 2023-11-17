import { defineStore } from 'pinia';

import {fetchWrapper} from "@/helpers/fetchwrapper";

export const useInstallationStore = defineStore('useInstallationStore', {
    state: () => ({   occupants:[],installations:[], chosenInstallation: '' }),
    actions: {

        async getInstallations() {

            const installationsResp = await fetchWrapper.get(import.meta.env.VITE_API_BASE+"/i/");
            let installations = [];


            installationsResp.forEach(e=>{installations.push({id:e.external_id,name: e.name, selected: false})});
            if (this.chosenInstallation == '') {
              this.chosenInstallation = installations[0].id;
            }
            this.installations = installations;
            return this.installations;
        },
        async getChosenInstallation() {
            return this.chosenInstallation

        },

        async getOccupants() {
          this.occupants = await fetchWrapper.get(import.meta.env.VITE_API_BASE+"/i/"+this.chosenInstallation+"/occupants/");
         return this.occupants;
        }


    },

})
