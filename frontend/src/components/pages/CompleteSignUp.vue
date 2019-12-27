<template>
  <v-app>
    <Header />
    <v-content>
      <v-container class="grey lighten-5">
        <Information
          text="メールアドレスが確認されました。<br>以下よりログインしてください。"
        />
        <v-btn href="/login" text>
          <span>Login</span>
        </v-btn>
      </v-container>
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
