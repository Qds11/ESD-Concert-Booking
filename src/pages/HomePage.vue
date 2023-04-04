<template>


  <h1 class="title">Concerts</h1>
  <!-- <v-img :src="require('../assets/concerts/concert1.jpg')"></v-img> -->
  <v-container>
    <v-row align="start" no-gutters style="height: 150px" class="my-7">
      <v-col cols="12" sm="3" md="4" v-for="concert in concerts" :key="concert.id">
        <v-card class="mx-auto" max-width="344">
          <v-img :src="require('../assets/concerts/' + concert.image_path)"></v-img>
            <v-chip color="deep-purple-accent-4" class="mt-2" text-color="white"  v-if=" recommended !==null && recommended == concert.genre">Recommended for you!</v-chip>


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
       <!-- <v-col v-if="concerts.length % 3 !== 0" :cols="(3 - (concerts.length % 3))"></v-col> -->
    </v-row>
  </v-container>
</template>

<script>
  import axios from "axios";


  export default {
    name: "HomePage",
    async mounted() {

      this.userid = JSON.parse(localStorage.getItem('userid'))

      await this.getAllConcertData(this.userid);
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
         const response = await axios.get(`http://localhost:5005/?userId=${this.userid}`);
          this.concerts = response.data.data.concerts;
          if (response.data.data.recommended) {
            this.recommended = response.data.data.recommended;
          }
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