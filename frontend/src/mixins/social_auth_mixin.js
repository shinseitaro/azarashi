import axios from 'axios';

export const authMixin = {
  methods: {
    checkToken: function(provider, redirect) {
      axios
        .post('http://localhost:8000/api/check/', {
          token: localStorage.getItem('vue-authenticate.vueauth_token'),
        })
        .then(response => {
          var path = response.data.status ? true : '/';
          redirect({ path: path });
        })
        .catch(error => {
          console.log(error);
        });
    },
    authenticate: function(provider) {
      console.log(provider);
      this.$auth
        .authenticate('github', { provider: 'github' })
        .then(function(response) {
          console.log(response);
          if (response.data.email === '') {
            window.location = '/';
          }
        })
        .catch(function(error) {
          console.log(error);
        });
    },
  },
};
