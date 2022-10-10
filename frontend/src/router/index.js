import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login.vue'
import Homepage from '@/components/Homepage'
import process from 'shelljs'

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
    }
  ]
})
