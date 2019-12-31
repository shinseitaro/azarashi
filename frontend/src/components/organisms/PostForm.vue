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
    <v-textarea v-model="comment" label="コメント"></v-textarea>
    <v-btn large color="primary" @click="sendForm">Post</v-btn>
  </v-container>
</template>

<script>
import * as API from '../../apis/API';

const reader = new FileReader();

export default {
  data() {
    return {
      file: null,
      fileName: [],
      previewSrc: '',
      clearable: false,
      comment: '',
    };
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
    sendForm: function() {
      const params = new FormData();
      params.append('file', this.file);
      params.append('comment', this.comment);
      API.fileUpload('card', params).then(response => {
        if (response.payload.status === 201) {
          this.fileName = [];
          this.previewSrc = '';
          this.comment = '';
        }
      });
    },
  },
};
</script>
