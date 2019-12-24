<template>
  <v-container class="grey lighten-5">
    <v-card class="mx-auto" max-width="400">
      <v-card-title>ユーザー登録</v-card-title>
      <div class="mx-4">
        <v-text-field
          v-model="email"
          label="e-mail"
          :rules="[rules.required]"
        ></v-text-field>
        <v-text-field
          v-model="password1"
          label="password"
          hint="8文字以上"
          :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
          :rules="[rules.required, rules.min]"
          :type="show1 ? 'text' : 'password'"
          @click:append="show1 = !show1"
        ></v-text-field>
        <v-text-field
          v-model="password2"
          label="password（確認）"
          hint="8文字以上"
          :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
          :rules="[rules.required, rules.min, rules.passwordMatch]"
          :type="show2 ? 'text' : 'password'"
          @click:append="show2 = !show2"
        ></v-text-field>
      </div>
      <v-card-actions>
        <v-btn block color="primary" @click="signUp">Sign Up</v-btn>
      </v-card-actions>
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
      email: '',
      password1: '',
      password2: '',
      rules: {
        required: value => !!value || '必須項目です',
        min: value => value.length >= 8 || '8文字以上',
        passwordMatch: value =>
          value === this.password1 || 'パスワードが一致しません',
      },
    };
  },
  methods: {
    signUp: function() {
      axios
        .post(
          process.env.VUE_APP_ROOT_URL + 'rest-auth/registration/',
          {
            email: this.email,
            password1: this.password1,
            password2: this.password2,
          },
          {
            headers: {
              'content-type': 'application/x-www-form-urlencoded',
            },
          }
        )
        .then(response => {
          console.log(response);
        })
        .catch(error => {
          // console.log(error.config);
          return { error };
        });
    },
  },
};
</script>
