import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const map = {
  namespaced: true,
  state: {
    isDisplayMarker: false,
    markerPosition: [0, 0],
    boundsNext: [139.7009177, 35.6580971],
    bounds: [
      [139.7009177, 35.6580971],
      [139.7009177, 35.6580971],
    ],
  },
  mutations: {
    SET_MARKER(state, marker) {
      state.isDisplayMarker = true;
      state.markerPosition = marker;
      state.boundsNext = marker;
    },
  },
  actions: {
    setMarker({ commit }, marker) {
      commit('SET_MARKER', marker);
    },
  },
  getters: {
    getBounds: state => {
      const boundsArray = [...state.bounds, state.boundsNext].slice(-2);
      state.bounds = boundsArray;
      return boundsArray;
    },
  },
};

export default map;
