<template>

<!-- <v-img :src="require('../assets/concerts/concert1.jpg')"></v-img> -->
 <v-container
    >
<div :class="['text-h2', 'pa-2']">{{ targetConcert.concert_name }}</div>
    <v-img
    :src="require('../assets/concerts/'+ targetConcert.image_path)"
    width="500"
    cover
    class="align-center"
    ></v-img>

<div :class="['text-h5', 'pa-2']">

       {{ targetConcert.description }}
</div>


    <div :class="['text-h6', 'pa-2']">Date: {{ getDateTime(targetConcert.date_time) }}</div>

    <div :class="['text-h6', 'pa-2']">Starting at ${{ targetConcert.price }}</div>
<div>
    <div v-if="!isTicketSaleOpen">
    Ticket Sales Open on {{ getDateTime(targetConcert.ticket_sale_date_time) }}
    </div>
    <div v-else>
    <v-btn>
        Buy Tickets
    </v-btn>
    </div>
</div>

  </v-container>
</template>

<script>

   import axios from "axios";
export default {
  name: 'ConcertPage',

  async created() {
      this.id = this.$route.params.id
      await this.getConcertById();
      //find concert with id, if not exist then redirect to homepage
    // this.targetConcert = this.concerts.find((c) => c.id == this.id)
    // //find out if ticket sale is open
    // this.isTicketSaleOpen=this.compareDateTime(this.targetConcert.date)

  },
  data() {
    return {
        recommended: 'txt',
        id: null,
        isTicketSaleOpen:false,
         targetConcert:null,
    };
    },
    computed: {

    },
    methods: {
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
        compareDateTime(date) {
            const currentDate = new Date(); //current date and time
            const myDate = new Date(date); //date and time to compare
            if (myDate.getTime() < currentDate.getTime()) {
                return true;
            } else {
             return false
            }
        },
        async getConcertById() {
            try {
                const response = await axios.get(`http://localhost:5005/concert/${this.id}`);
                // console.log("RESPONSE");
                if (response.data.length < 1) {
                this.$router.replace(this.$route.query.redirect || '/');
               }
               this.targetConcert=response.data[0]

            } catch (err) {
                console.log(err)
            }

        },
    }
}
</script>

<style scoped>
.word-break{
  white-space: initial;
}
h1{
  color:white
}
.align-center{
    margin:auto;
}
.v-container{
    color:white
}
</style>
