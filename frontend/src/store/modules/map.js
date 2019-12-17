import * as API from '../../apis/API';

const initialCenter = [139.7009177, 35.6580971];

const map = {
  namespaced: true,
  state: {
    damData: {},
    markers: [],
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
    GET_MARKERS(state, markers) {
      state.markers = markers;
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
      let markersArray = [];
      API.read('dam/map')
        .then(response => {
          commit('GET_DAM_DATA', response.payload);
          return response.payload;
        })
        .then(data => {
          data.features.map(value => {
            markersArray.push(value.geometry.coordinates);
          });
          commit('GET_MARKERS', markersArray);
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
