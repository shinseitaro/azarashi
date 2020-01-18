import Vue from 'vue';
import Vuetify from 'vuetify/lib';

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: '#607d8b',
        secondary: '#ff5722',
        accent: '#3f51b5',
        error: '#f44336',
        warning: '#ffc107',
        info: '#8bc34a',
        success: '#009688',
      },
    },
  },
});
