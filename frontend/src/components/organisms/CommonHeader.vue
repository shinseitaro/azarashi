<template>
  <v-app-bar app color="primary" dark>
    <div class="d-flex align-center">
      <v-img
        alt="Vuetify Logo"
        class="shrink mr-2"
        contain
        src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
        transition="scale-transition"
        width="40"
      />

      <v-img
        alt="Vuetify Name"
        class="shrink mt-1 hidden-sm-and-down"
        contain
        min-width="100"
        src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
        width="100"
      />
    </div>

    <v-spacer></v-spacer>

    <v-btn v-if="!isLoggedIn" href="/signup" text>
      <span class="mr-2">Sign Up</span>
    </v-btn>

    <v-btn v-if="!isLoggedIn" text @click="login">
      <span class="mr-2">Login</span>
    </v-btn>

    <v-btn v-if="isLoggedIn" text @click="logout">
      <span class="mr-2">Logout</span>
    </v-btn>
  </v-app-bar>
</template>

<script>
import { mapState } from 'vuex';

export default {
  computed: {
    ...mapState({
      isLoggedIn: state => state.auth.isLoggedIn,
    }),
  },
  methods: {
    login: function() {
      this.$router
        .push({ name: 'login' })
        .then(response => {
          return { response };
        })
        .catch(error => {
          return { error };
        });
    },
    logout: function() {
      this.$store.dispatch('auth/logout');
      if (this.$route.name !== 'sitetop') {
        this.$router.push({ name: 'sitetop' }).catch(error => {
          return { error };
        });
      }
    },
  },
};
</script>
