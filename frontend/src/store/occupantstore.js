
import { defineStore } from 'pinia'
import {fetchWrapper} from "@/helpers/fetchwrapper";

export const useOccupantStore = defineStore('useOccupantStore', {
    state: () => ({  occupant: {}, externalId: "", installId:""}),
    actions: {

        async getOccupant(installationId,externalId) {

            const occupantsResp = await fetchWrapper.get(import.meta.env.VITE_API_BASE+"/i/"+installationId+"/occupants/"+externalId);
            console.log(occupantsResp);
            this.occupant =  occupantsResp;
            return occupantsResp;
        },
        async updateOccupant(installationId,externalId) {
          //update occupant here
        },
        chooseInstall(installationId) {
          this.installId = installationId;
        },
        getInstall() {
          return this.installId;
        }
    },

})
