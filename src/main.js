import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import "material-design-icons-iconfont/dist/material-design-icons.css";
import '@mdi/font/css/materialdesignicons.css';
// import 'material-design-icons/iconfont/material-icons.css';
import vue3GoogleLogin from 'vue3-google-login'


const vuetify = createVuetify({
  components,
  directives,
});


createApp(App).use(router).use(vuetify).use(vue3GoogleLogin, {
  clientId: '836184012743-9ffch79b2b7cpi3d8tedafi0kq9dh8r0.apps.googleusercontent.com'
}).mount('#app')
