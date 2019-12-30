import Vue from 'vue';
import VueRouter from 'vue-router';
import store from '../store';
import SiteTop from '../components/pages/SiteTop';
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
    path: '/login',
    name: 'login',
    component: LoginPage,
  },
  {
    path: '/post',
    name: 'post',
    component: PostPage,
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
    path: '/login',
    query: { next: to.fullPath },
  });
}

export default router;
