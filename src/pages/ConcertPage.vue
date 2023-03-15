<template>

<!-- <v-img :src="require('../assets/concerts/concert1.jpg')"></v-img> -->
 <v-container
    >
<div :class="['text-h2', 'pa-2']">{{ targetConcert.title }}</div>

    <v-img
      :src="targetConcert.img"
    width="500"
    cover
    class="align-center"
    ></v-img>

<div :class="['text-h5', 'pa-2']">

       {{ targetConcert.desc }}
</div>


    <div :class="['text-h6', 'pa-2']">Date: {{ targetConcert.date }}</div>

    <div :class="['text-h6', 'pa-2']">Starting at ${{ targetConcert.price }}</div>
<div>
    <div v-if="!isTicketSaleOpen">
    Ticket Sales Open on {{ getDateTime }}
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


export default {
  name: 'ConcertPage',

  created() {
      this.id = this.$route.params.id
      //find concert with id, if not exist then redirect to homepage
    this.targetConcert = this.concerts.find((c) => c.id == this.id)
      console.log(this.targetConcert)
    //find out if ticket sale is open
    this.isTicketSaleOpen=this.compareDateTime(this.targetConcert.date)

  },
  data() {
    return {
        recommended: 'txt',
        id: null,
        isTicketSaleOpen:false,
         targetConcert:null,
         concerts:  [//to be take from db
        { id:1, name: 'txt', title:"TXT Sweet Mirage Tour 2023", date: '21/3/2023',ticketSaleDate:'2023-03-20T14:30:00', price: 168, desc: 'Hottest 4th Gen Kpop Group Finally in Singapore!',img:require('../assets/concerts/concert1.jpg')},
        { id:2, name: 'Mr Cho', title:"Cho Sweet Strings",date: '12/6/2023',ticketSaleDate:'2023-03-23T14:30:00', price: 50, desc: 'Listen to the beautiful violin melodies by the classic Mr Cho', img: require('../assets/concerts/concert2.jpg') },
        { id:3, name: 'Lil Pip', title:"Pip Install FTW", date: '18/5/2023',ticketSaleDate:'2023-03-18T14:30:00', price: 90, desc: 'Come listen to aggressive rap about python at its finest.', img: require('../assets/concerts/concert3.jpg')}
      ]
    };
    },
    computed: {

        getDateTime() {
            const date = new Date(this.targetConcert.ticketSaleDate);
            const day = date.getDate().toString().padStart(2, '0'); // get the day of the month (1-31) and pad with leading zeros if necessary
            const month = (date.getMonth() + 1).toString().padStart(2, '0'); // get the month (0-11) and add 1 to get the correct month number, then pad with leading zeros if necessary
            const year = date.getFullYear().toString(); // get the year (4 digits)
            const hours = date.getHours().toString().padStart(2, '0'); // get the hours (0-23) and pad with leading zeros if necessary
            const minutes = date.getMinutes().toString().padStart(2, '0'); // get the minutes (0-59) and pad with leading zeros if necessary
            const formattedDate = `${day}/${month}/${year} at ${hours}:${minutes}`;
            return formattedDate;
        }
    },
    methods: {
        compareDateTime(date) {
            const currentDate = new Date(); //current date and time
            const myDate = new Date(date); //date and time to compare
            if (myDate.getTime() < currentDate.getTime()) {
                return true;
            } else {
             return false
            }
        }
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
