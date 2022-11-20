import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login.vue'
import Homepage from '@/components/Homepage'
import process from 'shelljs'
import Register from '../components/Register'
import ForgotPassword from '../components/ForgotPassword'
import Reset from '../components/Reset'
import PrivacyPolicy from '../components/PrivacyPolicy'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Homepage',
      component: Homepage
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/forgotPassword',
      name: 'ForgotPassword',
      component: ForgotPassword
    },
    {
      path: '/reset',
      name: 'ResetPassword',
      component: Reset
    },
    {
      path: '/privacyPolicy',
      name: 'privacyPolicy',
      component: PrivacyPolicy
    }
  ]
})
