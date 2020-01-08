import * as API from '../../apis/API';

const map = {
  namespaced: true,
  state: {
    damGeoData: {},
    damList: [],
    isDisplayPopup: false,
    search: {
      name: '',
      address: '',
      prefecture: '',
      river: '',
      waterSystem: '',
    },
    isEmptySearchField: true,
    page: 1,
    pageLength: 1,
  },
  mutations: {
    SET_DAM_GEO_DATA(state, data) {
      state.damGeoData = data;
    },
    SET_DAM_LIST(state, list) {
      state.damList = list;
    },
    SET_POPUP(state, bool) {
      state.isDisplayPopup = bool;
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
    SET_PAGE_NUM(state, page) {
      state.page = page;
    },
    SET_PAGE_LENGTH(state, count) {
      state.pageLength = Math.ceil(count / 10);
    },
    RESET_PAGE_NUM(state) {
      state.page = 1;
    },
  },
  actions: {
    getDamGeoData({ commit }) {
      API.read('dam/map').then(response => {
        commit('SET_DAM_GEO_DATA', response.payload);
      });
    },
    getDamList({ commit, state }) {
      API.readPage('dam/list', state.page).then(response => {
        commit('SET_DAM_LIST', response.payload.results);
        commit('SET_PAGE_LENGTH', response.payload.count);
      });
    },
    initDamList({ commit }) {
      API.readPage('dam/list', 1).then(response => {
        commit('RESET_PAGE_NUM');
        commit('SET_DAM_LIST', response.payload.results);
        commit('SET_PAGE_LENGTH', response.payload.count);
      });
    },
    setPopup({ commit }, bool) {
      commit('SET_POPUP', bool);
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
          state.search.waterSystem,
          state.page
        ).then(response => {
          commit('SET_PAGE_LENGTH', response.payload.count);
          commit('SET_DAM_GEO_DATA', response.payload.results);
          commit('SET_DAM_LIST', response.payload.results.features);
        });
      } else {
        dispatch('getDamGeoData');
        dispatch('initDamList');
      }
      commit('SET_POPUP', false);
    },
    setPageNum({ commit }, payload) {
      commit('SET_PAGE_NUM', payload.page);
    },
  },
  getters: {},
};

export default map;
