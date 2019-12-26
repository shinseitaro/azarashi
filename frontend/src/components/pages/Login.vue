<template>
  <v-app>
    <Header />
    <v-content>
      <LoginForm />
    </v-content>
  </v-app>
</template>

<script>
import Header from '../organisms/Header';
import LoginForm from '../organisms/LoginForm';

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
