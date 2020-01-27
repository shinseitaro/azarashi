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
import UserPage from '../components/pages/UserPage';
import CardPage from '../components/pages/CardPage';
import StatsPage from '../components/pages/StatsPage';

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
    path: '/login/:damId?:userName?',
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
  {
    path: '/edit/:cardId',
    name: 'edit_post',
    component: PostPage,
    props: true,
  },
  {
    path: '/user/:userName',
    name: 'user',
    component: UserPage,
    props: true,
  },
  {
    path: '/user/:userName/mypage',
    name: 'mypage',
    component: UserPage,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: '/card/:cardId',
    name: 'card',
    component: CardPage,
    props: true,
  },
  {
    path: '/user/:userName/card/:cardId/mycard',
    name: 'mycard',
    component: CardPage,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: '/stats',
    name: 'stats',
    component: StatsPage,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    } else {
      return { x: 0, y: 0 };
    }
  },
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    goToNextByToken(to, from, next);
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

function goToNextByToken(to, from, next) {
  const token = localStorage.getItem('token');
  if (token !== null) {
    store
      .dispatch('auth/update')
      .then(() => {
        next();
      })
      .catch(error => {
        if (error.response.status === 401) {
          store.dispatch('auth/logout').then(() => {
            goToNextByToken(to, from, next);
          });
        }
      });
  } else {
    forceToLoginPage(to, from, next);
  }
}

export default router;
