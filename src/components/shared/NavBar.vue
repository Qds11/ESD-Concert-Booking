<template>
  <v-tabs v-model="tab" bg-color="primary" class="navbar">
    <router-link :to="{ path: '/concert' }" class="link-style">

      <v-tab value="one" class="ml-3"><b>TicketPRO</b></v-tab>
    </router-link>
    <!-- <v-tab value="two">Item Two</v-tab> -->
    <v-spacer></v-spacer>
    <v-tab value="three" class="mr-3" v-if="!isLoggedIn">

      <router-link :to="{ path: '/' }" class="link-style">
        Login/ Sign Up
      </router-link>

    </v-tab>
    <v-tab value="three" class="mr-3" v-else @click="signOut">
      Sign Out
    </v-tab>
  </v-tabs>
</template>

<script>

export default {
  name: 'NavBar',
  mounted() {

    // localStorage.setItem("username", 3);

    // localStorage.removeItem('username');
    if(localStorage.getItem('username')){
      this.username = JSON.parse(localStorage.getItem('username'))
      this.isLoggedIn=true
    }

  },

    data() {
      return {
        isLoggedIn: false,
        username: null
      }
  },
  methods: {
    signOut() {
      localStorage.removeItem('username');
      this.isLoggedIn = false
      this.username=null
      this.$router.push('/');
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
