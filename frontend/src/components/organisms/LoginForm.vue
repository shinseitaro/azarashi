<template>
  <v-container class="grey lighten-5">
    <v-btn large color="primary" :href="githubLogin">
      Login
    </v-btn>
    <v-btn large color="secondary" @click="login">
      Login2
    </v-btn>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      githubLogin: process.env.VUE_APP_ROOT_URL + 'auth/login/github/',
    };
  },
  methods: {
    login: function() {
      axios
        .get(process.env.VUE_APP_ROOT_URL + 'auth/login/github/')
        .then(response => {
          console.log(response);
          return (location.href = response.request.responseURL);
        })
        .catch(error => {
          // console.log(error.config);
          return { error };
        });
    },
  },
};
</script>
