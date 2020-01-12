<template>
  <v-app-bar app dark class="header">
    <div class="d-flex align-center">
      <v-img
        alt="mindam"
        class="shrink pointer"
        contain
        min-width="100"
        src="/img/logo_transparent.png"
        width="150"
        @click="goToTop"
      />
    </div>

    <v-spacer></v-spacer>

    <v-btn v-if="!isLoggedIn" text href="/signup">
      <span class="mr-2">Sign Up</span>
    </v-btn>

    <v-btn v-if="!isLoggedIn" text @click="login">
      <span class="mr-2">Login</span>
    </v-btn>

    <v-btn v-if="isLoggedIn" text @click="goToMyPage">
      <span class="mr-2">My Page</span>
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
    goToTop: function() {
      this.$router.push({ name: 'sitetop' }).catch(error => {
        return { error };
      });
    },
    login: function() {
      this.$router.push({ name: 'login' }).catch(error => {
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
    goToMyPage: function() {
      this.$router
        .push({
          name: 'mypage',
          params: { userId: this.$store.state.auth.userId },
        })
        .catch(error => {
          return { error };
        });
    },
  },
};
</script>

<style lang="scss">
.header {
  background-color: #514f48;
}

.pointer {
  cursor: pointer;
}
</style>
