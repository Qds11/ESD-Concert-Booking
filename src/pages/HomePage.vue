<template>


  <h1 class="title">Concerts Available</h1>
  <!-- <v-img :src="require('../assets/concerts/concert1.jpg')"></v-img> -->
  <v-container>
    <v-row align="start" no-gutters style="height: 150px">
      <v-col v-for="concert in concerts" :key="concert.id">
        <v-card class="mx-auto" max-width="344">
          <v-img :src="require('../assets/concerts/' + concert.image_path)"></v-img>
            <v-chip color="deep-purple-accent-4" class="mt-2" text-color="white"  v-if="recommended == concert.genre">Recommended for you!</v-chip>


          <v-card-title class="word-break">
            {{ concert.concert_name }}
          </v-card-title>

          <v-card-subtitle>
            Date: {{ getDateTime(concert.date_time) }}
          </v-card-subtitle>

          <v-card-subtitle> Starting at ${{ concert.price }} </v-card-subtitle>

          <v-card-actions>
            <router-link :to="{ path: '/concert/' + concert.concert_id }" class="link-style">
              <v-btn color="orange-lighten-2" variant="text"> Explore </v-btn>
            </router-link>

            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import axios from "axios";
  import {
    API_BASE_URL_NODEJS
  } from "../config.js";

  export default {
    name: "HomePage",
    async mounted() {

      this.userid = JSON.parse(localStorage.getItem('username'))
      // this.username = JSON.parse(localStorage.getItem('username'))

      await this.getAllConcertData(this.userid);

      // const userId = 2;
      // const response = await axios.get(`${API_BASE_URL_NODEJS}/reco/${userId}`);
      // this.recommended = response.data[0];
    },
    data() {
      return {
        recommended: null,
        concerts: null,
        show: false,
        userid: null,
        username: ""
      };
    },
    methods: {
      async getAllConcertData() {
        try {
          if (localStorage.getItem('userid')) {
            this.userid = JSON.parse(localStorage.getItem('userid'))
          }
          const response = await axios.get(API_BASE_URL_NODEJS, {
            params: {
              userid: this.userid
            }
          });
          console.log(response);
          this.concerts = response.data.concerts;
          if (response.data.recommended) {
            this.recommended = response.data.recommended.message;
          }
          console.log(this.recommended)
          //return data;
        } catch (err) {
          console.log(err);
        }

      },
      getDateTime(datetime) {
        const date = new Date(datetime);
        const day = date.getDate().toString().padStart(2,
        "0"); // get the day of the month (1-31) and pad with leading zeros if necessary
        const month = (date.getMonth() + 1).toString().padStart(2,
        "0"); // get the month (0-11) and add 1 to get the correct month number, then pad with leading zeros if necessary
        const year = date.getFullYear().toString(); // get the year (4 digits)
        const hours = date.getHours().toString().padStart(2,
        "0"); // get the hours (0-23) and pad with leading zeros if necessary
        const minutes = date.getMinutes().toString().padStart(2,
        "0"); // get the minutes (0-59) and pad with leading zeros if necessary
        const formattedDate = `${day}/${month}/${year} at ${hours}:${minutes}`;
        return formattedDate;
      },
    },

  };
</script>

<style scoped>
  .word-break {
    white-space: initial;
  }

  .title {
    color: white;
  }
</style>