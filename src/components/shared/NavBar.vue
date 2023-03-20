<template>
  <v-tabs v-model="tab" bg-color="primary" class="navbar">
    <router-link :to="{ path: '/' }" class="link-style">

      <v-tab value="one" class="ml-3"><b>TicketPRO</b></v-tab>
    </router-link>
    <!-- <v-tab value="two">Item Two</v-tab> -->
    <v-spacer></v-spacer>
    <v-tab value="three" class="mr-3" v-if="!isLoggedIn">

      <router-link :to="{ path: '/login' }" class="link-style">
        Login/ Sign Up
      </router-link>

    </v-tab>
    <v-tab value="three" class="mr-3" v-else>
      {{ username }}
    </v-tab>
  </v-tabs>
</template>

<script>

export default {
  name: 'NavBar',
  mounted(){
    if(localStorage.getItem('username')){
      this.username = JSON.parse(localStorage.getItem('username'))
    }

  },
  props: {
    isLoggedIn: {
      type: Boolean,
      default: false
    },
    data() {
      return {
        isLoggedIn: false,
        username: 'test'
      }
    }
  }

}
</script>

<style >
.navbar {
  position: absolute;
  top: 0;
  width: 100vw;
}

.link-style {
  text-decoration: none;
  color: white;
}
</style>
