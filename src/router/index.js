import { createRouter, createWebHistory } from "vue-router";
import TestComponent from '../components/TestComponent.vue'
import HomePage from "../pages/HomePage.vue";
import LoginPage from "../pages/LoginPage.vue"

const routes = [
  {
    path: '/test',
    name: 'TestComponent',
    component: TestComponent
  },
  {
    path: '/',
    name: 'HomePage',
    component: HomePage
  },
  {
    path:'/login',
    name: "LoginPage",
    component: LoginPage
  }

];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;