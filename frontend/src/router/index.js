import LoginView from '@/views/LoginView.vue';
import BarcodeView from "@/views/BarcodeView.vue";
import OccupantView from "@/views/OccupantView.vue";
import HomeView from "@/views/HomeView.vue";
import {createRouter, createWebHistory} from "vue-router";
import {useAuthStore} from "@/store/auth";
import OccupantListView from "@/views/OccupantListView.vue";

export const router = createRouter({
  history: createWebHistory(),
  linkActiveClass: 'active',
  routes: [
    {
      path: '/',
      name: "main",
      component: HomeView,
      meta: {showMenu: true, inMenu: true, icon: "mdi-account-multiple", title: "Home"}
    },
    {
      path: '/i/:installationId/occupant/',
      name: 'occupantlist',
      component: OccupantListView,
      meta: {showMenu: true, params:"installationId", inMenu: false, icon: "mdi-account-multiple", title: "Occupants"}
    },
    {path: '/login', component: LoginView, name: "login"},
    {
      path: '/barcode',
      name: "barcode",
      component: BarcodeView,
      meta: {inMenu: true, icon: "mdi-star", title: "Barcode"}
    },
    {path: '/i/:installationId/occupant/:externalId', component: OccupantView, name: "detail"},
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
