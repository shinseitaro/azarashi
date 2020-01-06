import Vue from 'vue';
import Vuex from 'vuex';
import map from './modules/map';
import auth from './modules/auth';
import dam from './modules/dam';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    map,
    auth,
    dam,
  },
});
