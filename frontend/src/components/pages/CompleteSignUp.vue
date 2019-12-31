<template>
  <base-layout>
    <v-container>
      <information-text
        text="メールアドレスが確認されました。<br>以下よりログインしてください。"
      />
      <v-btn href="/login" text>
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
};
</script>
