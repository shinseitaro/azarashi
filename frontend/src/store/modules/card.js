import * as API from '../../apis/API';

const card = {
  namespaced: true,
  state: {
    cardList: [],
    cardUser: '',
    cardItem: {},
  },
  mutations: {
    SET_CARD_LIST(state, array) {
      state.cardList = array;
    },
    SET_CARD_USER(state, name) {
      state.cardUser = name;
    },
    SET_CARD_ITEM(state, obj) {
      state.cardItem = obj;
    },
  },
  actions: {
    getCardList({ commit }, name) {
      commit('SET_CARD_USER', name);
      API.setQuery('card', 'user', name).then(response => {
        commit('SET_CARD_LIST', response.payload.results);
      });
    },
    getCardItem({ commit }, id) {
      return new Promise((resolve, reject) => {
        API.set('card', id)
          .then(response => {
            commit('SET_CARD_ITEM', response.payload);
            resolve();
          })
          .catch(error => {
            reject(error);
          });
      });
    },
    getCardListForDam({ commit }, damId) {
      API.setQuery('card', 'dam', damId).then(response => {
        commit('SET_CARD_LIST', response.payload.results);
      });
    },
  },
  getters: {},
};

export default card;
