<template>
    <v-container id="bg" fluid fill-height>
      <v-row align-self="center" class="h-screen">
        <v-col no-gutters cols="6">
          <v-img
            fluid
            src="require('../assets/concerts/seating_plan_1.jpg')"
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
              <v-row >
                <v-col cols="6">
                  <p class="text-h7 mt-5" style="columns: white">
                    Cat 1 Blink VIP: $398
                  </p>
                  <p class="text-h7 mt-5" style="columns: white">
                    Cat 2 Standing: $328
                  </p>
                  <p class="text-h7 mt-5" style="columns: white">
                    Cat 3 Standing: $248
                  </p>
                  <p class="text-h7 mt-5" style="columns: white">
                    Cat 4 Standing: $168
                  </p>
                  <p class="text-h7 mt-5" style="columns: white">
                    Cat 5: $328
                  </p>
                  <p class="text-h7 mt-5" style="columns: white">
                    Cat 6: $278
                  </p>
                  <p class="text-h7 mt-5" style="columns: white">
                    Cat 7: $228
                  </p>
                  <p class="text-h7 mt-5" style="columns: white">
                    Cat 8: $208
                  </p>
                  <p class="text-h7 mt-5" style="columns: white">
                    Cat 9: $168
                  </p>
                  <p class="text-h7 mt-5" style="columns: white">
                    Cat 10 (Restricted View): $168
                  </p>
                </v-col>
                <v-col cols="6">
                  <v-select
                    label="Quantity"
                    :items="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
                  ></v-select>
                  <v-select
                    label="Quantity"
                    :items="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
                  ></v-select>
                  <v-select
                    label="Quantity"
                    :items="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
                  ></v-select>
                  <v-select
                    label="Quantity"
                    :items="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
                  ></v-select>
                  <v-select
                    label="Quantity"
                    :items="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
                  ></v-select>
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
  
  export default {
    name: "SeatSelection",
  
    components: {
      SubmitButton,
    },
    methods: {},
    data() {
      return {
        username: "",
        password: ""
      };
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
  