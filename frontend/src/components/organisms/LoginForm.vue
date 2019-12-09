<template>
  <v-container class="grey lighten-5">
    <v-btn large color="primary" :href="githubLogin" @click="login">
      Login
    </v-btn>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      githubLogin: process.env.VUE_APP_ROOT_URL + 'auth/login/github/',
    };
  },
  methods: {
    login: function() {
      this.$store.dispatch('form/login', true);
    },
  },
};
</script>
