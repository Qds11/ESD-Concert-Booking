import { createRouter, createWebHistory } from "vue-router";
import TestComponent from '../components/TestComponent.vue'
import HomePage from "../pages/HomePage.vue";

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

];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;