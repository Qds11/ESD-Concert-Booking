<template>
  <v-container id="bg" fluid fill-height>
    <v-row align-self="center" class="h-screen">
      <v-col cols="8" align-self="center" class="pa-5">
        <v-container>
          <div :style="{ paddingLeft: '55%' }">
            <h1 :style="{ fontSize: '40px', color: 'white' }">
              Ticket Details
            </h1>
          </div>
        </v-container>
      </v-col>
      <v-col cols="4" align-self="center" class="pa-5">
        <div class="timer">
          {{min}}:{{sec}}
        </div>
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
                  Concert Name:
                  {{ concertDetails.concert_name }}
                </p>
                <p class="text-h5 mb-5" style="columns: white">
                  Number of tickets: 
                  {{ this.tix_quantity }}
                </p>
                <p class="text-h5 mb-5" style="columns: white">
                  Total Price: 
                  ${{ this.totalPrice }}
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

.timer {
      color: white;
      font-size: 2rem;
      font-weight: bolder;
      text-align: center;
      margin: 15px 0;
    }
</style>

<script>
import { loadScript } from "@paypal/paypal-js";
import axios from "axios";

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
      concertDetails: "",
      hallDetails: "",
      ticketAvailability: "",
      ticketPrices: "",
      totalPrice: 0,
      paymentStatus: false,
      timeSec: 5, // timer duration
    };
  },
  computed: {
      min() {
        return String(Math.floor(this.timeSec/60)).padStart(2, '0');
      },
      sec() {
        return String(this.timeSec%60).padStart(2, '0');
      },
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
    },
    // Send notification if payment is successful
    async sendNotif(paymentStatus) {
      if (paymentStatus) {
        const path = `http://127.0.0.1:5100/testing`;
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
    async get_concert() {
        //console.log("this.concert_id", this.concert_id);
        try{
          console.log("trying get_concert()");

          const response = await axios.get(`http://127.0.0.1:5005/concert/${this.concert_id}`);
          console.log("response", response);

          if (response.data.length < 1) { //no data
            console.log("totally not cryin");
          }
          else{
            console.log("get_concert() works!");
            this.concertDetails=response.data[0];

          }
        } catch (error) {
          // Errors when calling the service; such as network error, 
          // service offline, etc
          console.log(error);
        }

      },
  },
  mounted() {
    loadScript({ "client-id": "test" })
      .then((paypal) => {
        console.log(paypal.data);
        paypal
          .Buttons({
            onApprove: (data) => {
              console.log(data);
              // Capture the funds from the transaction
              return fetch("/my-server/capture-paypal-order", {
                method: "POST",
              })
                .then((response) => response.json())
                .then((details) => {
                  // Show a transaction success message to the buyer
                  this.paymentStatus = true;
                  this.sendNotif(this.paymentStatus);
                  alert(
                    "Transaction completed by " +
                      details.payer.name.given_name
                  );
                });
            },
          })
          .render("#paypal-button-container")
          .catch((error) => {
            console.error("Failed to render the PayPal buttons", error);
          });
      })
      .catch((error) => {
        console.error("Failed to load the PayPal JS SDK script", error);
      });

    localStorage.setItem("paymentStatus", JSON.stringify(this.paymentStatus));
  },
};
</script>
