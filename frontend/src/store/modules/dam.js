import * as API from '../../apis/API';

const dam = {
  namespaced: true,
  state: {
    damId: 0,
    damInfo: [],
    damCoord: [null, null],
    distributionList: [],
    distributionCoords: [[null, null]],
    cardList: [],
  },
  mutations: {
    SET_DAM_ID(state, id) {
      state.damId = id;
    },
    SET_DAM_INFO(state, array) {
      state.damInfo = array;
    },
    SET_DAM_COORD(state, array) {
      state.damCoord = array;
    },
    SET_DISTRIBUTION_LIST(state, array) {
      state.distributionList = array;
    },
    SET_DISTRIBUTION_COORDS(state, array) {
      state.distributionCoords = array;
    },
    SET_CARD_LIST(state, array) {
      state.cardList = array;
    },
  },
  actions: {
    getDamId({ commit }, id) {
      commit('SET_DAM_ID', id);
    },
    getDam({ commit }, id) {
      API.setQuery('dam', 'dam_code', id).then(response => {
        commit('SET_DAM_INFO', response.payload.results[0]);
        commit('SET_DAM_COORD', response.payload.results[0].geom.coordinates);
      });
    },
  },
  getters: {},
};

export default dam;
