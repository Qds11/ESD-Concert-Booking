<template>
  <v-banner
      lines="four"
      icon="mdi-lock"
      color="deep-purple-accent-4"
      class="my-4"
      v-if="recommended"
    >
      <v-banner-text>
       <h2>Recommended for you!</h2>
     <b>  {{ recommended.concert_name }}</b>
       <br>
       {{ getDateTime(recommended.date_time) }}
       <br>
       <router-link :to="{ path: '/concert/' + recommended.concert_id }" class="link-style">
       <v-btn
       color="orange-lighten-2"
       variant="text"
       >
       Explore
     </v-btn>
   </router-link>
      </v-banner-text>



    </v-banner>
<h1 class="title">Concerts Available</h1>
<!-- <v-img :src="require('../assets/concerts/concert1.jpg')"></v-img> -->
 <v-container
    >
     <v-row
        align="start"
        no-gutters
        style="height: 150px;"
      >
         <v-col  v-for="concert in concerts" :key="concert.id">
<v-card
      class="mx-auto"
      max-width="344"

    >
    <v-img
     :src="require('../assets/concerts/'+ concert.image_path)"

    ></v-img>

    <v-card-title class="word-break">
   {{ concert.concert_name }}

    </v-card-title>

    <v-card-subtitle>
    Date: {{ getDateTime(concert.date_time) }}
    </v-card-subtitle>

    <v-card-subtitle>
    Starting at ${{ concert.price }}
    </v-card-subtitle>

    <v-card-actions>
  <router-link :to="{ path: '/concert/' + concert.concert_id }" class="link-style">
        <v-btn
        color="orange-lighten-2"
        variant="text"
        >
        Explore
      </v-btn>
    </router-link>

      <v-spacer></v-spacer>


    </v-card-actions>

    <!-- <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>

        <v-card-text>
          I'm a thing. But, like most politicians, he promised more than he could deliver. You won't have time for sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape.
        </v-card-text>
      </div>
    </v-expand-transition> -->
  </v-card>
   </v-col>
  </v-row>
  </v-container>
</template>

<script>
   import axios from "axios";
import { API_BASE_URL_NODEJS } from '../config.js';
export default {
  name: 'HomePage',
  //   components: {
  //   NavBar
  // },
  async mounted() {
    this.concerts = await this.getAllConcertData()
    const userId = 1;
    const response = await axios.get(`${API_BASE_URL_NODEJS}/reco/${userId}`);
    this.recommended = response.data[0];
  },
  data() {
    return {
      recommended: null,
      concerts: null,
      show:false
    };
  },
  methods: {
    async getAllConcertData() {
        try {
          const {data} = await axios.get(API_BASE_URL_NODEJS);
          return data;
        } catch (err) {
            console.log(err)
        }
    },
      getDateTime(datetime) {
            const date = new Date(datetime);
            const day = date.getDate().toString().padStart(2, '0'); // get the day of the month (1-31) and pad with leading zeros if necessary
            const month = (date.getMonth() + 1).toString().padStart(2, '0'); // get the month (0-11) and add 1 to get the correct month number, then pad with leading zeros if necessary
            const year = date.getFullYear().toString(); // get the year (4 digits)
            const hours = date.getHours().toString().padStart(2, '0'); // get the hours (0-23) and pad with leading zeros if necessary
            const minutes = date.getMinutes().toString().padStart(2, '0'); // get the minutes (0-59) and pad with leading zeros if necessary
            const formattedDate = `${day}/${month}/${year} at ${hours}:${minutes}`;
            return formattedDate;
        },
  }


}
</script>

<style scoped>
.word-break{
  white-space: initial;
}
.title{
  color:white
}
</style>
