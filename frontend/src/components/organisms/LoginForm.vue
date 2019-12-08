<template>
  <v-container class="grey lighten-5">
    <v-btn large color="primary" @click="login">Login</v-btn>
  </v-container>
</template>

<script>
import axios from 'axios';
import oauth from 'axios-oauth-client';

export default {
  methods: {
    login: async function() {
      const getAuthorizationCode = oauth.client(axios.create(), {
        url: 'http://45.77.22.11:8000/auth/convert-token',
        grant_type: 'convert_token',
        client_id: '',
        client_secret: '',
        backend: 'github',
        token: '',
      });
      const auth = await getAuthorizationCode();
      console.log(auth);
    },
  },
};
</script>
