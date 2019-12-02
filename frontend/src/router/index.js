import Vue from 'vue';
import VueRouter from 'vue-router';
import SiteTop from '../components/pages/SiteTop.vue';
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
    path: '/post',
    name: 'post',
    component: Post,
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

export default router;
