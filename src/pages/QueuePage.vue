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
                You are now in the queue for <b>{{ concertDetails.concert_name }}</b>.
              </p>
              <p class="text-h5 mb-5" style="columns: white">
                When it is your turn, you will have 10 minutes to book tickets and make payment.
              </p>
            </v-container>
            <v-container>
              <p v-if='(queue_position.queue_position)==1' class="text-h3 mb-4" style="columns: white">
                <!-- {{queue_position.queue_position}} -->
                You're next!
              </p>
              <p v-else class="text-h3 mb-2" style="columns: white">
                {{queue_position.queue_position-1}}
              </p>
              <div v-if='(queue_position.queue_position)!=1'>
                <p v-if='(queue_position.queue_position-1)==1' class="text-h7 mb-5" style="columns: white">
                  person ahead of you
                </p>
                <p v-else class="text-h7 mb-5" style="columns: white">
                  people ahead of you
                </p>
              </div>
<!--               
              <v-progress-linear
                bg-color="deep-purple-lighten-5"
                color="deep-purple-accent-1"
                height="12"
                rounded
                model-value="80"
                striped
              ></v-progress-linear> -->
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
      this.concert_id = this.$route.params.concertid
      this.userid = JSON.parse(localStorage.getItem('userid'))
      //console.log("this.userid",this.userid);

      await this.add_to_queue();
      await this.get_concert();
      await this.get_queue_position();
      this.callRepeatedly(); // start calling queue position repeatedly

      
      // this.getQueuePositionRepeatedly = 
      //   setInterval(function(){
      //     // call your function here
      //     this.call_get_queue_position();
      //     console.log("queue ms called repeatedly");
      //   }, 2000); // -> can change time interval

        // this.getQueuePositionRepeatedly = setInterval(function () {
        //   this.call_get_queue_position();
        //   console.log("queue ms called repeatedly");
        // }, 2000);

      // stop calling
      // clearInterval(this.getQueuePositionRepeatedly);

    },
    components: {
    },
    data() {
      return {
        queue_position: 0,
        concertDetails:"",

      };
    },
    methods: {
      //post add_to_queue: call this once to queue user regardless whether they actually need to queue
      async add_to_queue() {
        try{
          console.log("trying add_to_queue()");

          const response = await axios.post(`http://127.0.0.1:5009/queue`, {concert_id:this.concert_id, user_id:this.userid});
          console.log("response", response);

          if (response.data.length < 1) { //no data
            console.log("totally not cryin");
          }
          else{
            console.log("add_to_queue() works!");
          }
        } catch (error) {
          // Errors when calling the service; such as network error, 
          // service offline, etc
          console.log(error);
        }
      },
      callRepeatedly(){  
        var time = this;
      
        this.getQueuePositionRepeatedly = setInterval(function () {
          time.triggerQueuePositionMS();
          console.log("queue ms called again");
        }, 60000);
      },
      async triggerQueuePositionMS(){
        await this.get_queue_position();
      },
      // get queue position: freqeuently call this to updated queue position
      async get_queue_position() {
        //var queue_id = 10; // QUEUE ID

        try{
          console.log("trying get_queue_position()");

          const response = await axios.get(`http://127.0.0.1:5009/waiting-queue/${this.userid}/${this.concert_id}`);
          console.log("response", response);

          if (response.data.length < 1) { //no data
            console.log("totally not cryin");
          }
          else{
            console.log("get_queue_position() works!");
            this.queue_position=response.data;
            if((this.queue_position.queue_position)==0){
              window.location='/seatSelectionPage/' + this.concert_id;
            }
          }
        } catch (error) {
          // Errors when calling the service; such as network error, 
          // service offline, etc
          console.log(error);
        }
      },
      //get concert
      async get_concert() {
        //console.log("this.concert_id", this.concert_id);
        try{
          console.log("trying get_concert()");

          const response = await axios.get(`http://127.0.0.1:5005/concert/${this.concert_id}`);
          console.log("response", response);

          if (response.data.length < 1) { //no data
            console.log("totally not cryin");
          }
          else{
            console.log("get_concert() works!");
            this.concertDetails=response.data[0];

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
  