

import App from './App.vue'

import { createPinia } from 'pinia'
import {router} from './router'
import {createApp} from "vue";
import quasar


createApp(App).use().use(router).use(createPinia()).mount('#app')
