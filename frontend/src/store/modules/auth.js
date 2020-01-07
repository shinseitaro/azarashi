import axios from 'axios';

const auth = {
  namespaced: true,
  state: {
    userId: 0,
    username: '',
    isLoggedIn: false,
    error: '',
  },
  mutations: {
    SET_NAME(state, payload) {
      state.userId = payload.pk;
      state.username = payload.name;
      state.isLoggedIn = true;
    },
    CLEAR_NAME(state) {
      state.userId = 0;
      state.username = '';
      state.isLoggedIn = false;
    },
    SET_ERROR(state, error) {
      state.error = error;
    },
  },
  actions: {
    login({ commit }, params) {
      return new Promise(resolve => {
        const payload = axios
          .post(process.env.VUE_APP_ROOT_URL + 'api-token-auth/', params, {
            headers: {
              'content-type': 'application/x-www-form-urlencoded',
            },
          })
          .then(response => {
            commit('SET_ERROR', '');
            localStorage.setItem('token', response.data.token);
            return { payload: response };
          })
          .catch(error => {
            commit('SET_ERROR', error.response.data.non_field_errors.join(''));
            return { error };
          });
        resolve(payload);
      });
    },
    logout({ commit }) {
      localStorage.removeItem('token');
      commit('CLEAR_NAME');
    },
    update({ commit }) {
      const token = localStorage.getItem('token');
      return new Promise(resolve => {
        const payload = axios
          .get(process.env.VUE_APP_ROOT_URL + 'rest-auth/user/', {
            headers: {
              Authorization: 'JWT ' + token,
            },
          })
          .then(response => {
            commit('SET_NAME', response.data);
            return { payload: response };
          })
          .catch(error => {
            return { error };
          });
        resolve(payload);
      });
    },
  },
  getters: {},
};

export default auth;
