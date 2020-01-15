<template>
  <v-container class="grey lighten-5">
    <v-card class="mx-auto pa-4" max-width="400">
      <v-card-title>ログイン</v-card-title>
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
          v-model="password"
          label="password"
          :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
          :rules="[rules.required]"
          :type="show ? 'text' : 'password'"
          @click:append="show = !show"
        ></v-text-field>
      </div>
      <v-card-actions>
        <v-btn block color="primary" :disabled="disabledBtn" @click="login">
          Login
        </v-btn>
      </v-card-actions>
      <div class="mx-4 red--text">
        <p>{{ error }}</p>
      </div>
    </v-card>
    <v-card class="mx-auto my-4 pa-4" max-width="400">
      <v-card-title>SNSでログイン</v-card-title>
      <v-list>
        <v-list-item>
          <v-btn
            block
            dark
            class="github-color"
            @click="authenticate('github')"
          >
            <v-icon left>mdi-github-circle</v-icon> GitHub
          </v-btn>
        </v-list-item>
        <v-list-item>
          <v-btn block dark class="twitter-color">
            <v-icon left>mdi-twitter</v-icon> twitter
          </v-btn>
        </v-list-item>
      </v-list>
    </v-card>
  </v-container>
</template>

<script>
import { mapState } from 'vuex';
import { authMixin } from '../../mixins/social_auth_mixin';

export default {
  mixins: [authMixin],
  data() {
    return {
      show: false,
      username: '',
      email: '',
      password: '',
      rules: {
        required: value => !!value || '必須項目です',
      },
    };
  },
  computed: {
    disabledBtn: function() {
      return this.username === '' || this.email === '' || this.password === '';
    },
    ...mapState({
      error: state => state.auth.error,
    }),
  },
  methods: {
    login: async function() {
      await this.$store.dispatch('auth/logout');
      const params = new URLSearchParams();
      params.append('name', this.username);
      params.append('email', this.email);
      params.append('password', this.password);
      await this.$store.dispatch('auth/login', params);
      this.$store
        .dispatch('auth/update')
        .then(response => {
          if (response.payload.status === 200) {
            if (this.$route.params.damId) {
              this.$router
                .push({
                  name: 'post',
                  params: { damId: this.$route.params.damId },
                })
                .catch(error => {
                  return { error };
                });
            } else {
              this.$router
                .push({
                  name: 'mypage',
                  params: { userId: this.$store.state.auth.userId },
                })
                .catch(error => {
                  return { error };
                });
            }
          }
        })
        .catch(error => {
          return { error };
        });
    },
  },
};
</script>

<style lang="scss">
.github-color {
  background-color: #333333 !important;
}

.twitter-color {
  background-color: #1da1f2 !important;
}
</style>
