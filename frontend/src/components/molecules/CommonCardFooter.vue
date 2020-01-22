<template>
  <v-card-actions>
    <v-spacer></v-spacer>
    <v-btn @click="goToDamPage">
      <v-icon left>mdi-map-legend</v-icon>ダム詳細
    </v-btn>
    <v-btn @click="goToPostPage">
      <v-icon left>mdi-pencil-plus</v-icon>投稿する
    </v-btn>
  </v-card-actions>
</template>

<script>
export default {
  props: ['damId'],
  methods: {
    goToDamPage: function() {
      this.$router
        .push({ name: 'dam', params: { damId: this.damId } })
        .catch(error => {
          return { error };
        });
    },
    goToPostPage: function() {
      this.$router
        .push({ name: 'post', params: { damId: this.damId } })
        .catch(error => {
          return { error };
        });
    },
  },
};
</script>
