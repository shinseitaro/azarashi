import * as API from '../../apis/API';

const card = {
  namespaced: true,
  state: {
    cardList: [],
    cardUser: '',
  },
  mutations: {
    SET_CARD_LIST(state, array) {
      state.cardList = array;
    },
    SET_CARD_USER(state, name) {
      state.cardUser = name;
    },
  },
  actions: {
    getCardList({ commit }, id) {
      API.setQuery('card', 'user', id).then(response => {
        commit('SET_CARD_LIST', response.payload.results);
        commit('SET_CARD_USER', response.payload.results[0].user.name);
      });
    },
  },
  getters: {},
};

export default card;
