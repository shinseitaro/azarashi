import Vue from 'vue';
import Vuex from 'vuex';
import map from './modules/map';
import form from './modules/form';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    map,
    form,
  },
});
