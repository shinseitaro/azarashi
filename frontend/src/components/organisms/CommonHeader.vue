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

    <v-btn href="/signup" text>
      <span class="mr-2">Sign Up</span>
    </v-btn>

    <v-btn href="/login" text>
      <span class="mr-2">Login</span>
    </v-btn>

    <v-btn text @click="logout">
      <span class="mr-2">Logout</span>
    </v-btn>
  </v-app-bar>
</template>

<script>
export default {
  methods: {
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
