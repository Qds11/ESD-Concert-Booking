
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
  import axios from "axios";
  export default {

    name: "SuccessPage",
    data() {
    return {
      isSuccessful: false, // Set this to true or false based on whether the booking was successful,
    };
  },
  methods:{
    async updateTicket(concert_id) {
      console.log(concert_id)
      var data = {
          chosen_cat1:JSON.parse(localStorage.getItem('chosen_cat1')),
          chosen_cat2:JSON.parse(localStorage.getItem('chosen_cat2')),
          chosen_cat3:JSON.parse(localStorage.getItem('chosen_cat3')),
          chosen_cat4:JSON.parse(localStorage.getItem('chosen_cat4')),
          chosen_cat5:JSON.parse(localStorage.getItem('chosen_cat5')),
        }
        console.log(data)
      axios.put(`http://127.0.0.1:5004/ticket/update/${concert_id}`, data)
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.log(error);
        });

    },
    
  }
,
    created(){
      this.isSuccessful = this.$route.params.paymentStatus
      console.log(this.isSuccessful)
      console.log(this.isSuccessful)
      if(this.isSuccessful==true){
        var concert_id=JSON.parse(localStorage.getItem('concert_id'))

        this.updateTicket(concert_id)
      }
      
        


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
