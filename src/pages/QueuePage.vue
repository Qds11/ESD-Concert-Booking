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
                When it is your turn, you will have 10 minutes to book tickets.
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
  import axios from "axios";

  export default {
    name: "QueuePage",
    async created() {
      //this.id = this.$route.params.id
      await this.add_to_queue();
      // await this.get_availability();
      // await this.get_prices();
      // await this.get_recommendation();
    },
    components: {
    },
    data() {
      return {
        // username: "",
        // password: ""
      };
    },
    methods: {
      //post add_to_queue: call this once to queue user regardless whether they actually need to queue
      async add_to_queue() {
        var concert_id = 1; // CHANGE THIS FOR HALL 2
        console.log("concert_id", concert_id);
        try{
          console.log("trying add_to_queue()");

          const response = await axios.post(`http://127.0.0.1:5009/queue`, {concert_id:1});
          console.log("response", response);

          if (response.data.length < 1) { //no data
            console.log("totally not cryin");
          }
          else{
            console.log("add_to_queue() works!");
            // this.hallDetails=response.data;
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
  