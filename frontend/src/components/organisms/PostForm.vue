<template>
  <v-container class="grey lighten-5">
    <v-file-input
      label="カード画像"
      accept="image/*"
      @change="inputFile"
    ></v-file-input>
    <v-textarea
      label="コメント"
      :value="comment"
      @change="inputComment"
    ></v-textarea>
    <v-btn large color="primary" @click="sendForm">File Upload</v-btn>
  </v-container>
</template>

<script>
import { mapState } from 'vuex';

export default {
  data() {
    return {
      file: null,
    };
  },
  computed: {
    ...mapState({
      comment: state => state.form.comment,
    }),
  },
  methods: {
    inputFile: function(e) {
      this.file = e;
    },
    inputComment: function(e) {
      this.$store.dispatch('form/inputComment', e.target.value);
    },
    sendForm: function() {
      const params = new FormData();
      params.append('file', this.file);
      this.$store.dispatch('form/sendForm', params);
    },
  },
};
</script>
