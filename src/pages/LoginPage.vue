<template>
    <v-container id="bg" fluid fill-height>
      <v-row align="center" style="height: 100vh">
        <v-col no-gutters cols="7">
          <v-img fluid :src="require('../assets/concerts/concert4.jpeg')" class="img">
          </v-img>
        </v-col>

      <v-col cols="5">
        <v-sheet color="black" fluid fill-height class="mx-auto">
          <v-form @submit.prevent>
            <v-text-field
              v-model="firstName"
              label="First name"
            ></v-text-field>

              <v-text-field v-model="password" label="password"></v-text-field>

              <v-btn type="submit" block class="mt-2">Submit</v-btn>
            </v-form>
          </v-sheet>

        </v-col>
      </v-row>
    </v-container>
</template>

<script>

export default {
  name: "LoginPage",
  components: {},
  data() {
    return {};
  },
};
</script>

<style>
#bg {
  background-image: linear-gradient(#0d0d33, #01010c, #040311);
  height: 100vh;
  background-repeat: no-repeat;

}

.img {
  height: 100vh;
}

html {
  background-color: black;
}
</style>
