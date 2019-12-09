import Vue from 'vue';
import VueRouter from 'vue-router';
import store from '../store';
import SiteTop from '../components/pages/SiteTop.vue';
import Login from '../components/pages/Login.vue';
import Post from '../components/pages/Post.vue';
import About from '../components/pages/About.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'sitetop',
    component: SiteTop,
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
  },
  {
    path: '/post',
    name: 'post',
    component: Post,
    meta: { requiresAuth: true },
  },
  {
    path: '/about',
    name: 'about',
    component: About,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.state.form.loggedIn) {
      next({
        path: '/login',
        query: { redirect: to.fullPath },
      });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
