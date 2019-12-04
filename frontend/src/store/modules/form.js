import * as API from '../../apis/API';

const form = {
  namespaced: true,
  state: {
    fileName: [],
    comment: '',
  },
  mutations: {
    INPUT_FILENAME(state, file) {
      state.fileName[0] = file;
    },
    INPUT_COMMENT(state, text) {
      state.comment = text;
    },
    CLEAR_FILENAME(state) {
      state.fileName = [];
    },
    CLEAR_FORM(state) {
      state.fileName = [];
      state.comment = '';
    },
  },
  actions: {
    inputFileName({ commit }, file) {
      commit('INPUT_FILENAME', file);
    },
    inputComment({ commit }, text) {
      commit('INPUT_COMMENT', text);
    },
    clearFileName({ commit }) {
      commit('CLEAR_FILENAME');
    },
    sendForm({ commit }, params) {
      API.fileUpload('card', params).then(response => {
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
