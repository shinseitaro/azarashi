import Vue from 'vue';
import VueRouter from 'vue-router';
// import store from '../store';
import SiteTop from '../components/pages/SiteTop';
import SignUp from '../components/pages/SignUp';
import CheckYourEmail from '../components/pages/CheckYourEmail';
import Login from '../components/pages/Login';
import Post from '../components/pages/Post';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'sitetop',
    component: SiteTop,
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUp,
  },
  {
    path: '/check_your_email',
    name: 'check_your_email',
    component: CheckYourEmail,
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
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

// router.beforeEach((to, from, next) => {
//   if (to.matched.some(record => record.meta.requiresAuth)) {
//     if (!store.state.form.loggedIn) {
//       next({
//         path: '/login',
//         query: { redirect: to.fullPath },
//       });
//     } else {
//       next();
//     }
//   } else {
//     next();
//   }
// });

export default router;
