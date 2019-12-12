module.exports = {
  pages: {
    index: {
      entry: 'frontend/src/main.js',
      template: 'frontend/templates/frontend/index.html',
    },
  },
  outputDir: 'frontend/static/frontend',
  publicPath: process.env.NODE_ENV === 'production' ? '/static/' : '/',
  transpileDependencies: ['vuetify'],
};
