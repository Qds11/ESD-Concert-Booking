<template>
    <v-container id="bg" fluid fill-height>
      <v-row align-self="center" class="h-screen">
        <v-col no-gutters cols="6">
          <v-img fluid :src="require('../assets/concerts/concert4.jpeg')" class="img h-screen">
          </v-img>
        </v-col>

      <v-col cols="5">
        <v-sheet color="black" fluid fill-height class="mx-auto">
          <v-form @submit.prevent>
            <v-text-field
              v-model="firstName"
              label="First name"
            ></v-text-field>

              <v-text-field v-model="password" label="Enter password"></v-text-field>

              <v-row>

                <v-col>
                  <SubmitButton action="Sign In"/>
                </v-col>

                <v-col>
                  <SubmitButton action="Register"/>
                </v-col>
              </v-row>
            
            </v-form>
          </v-sheet>

        </v-col>
      </v-row>
    </v-container>
</template>

<script>
import SubmitButton from '../components/shared/SubmitButton.vue';

export default {
  name: "LoginPage",
  components: {
    SubmitButton 
  },
  data() {
    return {

    };
  },
};
</script>

<style>
#bg {
  background-image: linear-gradient(#0d0d33, #01010c, #040311);
  height: 100vh;
  background-repeat: no-repeat;

}


html {
  background-color: black;
}
</style>
