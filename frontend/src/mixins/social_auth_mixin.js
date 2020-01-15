export const authMixin = {
  methods: {
    authenticate: function(provider) {
      this.$auth
        .authenticate(provider, { provider: provider })
        .then(response => {
          console.log(response);
          if (response.data.email != '') {
            localStorage.setItem('token', response.data.token);
            this.$router.push({ name: 'sitetop' });
          }
        })
        .catch(function(error) {
          console.log(error);
        });
    },
  },
};
