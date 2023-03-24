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
            <p class="text-h7 mb-5" style="columns: white">
              You are only allowed to purchase a maximum of 10 tickets.
            </p>
          </v-container>

          <v-form @submit.prevent>
            <!-- Singapore Stadium -->

            <div v-if='hallDetails.data==1'>
              <!-- Cat 1 -->
              <v-row>
                <v-col cols="6">
                  <p class="text-h7 mt-5" style="columns: white">
                      Cat 1 (Standing): ${{ticketPrices.cat1_price}}
                    </p>
                </v-col>
                <v-col cols="6">
                  <!-- check if sold out -->
                  <div v-if='ticketAvailability.cat1_avail==0'>
                    <v-select
                      v-model="cat1_quantity"
                      label="Quantity"
                      :items="[0]"
                      disabled
                    ></v-select>
                    <p class="text-h8" style="columns: white; color: red;">
                      Sold out.
                    </p>
                  </div>
                  <!-- NOT sold out -->
                  <div v-else>
                    <v-select
                      v-model="cat1_quantity"
                      label="Quantity"
                      :items="getQuantityList(ticketAvailability.cat1_avail)"
                    ></v-select>
                  </div>
                </v-col>
              </v-row>
            <!-- Cat 2 -->

            <v-row>
                <v-col cols="6">
                  <p class="text-h7 mt-5" style="columns: white">
                      Cat 2: ${{ticketPrices.cat2_price}}
                    </p>
                </v-col>
                <v-col cols="6">
                  <!-- check if sold out -->
                  <div v-if='ticketAvailability.cat2_avail==0'>
                    <v-select
                      v-model="cat2_quantity"
                      label="Quantity"
                      :items="[0]"
                      disabled
                    ></v-select>
                    <p class="text-h8" style="columns: white; color: red;">
                      Sold out.
                    </p>
                  </div>
                  <!-- NOT sold out -->
                  <div v-else>
                    <v-select
                      v-model="cat2_quantity"
                      label="Quantity"
                      :items="getQuantityList(ticketAvailability.cat2_avail)"
                    ></v-select>
                  </div>
                </v-col>
              </v-row>
            <!-- Cat 3 -->
            <v-row>
                <v-col cols="6">
                  <p class="text-h7 mt-5" style="columns: white">
                      Cat 3: ${{ticketPrices.cat3_price}}
                    </p>
                </v-col>
                <v-col cols="6">
                  <!-- check if sold out -->
                  <div v-if='ticketAvailability.cat3_avail==0'>
                    <v-select
                      v-model="cat3_quantity"
                      label="Quantity"
                      :items="[0]"
                      disabled
                    ></v-select>
                    <p class="text-h8" style="columns: white; color: red;">
                      Sold out.
                    </p>
                  </div>
                  <!-- NOT sold out -->
                  <div v-else>
                    <v-select
                      v-model="cat3_quantity"
                      label="Quantity"
                      :items="getQuantityList(ticketAvailability.cat3_avail)"
                    ></v-select>
                  </div>
                </v-col>
              </v-row>
              <!-- Cat 4 -->
              <v-row>
                <v-col cols="6">
                  <p class="text-h7 mt-5" style="columns: white">
                      Cat 3: ${{ticketPrices.cat4_price}}
                    </p>
                </v-col>
                <v-col cols="6">
                  <!-- check if sold out -->
                  <div v-if='ticketAvailability.cat4_avail==0'>
                    <v-select
                      v-model="cat4_quantity"
                      label="Quantity"
                      :items="[0]"
                      disabled
                    ></v-select>
                    <p class="text-h8" style="columns: white; color: red;">
                      Sold out.
                    </p>
                  </div>
                  <!-- NOT sold out -->
                  <div v-else>
                    <v-select
                      v-model="cat4_quantity"
                      label="Quantity"
                      :items="getQuantityList(ticketAvailability.cat4_avail)"
                    ></v-select>
                  </div>
                </v-col>
              </v-row>
            <!-- Cat 5 -->
            <v-row>
                <v-col cols="6">
                  <p class="text-h7 mt-5" style="columns: white">
                      Cat 3: ${{ticketPrices.cat5_price}}
                    </p>
                </v-col>
                <v-col cols="6">
                  <!-- check if sold out -->
                  <div v-if='ticketAvailability.cat5_avail==0'>
                    <v-select
                      v-model="cat5_quantity"
                      label="Quantity"
                      :items="[0]"
                      disabled
                    ></v-select>
                    <p class="text-h8" style="columns: white; color: red;">
                      Sold out.
                    </p>
                  </div>
                  <!-- NOT sold out -->
                  <div v-else>
                    <v-select
                      v-model="cat5_quantity"
                      label="Quantity"
                      :items="getQuantityList(ticketAvailability.cat5_avail)"
                    ></v-select>
                  </div>
                </v-col>
              </v-row>
          </div>

          <!-- Victoria Theatre -->
          <div v-else-if='hallDetails.data==3'>
            <!-- Cat 1 -->
            <v-row>
                <v-col cols="6">
                  <p class="text-h7 mt-5" style="columns: white">
                      Zone A: ${{ticketPrices.cat1_price}}
                    </p>
                </v-col>
                <v-col cols="6">
                  <!-- check if sold out -->
                  <div v-if='ticketAvailability.cat1_avail==0'>
                    <v-select
                      v-model="cat1_quantity"
                      label="Quantity"
                      :items="[0]"
                      disabled
                    ></v-select>
                    <p class="text-h8" style="columns: white; color: red;">
                      Sold out.
                    </p>
                  </div>
                  <!-- NOT sold out -->
                  <div v-else>
                    <v-select
                      v-model="cat1_quantity"
                      label="Quantity"
                      :items="getQuantityList(ticketAvailability.cat1_avail)"
                    ></v-select>
                  </div>
                </v-col>
              </v-row>
            <!-- Cat 2 -->

            <v-row>
                <v-col cols="6">
                  <p class="text-h7 mt-5" style="columns: white">
                    Zone B: ${{ticketPrices.cat2_price}}
                    </p>
                </v-col>
                <v-col cols="6">
                  <!-- check if sold out -->
                  <div v-if='ticketAvailability.cat2_avail==0'>
                    <v-select
                      v-model="cat2_quantity"
                      label="Quantity"
                      :items="[0]"
                      disabled
                    ></v-select>
                    <p class="text-h8" style="columns: white; color: red;">
                      Sold out.
                    </p>
                  </div>
                  <!-- NOT sold out -->
                  <div v-else>
                    <v-select
                      v-model="cat2_quantity"
                      label="Quantity"
                      :items="getQuantityList(ticketAvailability.cat2_avail)"
                    ></v-select>
                  </div>
                </v-col>
              </v-row>
            <!-- Cat 3 -->
            <v-row>
                <v-col cols="6">
                  <p class="text-h7 mt-5" style="columns: white">
                    Zone C: ${{ticketPrices.cat3_price}}
                    </p>
                </v-col>
                <v-col cols="6">
                  <!-- check if sold out -->
                  <div v-if='ticketAvailability.cat3_avail==0'>
                    <v-select
                      v-model="cat3_quantity"
                      label="Quantity"
                      :items="[0]"
                      disabled
                    ></v-select>
                    <p class="text-h8" style="columns: white; color: red;">
                      Sold out.
                    </p>
                  </div>
                  <!-- NOT sold out -->
                  <div v-else>
                    <v-select
                      v-model="cat3_quantity"
                      label="Quantity"
                      :items="getQuantityList(ticketAvailability.cat3_avail)"
                    ></v-select>
                  </div>
                </v-col>
              </v-row>
            </div>
            <div v-else></div>

            <!-- Calculate total amt. -->
              <v-row class="mt-5">
                <v-col>
                  <p class="text-h7 pt-1" style="columns: white">
                    Total amt.: ${{calculateTotalPrice(hallDetails.data)}}
                  </p>
                </v-col>

              <!-- Submit to Payment -->
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
        hallDetails: "",
        ticketAvailability: "",
        ticketPrices: "",
        concert_id: 1, //hardcoded
        cat1_quantity: 0,
        cat2_quantity: 0,
        cat3_quantity: 0,
        cat4_quantity: 0,
        cat5_quantity: 0,
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
    // generate dropdown list based on ticketAvailAmt
    getQuantityList(ticketAvailAmt){
      var itemList=[];
      if (ticketAvailAmt==1){
        itemList=[1];
        return itemList;
      }
      else if (ticketAvailAmt==2){
        itemList=[1, 2];
        return itemList;
      }
      else if (ticketAvailAmt==3){
        itemList=[1, 2, 3];
        return itemList;
      }
      else if (ticketAvailAmt==4){
        itemList=[1, 2, 3, 4];
        return itemList;
      }
      else if (ticketAvailAmt==5){
        itemList=[1, 2, 3, 4, 5];
        return itemList;
      }
      else if (ticketAvailAmt==6){
        itemList=[1, 2, 3, 4, 5, 6];
        return itemList;
      }
      else if (ticketAvailAmt==7){
        itemList=[1, 2, 3, 4, 5, 6, 7];
        return itemList;
      }
      else if (ticketAvailAmt==8){
        itemList=[1, 2, 3, 4, 5, 6, 7, 8];
        return itemList;
      }
      else if (ticketAvailAmt==9){
        itemList=[1, 2, 3, 4, 5, 6, 7, 8, 9];
        return itemList;
      }
      // ticketAvailAmt -> 10 and above
      else {
        itemList=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
        return itemList;
      }
    },
    // calculate Total Price of tickets chosen
    calculateTotalPrice(hall_id){
      var totalPrice=0;

      if (hall_id==1){
        totalPrice = (this.cat1_quantity*this.ticketPrices.cat1_price) + (this.cat2_quantity*this.ticketPrices.cat2_price) + (this.cat3_quantity*this.ticketPrices.cat3_price) + (this.cat4_quantity*this.ticketPrices.cat4_price) + (this.cat5_quantity*this.ticketPrices.cat5_price);
        return totalPrice.toFixed(2);
      }
      else{
        totalPrice = (this.cat1_quantity*this.ticketPrices.cat1_price) + (this.cat2_quantity*this.ticketPrices.cat2_price) + (this.cat3_quantity*this.ticketPrices.cat3_price);
        return totalPrice.toFixed(2);
      }
    }
  
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
