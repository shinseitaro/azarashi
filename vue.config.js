module.exports = {
  pages: {
    index: {
      entry: '/frontend/src/main.js',
      template: '/frontend/templates/frontend/index.html',
    },
  },
  outputDir: '/frontend/static/frontend',
  indexPath: '/frontend/templates/frontend/index.html',
  publicPath: process.env.NODE_ENV === 'production' ? '/static/' : '/frontend/static/frontend',
  transpileDependencies: ['vuetify'],
};

