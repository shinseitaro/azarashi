<template>
  <v-app>
    <Header />
    <v-content>
      <PostForm />
    </v-content>
  </v-app>
</template>

<script>
import Header from '../organisms/Header.vue';
import PostForm from '../organisms/PostForm.vue';

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
