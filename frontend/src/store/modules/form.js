const form = {
  namespaced: true,
  state: {
    comment: '',
  },
  mutations: {
    INPUT_COMMENT(state, text) {
      state.comment = text;
    },
  },
  actions: {
    inputComment({ commit }, text) {
      commit('INPUT_COMMENT', text);
    },
  },
  getters: {},
};

export default form;
