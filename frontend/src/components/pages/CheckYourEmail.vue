<template>
  <base-layout>
    <v-container>
      <information-text
        text="確認メールを送信しました。<br>メールボックスをご確認いただき、メール本文に記載のアドレスにアクセスしてください。"
      />
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
