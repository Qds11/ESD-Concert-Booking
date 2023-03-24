
<template>
  <v-container id="bg" fluid fill-height>
    <v-row align-self="center" class="h-screen">
      <v-col cols="8" align-self="center" class="pa-5">
        <v-container>
          <div :style="{ paddingLeft: '55%' }">
            <h1 :style="{ fontSize: '40px', color: 'white',}">Ticket Details</h1>
          </div>
        </v-container>
      </v-col>
      <v-container>
        <v-row>
          <v-col cols="6">
            <v-img
              fluid
              :src="require('../assets/payment/bp_concert.png')"
              class="img h-screen"
            ></v-img>
          </v-col>
          <v-col cols="6" align-self="center" class="pa-5">
            <v-sheet color="black" fluid>
            <v-container>
              <p class="text-h5 mb-5" style="columns: white">
                Blackpink concert (Kpop)
              </p>
              <p class="text-h5 mb-5" style="columns: white">
                Number of tickets:
              </p>
              <p class="text-h5 mb-5" style="columns: white">
                <!-- Total Price of Tickets: ${{ totalPrice }} -->
              </p>
            </v-container>
            <v-container>
              <div>
                <div id="paypal-button-container"></div>
              </div>
              <div>
                <PayPalScriptProvider :options="{ 'client-id': AYX78yVruw2aUiVYzwFdKMlWR9P771QpGLZqTdxbBBlkizAMYYzAP16GK4SPI63L4ih7Nhu9wm9BDpxu }">
                  <PayPalButtons :create-order="createOrder" :on-approve="onApprove" />
                </PayPalScriptProvider>
              </div>
            </v-container>
          </v-sheet>
          </v-col>
        </v-row>
      </v-container>
    </v-row>
  </v-container>
</template>


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

<script>
export default {
  mounted() {
    // Add PayPal script to the document
    const script = document.createElement('script')
    script.src = 'https://www.paypal.com/sdk/js?client-id=AYX78yVruw2aUiVYzwFdKMlWR9P771QpGLZqTdxbBBlkizAMYYzAP16GK4SPI63L4ih7Nhu9wm9BDpxu&components=buttons'
    script.addEventListener('load', () => {
      // Render PayPal buttons
      paypal.Buttons().render('#paypal-button-container')
    })
    document.body.appendChild(script)
  },
}
</script>