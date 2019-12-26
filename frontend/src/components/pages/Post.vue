<template>
  <v-app>
    <Header />
    <v-content>
      <PostForm />
    </v-content>
  </v-app>
</template>

<script>
import Header from '../organisms/Header';
import PostForm from '../organisms/PostForm';

export default {
  components: {
    Header,
    PostForm,
  },

  data: () => ({
    //
  }),
};
</script>
