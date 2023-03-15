<template>
    <v-tabs
      v-model="tab"
      bg-color="primary"
      class="navbar"
    >

      <v-tab value="one" class="ml-3">TicketMaster</v-tab>
      <v-tab value="two">Item Two</v-tab>
      <v-spacer></v-spacer>
      <v-tab value="three" class="mr-3" v-if="isLoggedIn">Login/ Sign Up</v-tab>
      <v-tab value="three" class="mr-3" v-else>
        Login/ Sign Up
    </v-tab>
    </v-tabs>
</template>

<script>

export default {
  name: 'NavBar',
   props: {
    isLoggedIn: Boolean
  }

}
</script>

<style scoped>
.navbar{
    position:absolute;
    top:0;
    width:100vw;
}

</style>
