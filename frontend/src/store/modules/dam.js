import * as API from '../../apis/API';

const dam = {
  namespaced: true,
  state: {
    damId: 0,
    damName: '',
    damInfo: [],
    damGeoData: {},
    damCoord: [null, null],
    distributionList: [],
    distributionCoords: [[null, null]],
    cardList: [],
  },
  mutations: {
    SET_DAM_ID(state, id) {
      state.damId = id;
    },
    SET_DAM_NAME(state, name) {
      state.damName = name;
    },
    SET_DAM_INFO(state, array) {
      state.damInfo = array;
    },
    SET_DAM_GEO_DATA(state, data) {
      state.damGeoData = data;
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
      return new Promise(resolve => {
        const payload = API.setQuery('dam', 'dam_code', id).then(response => {
          commit(
            'SET_DAM_NAME',
            response.payload.results.features[0].properties.name
          );
          commit(
            'SET_DAM_INFO',
            response.payload.results.features[0].properties
          );
          commit('SET_DAM_GEO_DATA', response.payload.results);
          commit(
            'SET_DAM_COORD',
            response.payload.results.features[0].geometry.coordinates
          );
        });
        resolve(payload);
      });
    },
  },
  getters: {},
};

export default dam;
