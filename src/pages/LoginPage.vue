<template>
  <v-container id="bg" fluid fill-height>
    <v-row align-self="center" class="h-screen">
      <v-col no-gutters cols="6">
        <v-img
          fluid
          :src="require('../assets/concerts/concert4.jpeg')"
          class="img h-screen"
        >
        </v-img>
      </v-col>

      <v-col cols="6" align-self="center" class="pa-5">
        <v-sheet color="black" fluid>
          <v-container>
            <p class="text-h4 mb-10" style="columns: white">
              Welcome to TicketPRO!
            </p>
          </v-container>

          <v-form @submit.prevent>
            <v-text-field
              v-model="username"
              :rules="nameRules"
              label="Enter username"
            ></v-text-field>

            <v-text-field
              v-model="password"
              label="Enter password"
            ></v-text-field>

            <v-row class="mt-9">
              <v-col>
                <SubmitButton action="Sign In" />
              </v-col>

              <v-col>
                <GoogleLogin :callback="callback" />
              </v-col>

              <v-col>
                <SubmitButton action="Register" />
              </v-col>
            </v-row>
          </v-form>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { decodeCredential } from "vue3-google-login";
import { ref } from "vue";
import axios from "axios";

const userEmail = ref({
  email: "",
});
const userName = ref({
  username: "",
});

const errorMsg = ref({
  errorMsg: "",
});

const callback = (response) => {
  // This callback will be triggered when the user selects or login to
  // their Google account from the popup

  const userData = decodeCredential(response.credential);
  console.log("Handle the userData", userData);
  userEmail.value.email = userData.email;
  verifyGmailAccount(userEmail);

  if (errorMsg.value.length == 0) {
    alert(errorMsg.value);
    return;
  } 
  else {
    alert("Welcome " + userName.value + "!");
    this.$router.push('/') 

  }

  async function verifyGmailAccount(userEmail) {
    console.log("entered verify account");

    var email = userEmail._rawValue.email;
    // console.log(email);

    // calls the user microservice to check if email exists in the database
    const path = `http://127.0.0.1:5000/users/${email}`;
    axios
      .get(path)
      .then((res) => {
        console.log(res.data);
        userName.value = res.data.username;
      })
      .catch((error) => {
        errorMsg.value = error.message;
        console.error(error);
      });
  }
};
</script>

<script>
import SubmitButton from "@/components/shared/SubmitButton.vue";

export default {
  name: "LoginPage",

  components: {
    SubmitButton,
  },
  methods: {},
  data() {
    return {
      username: "",
      password: ""
    };
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
