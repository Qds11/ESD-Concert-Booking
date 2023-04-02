<template>
  <v-container id="bg" fluid fill-height>
    <v-row align-self="center" class="h-screen">
      <v-col cols="8" align-self="center" class="pa-5">
        <v-container>
          <div :style="{ paddingLeft: '55%' }">
            <h1 :style="{ fontSize: '40px', color: 'white' }">
              Checkout
            </h1>
          </div>
        </v-container>
      </v-col>
      <v-container>
        <v-row>
          <v-col cols="6">
            <v-img
              fluid
              :src="require('../assets/payment/bp_concert.png')"
              class="img h-screen"
            ></v-img>
          </v-col>
          <v-col cols="6" align-self="center" class="pa-5">
            <v-sheet color="black" fluid>
              <v-container>
                <p class="text-h5 mb-5" style="columns: white">
                  Blackpink concert (Kpop)
                </p>
                <p class="text-h5 mb-5" style="columns: white">
                  Number of tickets: {{ ticket_quantity }}
                </p>
                <p class="text-h5 mb-5" style="columns: white">
                  Total Price of Tickets: ${{ totalPrice }}
                </p>
              </v-container>
              <v-container>
                <div>
                  <div id="paypal-button-container"></div>
                </div>
 
 
                <!-- peishan i disable this one first ah cos i dunno what this does haha, if u need it just uncomment -->
                <!-- <div>
                <PayPalScriptProvider :options="{ 'client-id': AYX78yVruw2aUiVYzwFdKMlWR9P771QpGLZqTdxbBBlkizAMYYzAP16GK4SPI63L4ih7Nhu9wm9BDpxu }">
                  <PayPalButtons :create-order="createOrder" :on-approve="onApprove" />
                </PayPalScriptProvider>
              </div> -->
              </v-container>
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
    </v-row>
  </v-container>
 </template>
 
 
 <style>
 #bg {
  background-image: linear-gradient(#01002c, #01010c, #040311);
  height: 100vh;
  background-repeat: no-repeat;
 }
 
 
 html {
  background-color: black;
 }
 </style>
 
 
 <script>
 import { loadScript } from "@paypal/paypal-js";
 import axios from "axios";
 
 
 
 
 // i commented out the below cos im using the paypal-js package to make the buttons come out, if u need to enter the client if use the
 // code on top
 
 
 export default {
  name: "PaymentPage",

  async created() {
    this.concert_id = this.$route.params.concertid;
    this.userid = JSON.parse(localStorage.getItem('userid'));

    this.tix_quantity = JSON.parse(localStorage.getItem('tix_quantity'));
    this.totalPrice = JSON.parse(localStorage.getItem('totalPrice'));
    this.timeSec = JSON.parse(localStorage.getItem('timeSec'));

    await this.get_concert();

    this.timeSec = JSON.parse(localStorage.getItem('timeSec'));
    this.seconds(); // start timer immediately, continue from seat selection pg
  },

  data() {
    return {
      paymentStatus: null,
      concert_id:null,
      totalPrice: 0,
      ticket_quantity: 0
 
 
 
 
    };
  },
  methods: {

    seconds() {
      this.timeSec--;
      
      var time = this;
      if (this.timer != null) {
          clearInterval(this.timer);
          this.timer = null;
      }
      this.timer = setInterval(function () {
          if (time.timeSec == 0) { 
            // if time is up
              time.end();
          } else {
              time.timeSec--;
              // store new time every sec
              localStorage.setItem('timeSec', JSON.stringify(time.timeSec));
          }
      }, 1000);
    },
    //if user exceeded 10mins
    async end(){
      clearInterval(this.timer);
      this.timer = null;
      this.timeSec = 0;
      await this.delete_from_queue();
    },
    //DELETE delete_from_queue: seat selection UI call this if user exceed 10mins
    async delete_from_queue() {
      try{
        console.log("trying delete_from_queue()");

        const response = await axios.delete(`http://127.0.0.1:5009/delete-from-queue/${this.userid}/${this.concert_id}`);
        console.log("response", response);

        if (response.data.length < 1) { //no data
          console.log("totally not cryin");
        }
        else{
          console.log("delete_from_queue() works!");
          window.location='/concert/' + this.concert_id; // go to concert pg when time exceeds
        }
      } catch (error) {
        // Errors when calling the service; such as network error, 
        // service offline, etc
        console.log(error);
      }
    },    // Send notification if payment is successful

    // Send notification if payment is successful, check paymentStatus value in data

    async sendNotif(paymentStatus) {
      if (paymentStatus) {
        
        const path = `http://127.0.0.1:5100/sendPaymentNotification/${this.userid}`;
        
        axios
          .get(path)
          .then((res) => {
            console.log(res.data);
          })
          .catch((error) => {
            console.error(error);
          });
      }
    },
  },
  mounted() {
    loadScript({ "client-id": "test" })
      .then((paypal) => {
        console.log(paypal.data);
        paypal
          .Buttons({
            createOrder: function(data, actions) {
        return actions.order.create({
          purchase_units: [{
            amount: {
              value: '20000'
            }
          }],
          application_context: {
            return_url: "https://localhost:8080/PaymentPage/"+this.concert_id, // sets the return URL to the current page
           
          }
        });
      },
      onApprove(data,actions) {
             console.log(data)
             // This function captures the funds from the transaction.
            
             return actions.order.capture({
         commit: true
       })
               // .then((response) => response.json())
               .then((details) => {
                 // This function shows a transaction success message to your buyer.
                 this.paymentStatus = true
                 // this.sendNotif(this.paymentStatus)
                 alert(
                   "Transaction completed by " + details.payer.name.given_name
                 );
                 
                 window.location.href='/BookingStatus/true'


               });
           },
           onCancel: function() {
        // Payment cancelled
        alert('Payment cancelled');
        // Replace with your cancel URL
        window.location.href='/BookingStatus/false'
      },
      onError: function(err) {
        // Payment failed
        console.log(err);
        alert('Payment failed');
        window.location.href = '/BookingStatus/false'; // Replace with your error URL
      }
         })


          .render("#paypal-button-container")
          .catch((error) => {
            console.error("failed to render the PayPal Buttons", error);
          });
      })
      .catch((error) => {
        console.error("failed to load the PayPal JS SDK script", error);
      });
 
 
   
      this.totalPrice=this.$route.params.total_price
      this.ticket_quantity=this.$route.params.ticket_quantity
 
 
     
      localStorage.setItem('paymentStatus', JSON.stringify(this.paymentStatus))
      console.log(this.pa)
 
 
      localStorage.setItem('concert_id', JSON.stringify(this.concert_id))
      this.ticket_quantity=JSON.parse(localStorage.getItem('tix_quantity'))
      this.totalPrice=JSON.parse(localStorage.getItem('totalPrice'))
     
     
  },
   // mounted() {
  //   // Add PayPal script to the document
  //   const script = document.createElement('script')
  //   script.src = 'https://www.paypal.com/sdk/js?client-id=AYX78yVruw2aUiVYzwFdKMlWR9P771QpGLZqTdxbBBlkizAMYYzAP16GK4SPI63L4ih7Nhu9wm9BDpxu&components=buttons'
  //   script.addEventListener('load', () => {
  //     // Render PayPal buttons
  //     paypal.Buttons().render('#paypal-button-container')
  //   })
  //   document.body.appendChild(script)
  // },
 };
 </script>
 