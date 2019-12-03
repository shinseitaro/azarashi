import * as API from '../../apis/API';

const form = {
  namespaced: true,
  state: {
    comment: '',
  },
  mutations: {
    INPUT_COMMENT(state, text) {
      state.comment = text;
    },
    CLEAR_FORM(state) {
      state.comment = '';
    },
  },
  actions: {
    inputComment({ commit }, text) {
      commit('INPUT_COMMENT', text);
    },
    sendForm({ commit }, params) {
      API.fileUpload('card', params).then(() => {
        commit('CLEAR_FORM');
      });
    },
  },
  getters: {},
};

export default form;
