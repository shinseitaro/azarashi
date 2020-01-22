<template>
  <v-row class="mx-0">
    <v-spacer></v-spacer>
    <v-btn @click="goToEditPostPage">
      <v-icon left>mdi-pencil-outline</v-icon>編集
    </v-btn>
    <v-btn><v-icon left>mdi-delete-forever</v-icon>削除</v-btn>
  </v-row>
</template>

<script>
export default {
  props: ['cardId'],
  methods: {
    goToEditPostPage: function() {
      this.$router
        .push({ name: 'edit_post', params: { cardId: this.cardId } })
        .catch(error => {
          return { error };
        });
    },
  },
};
</script>
