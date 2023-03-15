<template>
<NavBar :isLoggedIn="false"/>
  <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
<router-view></router-view>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import NavBar from './components/shared/NavBar.vue'
export default {
  name: 'App',
  components: {
       NavBar
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  margin-top: 45px;
  background-color:rgb(28, 27, 29) ;
  width:100vw;
  height: 100vh;
}
</style>
