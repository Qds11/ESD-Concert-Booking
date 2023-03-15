<template>
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
      :src="concert.img"

    ></v-img>

    <v-card-title class="word-break">
   {{ concert.desc }}

    </v-card-title>

    <v-card-subtitle>
    Date: {{ concert.date }}
    </v-card-subtitle>

    <v-card-subtitle>
    Starting at ${{ concert.price }}
    </v-card-subtitle>

    <v-card-actions>
  <router-link :to="{ path: '/concert/' + concert.id }">
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

// import NavBar from '../components/shared/NavBar.vue'
export default {
  name: 'HomePage',
  //   components: {
  //   NavBar
  // },
  data() {
    return {
      recommended: 'txt',
      concerts: [//to be take from db
        { id:1, name: 'txt', title:"TXT Sweet Mirage Tour 2023", date: '21/3/2023',ticketSaleDate:'2023-03-20T14:30:00', price: 168, desc: 'Hottest 4th Gen Kpop Group Finally in Singapore!',img:require('../assets/concerts/concert1.jpg')},
        { id:2, name: 'Mr Cho', title:"Cho Sweet Strings",date: '12/6/2023',ticketSaleDate:'2023-03-23T14:30:00', price: 50, desc: 'Listen to the beautiful violin melodies by the classic Mr Cho', img: require('../assets/concerts/concert2.jpg') },
        { id:3, name: 'Lil Pip', title:"Pip Install FTW", date: '18/5/2023',ticketSaleDate:'2023-03-18T14:30:00', price: 90, desc: 'Come listen to aggressive rap about python at its finest.', img: require('../assets/concerts/concert3.jpg')}
      ]
    };
  },


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
