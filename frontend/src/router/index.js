import Vue from 'vue';
import VueRouter from 'vue-router';
import store from '../store';
import SiteTop from '../components/pages/SiteTop';
import DamPage from '../components/pages/DamPage';
import SignUp from '../components/pages/SignUp';
import CheckYourEmail from '../components/pages/CheckYourEmail';
import CompleteSignUp from '../components/pages/CompleteSignUp';
import LoginPage from '../components/pages/LoginPage';
import PostPage from '../components/pages/PostPage';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'sitetop',
    component: SiteTop,
  },
  {
    path: '/dam/:damId',
    name: 'dam',
    component: DamPage,
    props: true,
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
    path: '/complete_sign_up',
    name: 'complete_sign_up',
    component: CompleteSignUp,
  },
  {
    path: '/login/:damId?',
    name: 'login',
    component: LoginPage,
    props: true,
  },
  {
    path: '/post/:damId',
    name: 'post',
    component: PostPage,
    props: true,
    meta: { requiresAuth: true },
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token');
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.state.auth.isLoggedIn) {
      next();
    } else {
      if (token !== null) {
        store
          .dispatch('auth/update')
          .then(() => {
            next();
          })
          .catch(() => {
            forceToLoginPage(to, from, next);
          });
      } else {
        forceToLoginPage(to, from, next);
      }
    }
  } else {
    next();
  }
});

function forceToLoginPage(to, from, next) {
  next({
    name: 'login',
    query: { next: to.fullPath },
    params: to.params,
  });
}

export default router;
