// import * as API from '../../apis/API';

const form = {
  namespaced: true,
  state: {
    loggedIn: false,
  },
  mutations: {
    LOGIN(state, bool) {
      state.loggedIn = bool;
    },
  },
  actions: {
    login({ commit }, bool) {
      commit('LOGIN', bool);
    },
  },
  getters: {},
};

export default form;
