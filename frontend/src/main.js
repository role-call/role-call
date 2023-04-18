

import App from './App.vue'

import { createPinia } from 'pinia'
import {router} from './router'
import {createApp} from "vue";
import KProgress from 'k-progress-v3';


createApp(App).component('k-progress', KProgress).use(router).use(createPinia()).mount('#app')
