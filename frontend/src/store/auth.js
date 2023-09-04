import {defineStore} from "pinia";
import {fetchWrapper} from '../helpers/fetchwrapper';
import {router} from '@/router'

export const useAuthStore = defineStore("user", {
    state: () => ({

        user: JSON.parse(localStorage.getItem('user')),
        returnUrl: null
    }),

    actions: {
        // async fetchUser() {
        //     const res = await fetchWrapper("http://localhost:8000/user");
        //
        //     const user = await res.json();
        //     this.user = user;
        // },
        async signUp(login, password) {
            const res = await fetchWrapper(import.meta.env.VITE_API_BASE+"/accounts/register",
                {login, password})
            const user = await res.json()
            this.user = user;
        },
        async signIn(login, password) {
            const user = await fetchWrapper.post(import.meta.env.VITE_API_BASE + "/api/token/", {
                username: login,
                password: password
            });
            user.user = login;
            this.user = user;

            localStorage.setItem('user', JSON.stringify(user));
            router.push(this.returnUrl || '/');
        },
        async logout() {
            this.user = null
            localStorage.setItem('user', null);
            router.push('login');
        }
    },
});
