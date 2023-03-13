import { createRouter, createWebHistory } from "vue-router";
import TestComponent from '../components/TestComponent.vue'

const routes = [
  {
    path: '/test',
    name: 'TestComponent',
    component: TestComponent
  }

];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;