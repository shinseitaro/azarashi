import * as API from '../../apis/API';

const initialCenter = [139.7009177, 35.6580971];

const map = {
  namespaced: true,
  state: {
    damGeoData: {},
    damList: [],
    isDisplayMarker: false,
    isDisplayPopup: false,
    markerPosition: initialCenter,
    boundsNext: initialCenter,
    bounds: [initialCenter, initialCenter],
    isMoving: false,
    search: {
      name: '',
      address: '',
      prefecture: '',
      river: '',
      waterSystem: '',
    },
    isEmptySearchField: true,
  },
  mutations: {
    GET_DAM_GEO_DATA(state, data) {
      state.damGeoData = data;
    },
    GET_DAM_LIST(state, list) {
      state.damList = list;
    },
    SET_POPUP(state, bool) {
      state.isDisplayPopup = bool;
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
    SEARCH_NAME(state, name) {
      state.search.name = name;
    },
    SEARCH_ADDRESS(state, address) {
      state.search.address = address;
    },
    SEARCH_PREF(state, pref) {
      state.search.prefecture = pref;
    },
    SEARCH_RIVER(state, river) {
      state.search.river = river;
    },
    SEARCH_WATER_SYSTEM(state, waterSystem) {
      state.search.waterSystem = waterSystem;
    },
    EMPTY_SEARCH_FIELD(state, bool) {
      state.isEmptySearchField = bool;
    },
  },
  actions: {
    getDamGeoData({ commit }) {
      API.read('dam/map').then(response => {
        commit('GET_DAM_GEO_DATA', response.payload);
      });
    },
    getDamList({ commit }) {
      API.read('dam/list').then(response => {
        commit('GET_DAM_LIST', response.payload);
      });
    },
    setPopup({ commit }, bool) {
      commit('SET_POPUP', bool);
    },
    startMove({ commit }, marker) {
      commit('START_MOVE', marker);
    },
    stopMove({ commit }) {
      commit('STOP_MOVE');
    },
    searchName({ commit }, name) {
      return new Promise(resolve => {
        commit('SEARCH_NAME', name);
        resolve();
      });
    },
    searchAddress({ commit }, address) {
      return new Promise(resolve => {
        commit('SEARCH_ADDRESS', address);
        resolve();
      });
    },
    searchPref({ commit }, pref) {
      return new Promise(resolve => {
        commit('SEARCH_PREF', pref);
        resolve();
      });
    },
    searchRiver({ commit }, river) {
      return new Promise(resolve => {
        commit('SEARCH_RIVER', river);
        resolve();
      });
    },
    searchWaterSystem({ commit }, waterSystem) {
      return new Promise(resolve => {
        commit('SEARCH_WATER_SYSTEM', waterSystem);
        resolve();
      });
    },
    emptySearchField({ commit, state }) {
      const isEmpty = Object.values(state.search).every(
        x => x === null || x === ''
      );
      return new Promise(resolve => {
        commit('EMPTY_SEARCH_FIELD', isEmpty);
        resolve();
      });
    },
    searchResult({ dispatch, commit, state }) {
      if (!state.isEmptySearchField) {
        API.searchGeo(
          'dam/search',
          state.search.name,
          state.search.address,
          state.search.prefecture,
          state.search.river,
          state.search.waterSystem
        ).then(response => {
          commit('GET_DAM_GEO_DATA', response.payload.results);
          commit('GET_DAM_LIST', response.payload.results.features);
        });
      } else {
        dispatch('getDamGeoData');
        dispatch('getDamList');
      }
      commit('SET_POPUP', false);
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
