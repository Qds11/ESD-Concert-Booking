<template>
    <v-container id="bg" fluid fill-height>
      <v-row align-self="center" class="h-screen">
        <v-col cols="12" align-self="center" class="pa-5">
          <v-sheet color="black" fluid>
            <v-container>
              <p class="text-h3 mb-10" style="columns: white; font-weight: bold">
                TicketPro
              </p>
              <p class="text-h4 mb-5" style="columns: white">
                You are now in the queue for (insert concert).
              </p>
              <p class="text-h5 mb-5" style="columns: white">
                When it is your turn, you will have 10 minutes to enter the ticket booking page.
              </p>
            </v-container>
            <v-container>
              <p class="text-h3 mb-2" style="columns: white">
                2000+
              </p>
              <p class="text-h7 mb-5" style="columns: white">
                people ahead of you
              </p>
              <v-progress-linear
                bg-color="deep-purple-lighten-5"
                color="deep-purple-accent-1"
                height="12"
                rounded
                model-value="40"
                striped
              ></v-progress-linear>
            </v-container>
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script setup>


  
  </script>
  
  <script>
  
  export default {
    name: "LoginPage",
  
    components: {
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
  