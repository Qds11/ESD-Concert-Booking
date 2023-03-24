
<template>

    <v-container class="box">
      <v-layout align-center justify-center class="h-100 align-center justify-center">
        <v-flex xs12 sm8 md6>
          <v-card class="pa-10">
            <v-card-text>
                <v-icon :color="isSuccessful ? 'green' : 'red'" size="48">
              {{ isSuccessful ? 'mdi-check-circle-outline' : 'mdi-alert-circle-outline' }}
            </v-icon>
            <h1 class="text-center mt-3 mb-5">{{ isSuccessful ? 'Success!' : 'Oops, there was an error.' }}</h1>
            <p class="text-center">{{ isSuccessful ? 'Your booking was successful.' : 'Sorry, we were unable to process your booking at this time. Please try again later.' }}</p>
          </v-card-text>
            <v-card-actions>
              <v-btn color="primary" to="/">Back to Home</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </template>
  
  <script>

  export default {

    name: "SuccessPage",
    data() {
    return {
      isSuccessful: null, // Set this to true or false based on whether the booking was successful,
    };
  },
    mounted(){
      this.isSuccessful=JSON.parse(localStorage.getItem('paymentStatus'))


    }
  };
  
  </script>
  
  <style scoped>
  .h-100 {
    height: 100%;
  }
  .box{
    padding-top: 200px;
  }
  </style>
