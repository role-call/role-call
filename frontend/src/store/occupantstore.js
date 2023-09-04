
import { defineStore } from 'pinia'
import {fetchWrapper} from "@/helpers/fetchwrapper";

export const useOccupantStore = defineStore('useOccupantStore', {
    state: () => ({  occupant: {}, externalId: ""}),
    actions: {

        async getOccupant(installationId,externalId) {
            this.externalId = externalId;
            const occupantsResp = await fetchWrapper.get(import.meta.env.VITE_API_BASE+"/i/"+installationId+"/occupants/"+externalId);
            console.log(occupantsResp);
            this.occupant =  occupantsResp;
        },

    },

})
