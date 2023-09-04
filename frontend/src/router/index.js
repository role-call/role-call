import  LoginView  from '@/views/LoginView.vue';
import BarcodeView from "@/views/BarcodeView.vue";
import OccupantView from "@/views/OccupantView.vue";
import HomeView from "@/views/HomeView.vue";
import {createRouter, createWebHistory} from "vue-router";
import {useAuthStore} from "@/store/auth";
export const router = createRouter({
  history: createWebHistory(),
  linkActiveClass: 'active',
  routes: [
    { path: '/', component: HomeView },
    { path: '/login', component: LoginView },
    { path: '/barcode', component: BarcodeView },
  { path: '/i/:installationId/occupant/:externalId', component: OccupantView , name:"detail"},
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
