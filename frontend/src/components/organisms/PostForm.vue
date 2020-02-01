<template>
  <v-container>
    <v-file-input
      ref="fileInput"
      label="カード画像"
      accept="image/*"
      :clearable="clearable"
      @click="clearFileName"
      @change="inputFile"
    ></v-file-input>
    <div>
      <img :src="previewSrc" alt="" width="300" />
    </div>
    <div>{{ fileName }}</div>
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
    <v-dialog v-model="loading" fullscreen>
      <v-container fluid fill-height class="dialog">
        <v-layout justify-center align-center>
          <v-progress-circular indeterminate color="primary">
          </v-progress-circular>
        </v-layout>
      </v-container>
    </v-dialog>
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
      fileName: '',
      previewSrc: '',
      clearable: false,
      comment: '',
      loading: false,
    };
  },
  mounted() {
    if (this.cardId) {
      API.set('card', this.cardId).then(response => {
        if (response.payload.user.name === this.$store.state.auth.username) {
          const me = this;
          xhr.open(
            'GET',
            process.env.VUE_APP_ROOT_URL + response.payload.file,
            true
          );
          xhr.responseType = 'arraybuffer';
          xhr.onload = function() {
            const arrayBuffer = this.response;
            me.file = new File([arrayBuffer], response.payload.file_name);
          };
          xhr.send();
          this.fileName = response.payload.file_name;
          this.previewSrc = `http://res.cloudinary.com/${process.env.VUE_APP_CLOUDINARY_CLOUD_NAME}/image/upload/${process.env.VUE_APP_CLOUDINARY_IMAGE_PARAMS}/${response.payload.cloudinary_url}`;
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
      this.fileName = e.name;
    },
    clearFile: function() {
      this.file = null;
      this.fileName = '';
      this.previewSrc = '';
      this.$refs.fileInput.lazyValue = '';
    },
    clearFileName: function(e) {
      e.target.value = '';
    },
    post: function() {
      this.loading = true;
      const params = new FormData();
      params.append('file', this.file);
      params.append('file_name', this.fileName);
      params.append('comment', this.comment);
      params.append('dam_id', this.damId);
      params.append('username', this.$store.state.auth.username);
      API.fileUpload('card', params)
        .then(response => {
          if (response.payload.status === 201) {
            this.fileName = '';
            this.previewSrc = '';
            this.comment = '';
            this.$refs.fileInput.lazyValue = '';
          }
        })
        .finally(() => {
          this.loading = false;
        });
    },
    edit: function() {
      this.loading = true;
      const params = new FormData();
      params.append('file', this.file);
      params.append('file_name', this.fileName);
      params.append('comment', this.comment);
      API.fileUpdate('card', this.cardId, params)
        .then(response => {
          if (response.payload.status === 200) {
            this.fileName = '';
            this.previewSrc = '';
            this.comment = '';
            this.$refs.fileInput.lazyValue = '';
          }
        })
        .finally(() => {
          this.loading = false;
        });
    },
  },
};
</script>

<style lang="scss">
.dialog {
  background-color: rgba(255, 255, 255, 0.5);
}
</style>
