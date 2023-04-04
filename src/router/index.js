import { createRouter, createWebHistory } from "vue-router";
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
    path: "/",
    name: "LoginPage",
    component: LoginPage,
  },
  {
    path: "/concert/:id",
    name: "ConcertPage",
    component: ConcertPage,
  },
  {
    path: "/BookingStatus/:paymentStatus",
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
    path: "/PaymentPage/:concertid",
    name: "PaymentPage",
    component: PaymentPage,
  }


];


const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach(async (to, from, next) => {
  var username = JSON.parse(localStorage.getItem('username'))

  if (
    // make sure the user is not authenticated (they haven't logged in)
    !username &&
    // Avoid an infinite redirect
    to.name !== 'LoginPage'
  ) {
    // redirect the user to the login page
    next({ name: 'LoginPage' })
  } else {
    // allow the user to access the destination route
    next()
  }
})

export default router;