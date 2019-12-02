import * as API from '../../apis/API';

const initialCenter = [139.7009177, 35.6580971];

const map = {
  namespaced: true,
  state: {
    damData: {},
    isDisplayMarker: false,
    markerPosition: initialCenter,
    boundsNext: initialCenter,
    bounds: [initialCenter, initialCenter],
    isMoving: false,
  },
  mutations: {
    GET_DAM_DATA(state, data) {
      state.damData = data;
    },
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
    getDamData({ commit }) {
      API.read('dam').then(data => {
        commit('GET_DAM_DATA', data);
      });
    },
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
