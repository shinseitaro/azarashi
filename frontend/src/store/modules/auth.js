import axios from 'axios';

const auth = {
  namespaced: true,
  state: {
    username: '',
    isLoggedIn: false,
    error: '',
  },
  mutations: {
    SET_NAME(state, name) {
      state.username = name;
      state.isLoggedIn = true;
    },
    CLEAR_NAME(state) {
      state.username = '';
      state.isLoggedIn = false;
    },
    SET_ERROR(state, error) {
      state.error = error;
    },
  },
  actions: {
    login({ dispatch, commit }, params) {
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
            dispatch('update');
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
            commit('SET_NAME', response.data.name);
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
