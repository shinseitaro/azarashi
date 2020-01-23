<template>
  <v-container class="grey lighten-5">
    <v-card class="mx-auto pa-4" max-width="400">
      <v-card-title>ユーザー登録</v-card-title>
      <div class="mx-4">
        <v-text-field
          v-model="username"
          label="user name"
          :rules="[rules.required]"
        ></v-text-field>
        <v-text-field
          v-model="email"
          label="e-mail"
          type="email"
          :rules="[rules.required]"
        ></v-text-field>
        <v-text-field
          v-model="password1"
          label="password"
          hint="最低8文字以上必要です。数字だけのパスワードにはできません。"
          :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
          :rules="[rules.required, rules.min, rules.notNumberOnly]"
          :type="show1 ? 'text' : 'password'"
          @click:append="show1 = !show1"
        ></v-text-field>
        <v-text-field
          v-model="password2"
          label="password（確認用）"
          hint="確認のため、再度パスワードを入力してください。"
          :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
          :rules="[
            rules.required,
            rules.min,
            rules.notNumberOnly,
            rules.passwordMatch,
          ]"
          :type="show2 ? 'text' : 'password'"
          @click:append="show2 = !show2"
        ></v-text-field>
      </div>
      <v-card-actions>
        <v-btn block color="primary" :disabled="disabledBtn" @click="signUp">
          Sign Up
        </v-btn>
      </v-card-actions>
      <div class="mx-4 red--text">
        <p>{{ error }}</p>
      </div>
    </v-card>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      show1: false,
      show2: false,
      username: '',
      email: '',
      password1: '',
      password2: '',
      rules: {
        required: value => !!value || '必須項目です',
        min: value => value.length >= 8 || '8文字以上必要です',
        notNumberOnly: value =>
          !/^\d*$/.test(value) || '数字だけのパスワードにはできません',
        passwordMatch: value =>
          value === this.password1 || 'パスワードが一致しません',
      },
      error: '',
    };
  },
  computed: {
    disabledBtn: function() {
      return (
        this.username === '' ||
        this.email === '' ||
        this.password1 === '' ||
        this.password2 === '' ||
        this.password1 !== this.password2
      );
    },
  },
  methods: {
    signUp: function() {
      const params = new URLSearchParams();
      params.append('username', this.username);
      params.append('email', this.email);
      params.append('password1', this.password1);
      params.append('password2', this.password2);
      axios
        .post(
          process.env.VUE_APP_ROOT_URL + '/rest-auth/registration/',
          params,
          {
            headers: {
              'content-type': 'application/x-www-form-urlencoded',
            },
          }
        )
        .then(() => {
          this.$router.push('check_your_email');
        })
        .catch(error => {
          return (this.error = error.response.data.email.join(''));
        });
    },
  },
};
</script>
