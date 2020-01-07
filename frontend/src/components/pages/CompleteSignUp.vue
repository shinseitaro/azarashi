<template>
  <base-layout>
    <v-container>
      <information-text
        text="メールアドレスが確認されました。<br>以下よりログインしてください。"
      />
      <v-btn @click="login">
        <span>Login</span>
      </v-btn>
    </v-container>
  </base-layout>
</template>

<script>
import BaseLayout from '../organisms/BaseLayout';
import InformationText from '../atoms/InformationText';

export default {
  components: {
    BaseLayout,
    InformationText,
  },
  methods: {
    login: function() {
      this.$router
        .push({ name: 'login' })
        .then(response => {
          return { response };
        })
        .catch(error => {
          return { error };
        });
    },
  },
};
</script>
