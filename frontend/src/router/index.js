import { createRouter, createWebHistory } from 'vue-router';

import Home from '../views/Home.vue'
import Registration from '../views/Registration.vue'
import Login from '../views/Login.vue'

const routes = [

  {
    path: '/',
    name: 'Home',
    component: Home
  },

  {
    path: '/register',
    name: 'Registration',
    component: Registration,
    props: true,
    meta: {
      title: 'Register'
    },
  },

  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: {
      title: 'Login'
    },
    beforeEnter: (to, from, next) => {
      if (localStorage.getItem('token')) {
        next('/')
      } else {
        next()
      }
    }
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})


export default router;
