<template>
  <v-container id="bg" fluid fill-height>
    <v-row align-self="center" class="h-screen">
      <v-col no-gutters cols="6">
        <p class="text-h5 my-6" style="columns: white; color: white;">
          <b>{{concertDetails.concert_name}}</b>
          <br>
          {{ getDateTime(concertDetails.date_time) }}
          <br>
          {{ hallDetails.hall_name}}

        </p>
        <div v-if='hallDetails.data==1'>
          <v-img
            fluid
            :src="require('../../src/assets/halls/seating_plan_2.jpg')"
            class="img"
          >
          </v-img>
        </div>
        <div v-else-if='hallDetails.data==2'>
          <v-img
            fluid
            :src="require('../../src/assets/halls/f9f85ae0-fb2f-11eb-a641-4e23b81c2c33.jpg')"
            class="img"
          >
          </v-img>
        </div>
        <div v-else></div>
      </v-col>

      <v-col cols="6" align-self="center" class="pa-5">
        <v-sheet color="black" fluid>
          <v-container>
            <p class="text-h4 mb-5" style="columns: white">
              Seat Selection
            </p>
          </v-container>
          <v-container>
            <p class="text-h7 mb-5" style="columns: white">
              Recommended Categories: 
              <br>
              {{showRecommendation(recommendations.recommendation)}}
            </p>
            <v-divider :thickness="2" color="white"></v-divider>
            <p class="text-h7 mb-5 pt-5" style="columns: white">
              You are allowed to purchase a maximum of 10 tickets.
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
                      @update:modelValue="select_seat_popup = true"
                    ></v-select>
                  </div>
                </v-col>
              </v-row>

              <!-- SEATS POPUP -->
              <v-dialog
                v-model="select_seat_popup"
                width="auto"
                persistent
              >
                <v-card>
                  <v-card-text>
                    <v-container>
                      <v-row>
                        <p class="text-h5 mb-5" style="columns: white">
                          Are you ok with these seats?
                        </p>
                      </v-row>
                      <v-row align-self="center">
                        <v-col no-gutters cols="8">
                          <v-img
                            fluid
                            :src="require('../../src/assets/seats/seats_B6_B7.png')"
                            :width="600"
                          >
                          </v-img>
                        </v-col>
                        <v-col no-gutters cols="4">
                          <p class="text-h6 mb-5" style="columns: white">
                            Seats: B6, B7
                          </p>
                        </v-col>
                      </v-row>
                    </v-container>
                  </v-card-text>
                  <v-card-actions>
                    <!-- <v-btn color="primary" block @click="dialog = false">Close Dialog</v-btn> -->
                    <v-spacer></v-spacer>
                    <v-btn
                      color="deep-purple-accent-1"
                      variant="text"
                      @click="select_seat_popup = false"
                    >
                      Reselect
                    </v-btn>
                    <v-btn
                      color="deep-purple-accent-1"
                      variant="text"
                      @click="select_seat_popup = false"
                    >
                      <span style="font-weight: bold;">Select these seats</span>
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
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
          <div v-else-if='hallDetails.data==2'>
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
            </div>
            <div v-else></div>

            <!-- Calculate total amt. -->
            <div v-if='quantityExceeded==true'>
              <p class="text-h7 mb-5 pt-5" style="columns: white; color: red;">
                Ticket quantity cannot exceed 10. Please choose again.
              </p>
            </div>
            <div v-if='quantityZero==true'>
              <p class="text-h7 mb-5 pt-5" style="columns: white; color: red;">
                Please select a ticket.
              </p>
            </div>
              <v-row class="mt-5">
                <v-col>
                  <p class="text-h7 pt-1" style="columns: white">
                    Total Price: <span style="font-weight: bold;">${{calculateTotalPrice(hallDetails.data)}}</span>
                  </p>
                </v-col>

              <!-- Submit to Payment -->
              <v-col>
                <router-link :to="{ path: '/seatSelectionPage/' + id }" class="link-style">
            
              <SubmitButton action="Proceed to Payment" @click="proceed_to_payment()"/>
            </router-link>
                
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
    this.concert_id = this.$route.params.concertid

    await this.get_concert();

    console.log(this.concert_id)

    await this.get_hall();
    await this.get_availability();
    await this.get_prices();
    await this.get_recommendation();

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
        concertDetails: "",
        hallDetails: "",
        ticketAvailability: "",
        ticketPrices: "",
        recommendations: "",
        //concert_id: null, //hardcoded
        cat1_quantity: 0,
        cat2_quantity: 0,
        cat3_quantity: 0,
        cat4_quantity: 0,
        cat5_quantity: 0,
        quantityExceeded: false,
        quantityZero: false,
        select_seat_popup: false,
        totalPrice: 0
      };
  },
  methods: {
    getDateTime(datetime) {
            const date = new Date(datetime);
            const day = date.getDate().toString().padStart(2, '0'); // get the day of the month (1-31) and pad with leading zeros if necessary
            const month = (date.getMonth() + 1).toString().padStart(2, '0'); // get the month (0-11) and add 1 to get the correct month number, then pad with leading zeros if necessary
            const year = date.getFullYear().toString(); // get the year (4 digits)
            const hours = date.getHours().toString().padStart(2, '0'); // get the hours (0-23) and pad with leading zeros if necessary
            const minutes = date.getMinutes().toString().padStart(2, '0'); // get the minutes (0-59) and pad with leading zeros if necessary
            const formattedDate = `${day}/${month}/${year}, ${hours}:${minutes}`;
            return formattedDate;
        },
    //get concert
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
    //get hall_details
    async get_hall() {

      console.log("this.concert_id", this.concert_id);

      var concert_id = this.concert_id; // CHANGE THIS FOR HALL 2
      console.log("concert_id", concert_id);

      try{
        console.log("trying get_hall()");

        const response = await axios.get(`http://127.0.0.1:5004/hall/${this.concert_id}`);
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

      console.log("this.concert_id", this.concert_id);

      var concert_id = this.concert_id; // CHANGE THIS FOR HALL 2
      console.log("concert_id", concert_id);

      try{
        console.log("trying get_availability()");

        const response = await axios.get(`http://127.0.0.1:5004/avail/${this.concert_id}`);
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

      console.log("this.concert_id", this.concert_id);

      var concert_id = this.concert_id; // CHANGE THIS FOR HALL 2
      console.log("concert_id", concert_id);

      try{
        console.log("trying get_prices()");

        const response = await axios.get(`http://127.0.0.1:5004/price/${this.concert_id}`);
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
    //get recommendation
    async get_recommendation() {

      console.log("this.concert_id", this.concert_id);

      var concert_id = this.concert_id;
      console.log("concert_id", concert_id);

      try{
        console.log("trying get_recommendation()");

        const response = await axios.get(`http://127.0.0.1:5003/recommendations/concert/${this.concert_id}`);
        console.log("response", response);

        if (response.data.length < 1) { //no data
          console.log("totally not cryin");
        }
        else{
          console.log("get_recommendation() works!");
          this.recommendations=response.data;
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
        itemList=[0, 1];
        return itemList;
      }
      else if (ticketAvailAmt==2){
        itemList=[0, 1, 2];
        return itemList;
      }
      else if (ticketAvailAmt==3){
        itemList=[0, 1, 2, 3];
        return itemList;
      }
      else if (ticketAvailAmt==4){
        itemList=[0, 1, 2, 3, 4];
        return itemList;
      }
      else if (ticketAvailAmt==5){
        itemList=[0, 1, 2, 3, 4, 5];
        return itemList;
      }
      else if (ticketAvailAmt==6){
        itemList=[0, 1, 2, 3, 4, 5, 6];
        return itemList;
      }
      else if (ticketAvailAmt==7){
        itemList=[0, 1, 2, 3, 4, 5, 6, 7];
        return itemList;
      }
      else if (ticketAvailAmt==8){
        itemList=[0, 1, 2, 3, 4, 5, 6, 7, 8];
        return itemList;
      }
      else if (ticketAvailAmt==9){
        itemList=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
        return itemList;
      }
      // ticketAvailAmt -> 10 and above
      else {
        itemList=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
        return itemList;
      }
    },
    // calculate Total Price of tickets chosen
    calculateTotalPrice(hall_id){
      if (hall_id==1){
        this.totalPrice = (this.cat1_quantity*this.ticketPrices.cat1_price) + (this.cat2_quantity*this.ticketPrices.cat2_price) + (this.cat3_quantity*this.ticketPrices.cat3_price) + (this.cat4_quantity*this.ticketPrices.cat4_price) + (this.cat5_quantity*this.ticketPrices.cat5_price);
        this.totalPrice = this.totalPrice.toFixed(2);
        
        return this.totalPrice
      }
      else{
        this.totalPrice = (this.cat1_quantity*this.ticketPrices.cat1_price) + (this.cat2_quantity*this.ticketPrices.cat2_price) + (this.cat3_quantity*this.ticketPrices.cat3_price);
        this.totalPrice = this.totalPrice.toFixed(2);

        return this.totalPrice
      }
    },
    // display recomm
    showRecommendation(recommendations){
      // console.log("recommendations", recommendations);
      var recommMsg="";
      var catName="";
      var recomm;

      for (recomm in recommendations){
        // console.log("recomm", recomm);
        // console.log("recommendations[recomm]", recommendations[recomm]);
        for (const [key, value] of Object.entries(recommendations[recomm])) {
          // console.log(`${key}: ${value}`);
          
          // Match key with cat name
          if (key=="cat1"){
            catName="Cat 1 (Standing)";
          }
          else if (key=="cat2"){
            catName="Cat 2";
          }
          else if (key=="cat3"){
            catName="Cat 3";
          }
          else if (key=="cat4"){
            catName="Cat 4";
          }
          else if (key=="cat5"){
            catName="Cat 5";
          }
          else{
            catName="Cat Unknown";
          }
          recommMsg+=catName + " - " + value + "\n";
          console.log("recommMsg", recommMsg);
        }
      }
      return recommMsg;

    },
    // check for tix qty exceeded, pass data to payment
    proceed_to_payment() {
      var tix_quantity = this.cat1_quantity + this.cat2_quantity + this.cat3_quantity + this.cat4_quantity + this.cat5_quantity;
      localStorage.setItem('chosen_cat1', JSON.stringify(this.cat1_quantity))
      localStorage.setItem('chosen_cat2', JSON.stringify(this.cat2_quantity))
      localStorage.setItem('chosen_cat3', JSON.stringify(this.cat3_quantity))
      localStorage.setItem('chosen_cat4', JSON.stringify(this.cat4_quantity))
      localStorage.setItem('chosen_cat5', JSON.stringify(this.cat5_quantity))
      localStorage.setItem('concert_id',JSON.stringify(this.concert_id))
      if (tix_quantity > 10) {
        this.quantityExceeded = true;
        //show error message
      }
      // check for tix qty = 0
      else if (tix_quantity == 0) {
        this.quantityZero = true;
        //show error message
      }
      else{
        this.quantityExceeded = false;
        this.quantityZero = false;

        // proceed to payment pg
      }
    }
      
      
  }
  
}
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
