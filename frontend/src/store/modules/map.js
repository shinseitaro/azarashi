import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const map = {
  namespaced: true,
  state: {
    isDisplayMarker: false,
    markerPosition: [139.7009177, 35.6580971],
    boundsNext: [139.7009177, 35.6580971],
    bounds: [
      [139.7009177, 35.6580971],
      [139.7009177, 35.6580971],
    ],
    isMoving: false,
  },
  mutations: {
    START_MOVE(state, marker) {
      state.isMoving = true;
      state.isDisplayMarker = true;
      state.markerPosition = marker;
      state.boundsNext = marker;
    },
    STOP_MOVE(state) {
      state.isMoving = false;
    },
  },
  actions: {
    startMove({ commit }, marker) {
      commit('START_MOVE', marker);
    },
    stopMove({ commit }) {
      commit('STOP_MOVE');
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
