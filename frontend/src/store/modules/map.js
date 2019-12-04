import * as API from '../../apis/API';

const initialCenter = [139.7009177, 35.6580971];

const map = {
  namespaced: true,
  state: {
    page: 1,
    damDataForCardList: [],
    damData: {},
    markers: [],
    isDisplayMarker: false,
    markerPosition: initialCenter,
    boundsNext: initialCenter,
    bounds: [initialCenter, initialCenter],
    isMoving: false,
    loadingBusy: false,
  },
  mutations: {
    GET_DAM_DATA(state, data) {
      state.damData = data;
    },
    GET_DAM_DATA_FOR_CARD_LIST(state, data) {
      state.damDataForCardList.push(data)
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
    PAGE_UP(state) {
      state.page =+ 1
    },
    PAGE_DOWN(state) {
      state.page =-1
    },
    LOADING_BUSY(state){
      state.loadingBusy = true;
    },
    LOADING_NOT_BUSY(state){
      state.loadingBusy = false;
    },

  },
  actions: {

    //カードリスト用のactionをつくる
    //API.readpage()
    //stateも新規に必要
    //pageもstateにするといい。
    //pageの値を変更するためのaction
    getDamDataForCardList({commit}) {
      API.readPage('dam', state.page).then(response => {
        commit('GET_DAM_DATA_FOR_CARD_LIST', response.payload.results);
        return ''
      })
    }
    ,


    getDamData({ commit }) {
      let markersArray = [];
      API.read('dam')
        .then(response => {
          commit('GET_DAM_DATA', response.payload.results);
          return response.payload.results;
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
    pageUp( { commit },   ) {
      commit('PAGE_UP')
    },
    pageDown({ commit },) {
      commit('PAGE_DOWN')
    },
    loadingBusy({commit},) {
      commit('LOADING_BUSY')
    }
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
