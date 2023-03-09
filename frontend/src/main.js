

import App from './App.vue'

import { createPinia } from 'pinia'
import {router} from './router'
import {createApp} from "vue";

createApp(App).use(router).use(createPinia()).mount('#app')
