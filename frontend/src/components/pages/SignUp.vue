<template>
  <v-app>
    <Header />
    <v-content>
      <SignUpForm />
    </v-content>
  </v-app>
</template>

<script>
import Header from '../organisms/Header.vue';
import SignUpForm from '../organisms/SignUpForm';

export default {
  components: {
    Header,
    SignUpForm,
  },

  data: () => ({
    //
  }),
};
</script>
