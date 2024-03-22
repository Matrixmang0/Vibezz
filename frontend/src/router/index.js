import { createRouter, createWebHistory } from 'vue-router';

import Registration from '../views/Registration.vue'
import Login from '../views/Login.vue'

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

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
