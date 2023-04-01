import { createRouter, createWebHistory } from "vue-router";
import TestComponent from '../components/TestComponent.vue'
import HomePage from "../pages/HomePage.vue";
import LoginPage from "../pages/LoginPage.vue"
import ConcertPage from "../pages/ConcertPage.vue";
import BookingStatus from "../pages/BookingStatus.vue";
import QueuePage from "../pages/QueuePage.vue";
import SeatSelectionPage from "../pages/SeatSelectionPage.vue";
import PaymentPage from "../pages/PaymentPage.vue";



const routes = [
  {
    path: "/test",
    name: "TestComponent",
    component: TestComponent,
  },
  {
    path: "/",
    name: "HomePage",
    component: HomePage,
  },
  {
    path: "/login",
    name: "LoginPage",
    component: LoginPage,
  },
  {
    path: "/concert/:id",
    name: "ConcertPage",
    component: ConcertPage,
  },
  {
    path: "/BookingStatus",
    name: "BookingStatus",
    component: BookingStatus,
  },
  {
    path: "/queuePage/:concertid",
    name: "QueuePage",
    component: QueuePage,
  },
  {
    path: "/seatSelectionPage/:concertid",
    name: "SeatSelectionPage",
    component: SeatSelectionPage,
  },
  {
    path: "/PaymentPage",
    name: "PaymentPage",
    component: PaymentPage,
  }


];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;