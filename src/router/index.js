import { createRouter, createWebHashHistory } from "vue-router";
import TestComponent from '../components/TestComponent.vue'

const routes = [
  {
    path: '/test',
    name: 'TestComponent',
    component: TestComponent
  }

];

const router = createRouter({
  history: createWebHashHistory(),
  routes
});

export default router;