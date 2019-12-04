<template>
  <v-container class="grey lighten-5">
    <v-file-input
      label="カード画像"
      accept="image/*"
      :clearable="clearable"
      :value="fileName"
      @change="inputFile"
    ></v-file-input>
    <div>
      <img :src="previewSrc" alt="" />
    </div>
    <v-btn @click="clearFile">Clear File</v-btn>
    <v-textarea
      label="コメント"
      :value="comment"
      @change="inputComment"
    ></v-textarea>
    <v-btn large color="primary" @click="sendForm">Upload File</v-btn>
  </v-container>
</template>

<script>
import { mapState } from 'vuex';

const reader = new FileReader();

export default {
  data() {
    return {
      file: null,
      previewSrc: '',
      clearable: false,
    };
  },
  computed: {
    ...mapState({
      fileName: state => state.form.fileName,
      comment: state => state.form.comment,
    }),
  },
  methods: {
    inputFile: function(e) {
      reader.onload = e => {
        console.log(e);
        this.previewSrc = e.target.result;
      };
      reader.readAsDataURL(e);
      this.file = e;
      this.$store.dispatch('form/inputFileName', e.name);
    },
    clearFile: function() {
      reader.abort();
      this.file = null;
      this.previewSrc = '';
      this.$store.dispatch('form/clearFileName');
    },
    inputComment: function(e) {
      this.$store.dispatch('form/inputComment', e);
    },
    sendForm: function() {
      const params = new FormData();
      params.append('file', this.file);
      this.$store.dispatch('form/sendForm', params);
      this.previewSrc = '';
    },
  },
};
</script>
