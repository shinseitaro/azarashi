<template>
  <v-container>
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
    <div>{{ fileName[0] }}</div>
    <div class="my-4">
      <v-btn @click="clearFile">Clear File</v-btn>
    </div>
    <v-textarea v-model="comment" label="コメント"></v-textarea>
    <v-btn
      v-if="this.$route.name === 'post'"
      large
      color="primary"
      @click="post"
    >
      Post
    </v-btn>
    <v-btn
      v-if="this.$route.name === 'edit_post'"
      large
      color="primary"
      @click="edit"
    >
      Edit
    </v-btn>
  </v-container>
</template>

<script>
import * as API from '../../apis/API';

const reader = new FileReader();
const xhr = new XMLHttpRequest();

export default {
  props: ['damId', 'cardId'],
  data() {
    return {
      file: null,
      fileName: [],
      previewSrc: '',
      clearable: false,
      comment: '',
    };
  },
  mounted() {
    if (this.cardId) {
      API.set('card', this.cardId).then(response => {
        if (response.payload.user === this.$store.state.auth.userId) {
          xhr.open(
            'GET',
            process.env.VUE_APP_ROOT_URL + response.payload.file,
            true
          );
          xhr.responseType = 'arraybuffer';
          xhr.onload = () => {
            const arrayBuffer = this.response;
            this.file = new File([arrayBuffer], response.payload.file_name);
          };
          xhr.send();
          this.fileName[0] = response.payload.file_name;
          this.previewSrc = response.payload.cloudinary_url;
          this.comment = response.payload.comment;
        } else {
          this.$router.push({ name: 'sitetop' }).catch(error => {
            return { error };
          });
        }
      });
    }
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
    post: function() {
      const params = new FormData();
      params.append('file', this.file);
      params.append('file_name', this.fileName[0]);
      params.append('comment', this.comment);
      params.append('dam_id', this.damId);
      params.append('username', this.$store.state.auth.username);
      API.fileUpload('card', params).then(response => {
        if (response.payload.status === 201) {
          this.fileName = [];
          this.previewSrc = '';
          this.comment = '';
        }
      });
    },
    edit: function() {
      const params = new FormData();
      params.append('file', this.file);
      params.append('file_name', this.fileName[0]);
      params.append('comment', this.comment);
      API.fileUpdate('card', this.cardId, params).then(response => {
        if (response.payload.status === 200) {
          this.fileName = [];
          this.previewSrc = '';
          this.comment = '';
        }
      });
    },
  },
};
</script>
