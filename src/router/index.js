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
    path: "/queuePage/:concertid/",
    name: "QueuePage",
    component: QueuePage,
  },
  {
    path: "/seatSelectionPage/:concertid",
    name: "SeatSelectionPage",
    component: SeatSelectionPage,
  },
  {
    path: "/PaymentPage/:concertid",
    name: "PaymentPage",
    component: PaymentPage,
  }


];
// Check if user is authorized to access the route
const isAuthorized = () => {
  // Implement your logic to check if the user is authorized
  // For example, check if the user has a valid session token
  // If the user is authorized, return true. Otherwise, return false.
};

// Handle the request to the route
const handleRoute = (route) => {
  if (isAuthorized()) {
    // If user is authorized, show the requested route
    const page = routes[route];
    page.show();
  } else {
    // If user is not authorized, redirect to login page
    window.location.href = '/login';
  }
};
// Call handleRoute with the requested route
handleRoute('/HomePage');

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;