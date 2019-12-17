import * as API from '../../apis/API';

const form = {
  namespaced: true,
  state: {
    loggedIn: false,
    comment: '',
  },
  mutations: {
    LOGIN(state, bool) {
      state.loggedIn = bool;
    },
    INPUT_COMMENT(state, text) {
      state.comment = text;
    },
    CLEAR_FORM(state) {
      state.comment = '';
    },
  },
  actions: {
    login({ commit }, bool) {
      commit('LOGIN', bool);
    },
    inputComment({ commit }, text) {
      commit('INPUT_COMMENT', text);
    },
    sendForm({ commit, state }, params) {
      API.fileUpload('card', params, state).then(response => {
        console.log(response.payload.status);
        if (response.payload.status === 201) {
          commit('CLEAR_FORM');
        }
      });
    },
  },
  getters: {},
};

export default form;
