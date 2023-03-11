// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAYOQ3kI0T_YeGx_Jmr0w7Cn4LSwxNAXvM",
  authDomain: "esd-concert-booking.firebaseapp.com",
  projectId: "esd-concert-booking",
  storageBucket: "esd-concert-booking.appspot.com",
  messagingSenderId: "810038090009",
  appId: "1:810038090009:web:ab8e59ba386982efa00d88",
  measurementId: "G-KKN5CW2JPW",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
