import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login.vue'
import Homepage from '@/components/Homepage'
import process from 'shelljs'
import Register from '../components/Register'
import ForgotPassword from '../components/ForgotPassword'
import Reset from '../components/Reset'
import BusinessContact from '../components/BusinessContact'
import Profile from '../components/Profile'
import EditProfile from '../components/EditProfile'
import HouseDetails from '../components/HouseDetails'
import PrivacyPolicy from '../components/PrivacyPolicy'
import AboutUs from '../components/AboutUs'
import MyHouseDetails from '../components/MyHouseDetails'
import HouseRegistry from '../components/HouseRegistry'
import MyReservationDetails from '../components/MyReservationDetails'

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
      path: '/BusinessContact',
      name: 'BusinessContact',
      component: BusinessContact
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile
    },
    {
      path: '/editProfile',
      name: 'EditProfile',
      component: EditProfile
    },
    {
      path: '/housedetails',
      name: 'HouseDetails',
      component: HouseDetails
    },
    {
      path: '/myReservationDetails',
      name: 'MyReservationDetails',
      component: MyReservationDetails
    },
    {
      path: '/myHouseDetails',
      name: 'MyHouseDetails',
      component: MyHouseDetails
    },
    {
      path: '/privacyPolicy',
      name: 'privacyPolicy',
      component: PrivacyPolicy
    },
    {
      path: '/aboutUs',
      name: 'AboutUs',
      component: AboutUs
    },
    {
      path: '/HouseRegistry',
      name: 'HouseRegistry',
      component: HouseRegistry
    }
  ]
})
