<template>
  <v-app>
    <Header />
    <v-content>
      <LoginForm />
    </v-content>
  </v-app>
</template>

<script>
import Header from '../organisms/Header.vue';
import LoginForm from '../organisms/LoginForm.vue';

export default {
  components: {
    Header,
    LoginForm,
  },

  data: () => ({
    //
  }),
};
</script>
