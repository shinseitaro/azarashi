<template>
  <v-container class="grey lighten-5">
    <v-file-input
      label="カード画像"
      accept="image/*"
      :clearable="clearable"
      :value="fileName"
      @click="clearFileName"
      @change="inputFile"
    ></v-file-input>
    <div>
      <img :src="previewSrc" alt="" width="300" />
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
      fileName: [],
      previewSrc: '',
      clearable: false,
    };
  },
  mounted() {
    this.$store.dispatch('form/login', true);
  },
  computed: {
    ...mapState({
      comment: state => state.form.comment,
    }),
  },
  methods: {
    inputFile: function(e) {
      reader.onload = e => {
        this.previewSrc = e.target.result;
      };
      reader.readAsDataURL(e);
      this.file = e;
      this.fileName[0] = e.name;
    },
    clearFile: function() {
      this.file = null;
      this.fileName = [];
      this.previewSrc = '';
    },
    clearFileName: function(e) {
      e.target.value = '';
    },
    inputComment: function(e) {
      this.$store.dispatch('form/inputComment', e);
    },
    sendForm: function() {
      const params = new FormData();
      params.append('file', this.file);
      params.append('comment', this.$store.state.form.comment);
      this.$store.dispatch('form/sendForm', params);
      this.fileName = [];
      this.previewSrc = '';
    },
  },
};
</script>
