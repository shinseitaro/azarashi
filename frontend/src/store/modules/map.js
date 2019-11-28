const initialCenter = [139.7009177, 35.6580971];

const map = {
  namespaced: true,
  state: {
    isDisplayMarker: false,
    markerPosition: initialCenter,
    boundsNext: initialCenter,
    bounds: [initialCenter, initialCenter],
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
