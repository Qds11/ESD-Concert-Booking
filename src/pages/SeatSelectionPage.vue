<template>
  <v-container id="bg" fluid fill-height>
    <v-row align-self="center" class="h-screen">
      <v-col no-gutters cols="6">
        <v-img
          fluid
          :src="require('../../src/assets/halls/seating_plan_2.jpg')"
          class="img h-screen"
        >
        </v-img>
      </v-col>

      <v-col cols="6" align-self="center" class="pa-5">
        <v-sheet color="black" fluid>
          <v-container>
            <p class="text-h4 mb-5" style="columns: white">
              Seat Selection
            </p>
          </v-container>
          <v-container>
            <p class="text-h6 mb-5" style="columns: white">
              Recommended Categories: Cat 1 Blink VIP, Cat 2 Standing, Cat 3 Standing, Cat 4 Standing
            </p>
          </v-container>

          <v-form @submit.prevent>
            <v-row>
              <v-col cols="6">
                <!-- <v-btn
                    variant="flat"
                    color="secondary"
                    disabled
                ></v-btn> -->
                <div v-if='concert_id==1'>
                  <p class="text-h7 mt-5" style="columns: white">
                    Cat 1 Blink VIP: {{ticketPrices["cat1_price"]}}
                  </p>
                </div>
                <div v-else></div>
              </v-col>
                <v-col cols="6">
                  <v-select
                  label="Quantity"
                  :items="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
                ></v-select>
                </v-col>
              </v-row>
              <v-row class="mt-5">
                <v-col>
                  <p class="text-h7 pt-1" style="columns: white">
                    Total amt.: $xxx
                  </p>
                </v-col>
                <v-col>
                  <SubmitButton action="Proceed to Payment" />
                </v-col>
            </v-row>
          </v-form>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>



</script>

<script>
import SubmitButton from "@/components/shared/SubmitButton.vue";
import axios from "axios";


export default {
  name: "SeatSelectionPage",
  async created() {
    //this.id = this.$route.params.id
    await this.get_hall();
    await this.get_availability();
    await this.get_prices();

    // find concert with id, if not exist then redirect to homepage
  // this.targetConcert = this.concerts.find((c) => c.id == this.id)
  // //find out if ticket sale is open
  // this.isTicketSaleOpen=this.compareDateTime(this.targetConcert.date)
  },
  components: {
    SubmitButton,
  },
  computed: {
      // hasBooks: function () {
      //     return this.books.length > 0;
      // }
  },
  data() {
      return {
        hallDetails: null,
        ticketAvailability: null,
        ticketPrices: null,
        concert_id: 1

      };
  },
  methods: {
    //get hall_details
    async get_hall() {
      var concert_id = 1;
      console.log("concert_id", concert_id);
      try{
        console.log("trying get_hall()");

        const response = await axios.get(`http://127.0.0.1:5004/hall/${concert_id}`);
        console.log("response", response);

        if (response.data.length < 1) { //no data
          console.log("totally not cryin");
        }
        else{
          console.log("get_hall() works!");
          this.hallDetails=response.data;
        }
      } catch (error) {
        // Errors when calling the service; such as network error, 
        // service offline, etc
        console.log(error);
      }

    },
    //get availability by providing concert_id
    async get_availability() {
      var concert_id = 1;
      console.log("concert_id", concert_id);
      try{
        console.log("trying get_availability()");

        const response = await axios.get(`http://127.0.0.1:5004/avail/${concert_id}`);
        console.log("response", response);

        if (response.data.length < 1) { //no data
          console.log("totally not cryin");
        }
        else{
          console.log("get_availability() works!");
          this.ticketAvailability=response.data;

        }
      } catch (error) {
        // Errors when calling the service; such as network error, 
        // service offline, etc
        console.log(error);
      }

    },
    //get prices by providing concert_id
    async get_prices() {
      var concert_id = 1;
      console.log("concert_id", concert_id);
      try{
        console.log("trying get_prices()");

        const response = await axios.get(`http://127.0.0.1:5004/price/${concert_id}`);
        console.log("response", response);

        if (response.data.length < 1) { //no data
          console.log("totally not cryin");
        }
        else{
          console.log("get_prices() works!");
          this.ticketPrices=response.data;
        }
      } catch (error) {
        // Errors when calling the service; such as network error, 
        // service offline, etc
        console.log(error);
      }

    },
  
  },
};
</script>

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
