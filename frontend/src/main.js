import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import vuetify from './plugins/vuetify';
import VueAuthenticate from 'vue-authenticate';
import VueAxios from 'vue-axios';
import axios from 'axios';

Vue.config.productionTip = false;
Vue.use(VueAxios, axios);
Vue.use(VueAuthenticate, {
  tokenPath: 'token',
  providers: {
    github: {
      clientId: '7f93ca54ce0f48e7b05c',
      redirectUri: 'http://127.0.0.1:8080/',
      url: 'http://127.0.0.1:8000/api/login/social/jwt-pair-user/github/',
    },
  },
});
new Vue({
  router,
  store,
  vuetify,
  render: h => h(App),
}).$mount('#app');
