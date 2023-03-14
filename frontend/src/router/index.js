import { createRouter, createWebHistory } from 'vue-router';

import { useAuthStore } from '../store/auth';
import  HomeView  from '../views/HomeView.vue';
import  LoginView  from '@/views/LoginView.vue';
import BarcodeView from "@/views/BarcodeView.vue";
export const router = createRouter({
  history: createWebHistory(),
  linkActiveClass: 'active',
  routes: [
    { path: '/', component: HomeView },
    { path: '/login', component: LoginView },
    { path: '/barcode', component: BarcodeView },

  ]
});

router.beforeEach(async (to) => {
  // redirect to login page if not logged in and trying to access a restricted page
  const publicPages = ['/login'];
  const authRequired = !publicPages.includes(to.path);
  const auth = useAuthStore();
  if (authRequired && !auth.user) {
    auth.returnUrl = to.fullPath;
    return '/login';
  }
});
