<template>
  <v-app>
    <Header />
    <v-content>
      <Information
        text="確認メールを送信しました。<br>メールボックスをご確認いただき、メール本文に記載のアドレスにアクセスしてください。"
      />
    </v-content>
  </v-app>
</template>

<script>
import Header from '../organisms/Header';
import Information from '../atoms/Information';

export default {
  components: {
    Header,
    Information,
  },

  data: () => ({
    //
  }),
};
</script>
