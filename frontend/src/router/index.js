import Vue from 'vue'
import VueRouter from 'vue-router'

import Registration from '../components/Registration.vue'
import Login from '../components/Login.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/register',
    name: 'Registration',
    component: Registration,
    props: true,
    meta: {
      title: 'Register'
    },
    beforeEnter: (to, from, next) => {
      if (localStorage.getItem('token')) {
        next('/login')
      } else {
        next()
      }
    }
  },

  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: {
      title: 'Login'
    },
  },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
})

export default router
