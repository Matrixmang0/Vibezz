import { createRouter, createWebHistory } from 'vue-router';
import store from '../store';

import Home from '../views/Home.vue';
import Registration from '../views/Registration.vue';
import Login from '../views/Login.vue';
import Profile from '../views/Profile.vue';
import ChangePassword from '../views/ChangePassword.vue';
import MyStudio from '../views/MyStudio.vue';
import CreateAlbum from '../views/CreateAlbum.vue';

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
        store.dispatch('showMessage', "You are already logged in");
        next('/')
      } else {
        next()
      }
    }
  },

  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
    meta: {
      title: 'Profile'
    },
    beforeEnter: async (to, from, next) => {
      try {
        if (!localStorage.getItem('token')) {
          store.dispatch('showMessage', "Please login to access this page");
          next('/login');
          return;
        }

        const token = localStorage.getItem('token');

        const response = await fetch('http://127.0.0.1:5000/api/user/' + localStorage.getItem('user_id'), {
          method: 'get',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token,
          },
        });

        if (response.ok) {
          const data = await response.json();
          to.meta.data = data;
          next();
        } else {
          console.error('Failed to fetch user data:', response.status);
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }
  },
  
  {
    path: '/change-password',
    name: 'ChangePassword',
    component: ChangePassword,
    meta: {
      title: 'Change Password'
    },
    beforeEnter: async (to, from, next) => {
      try {
        if (!localStorage.getItem('token')) {
          store.dispatch('showMessage', "Please login to access this page");
          next('/login');
          return;
        }
        next();
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }
  },

  {
    path: '/studio',
    name: 'MyStudio',
    component: MyStudio,
    meta: {
      title: 'Studio'
    },  
    beforeEnter: async (to, from, next) => {
      try {
        if (!localStorage.getItem('token')) {
          store.dispatch('showMessage', "Please login to access this page");
          next('/login');
          return;
        }

        const token = localStorage.getItem('token');
        const response = await fetch('http://127.0.0.1:5000/api/' + localStorage.getItem('user_id') +'/albums', {
          method: 'get',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token,
          },
        });

        if (response.ok) {
          const data = await response.json();
          if (data.msg === "No albums found"){
            to.meta.albumExists = false;
            next();
          }
          else{
            to.meta.albumExists = true;
            to.meta.data = data;
            next();
          }
        } else {
          console.error('Failed to fetch album data:', response.status);
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
  },

    {
      path: '/create-album',
      name: 'CreateAlbum',
      component: CreateAlbum,
      meta: {
        title: 'Create Album'
      },
      beforeEnter: async (to, from, next) => {
        try {
          if (!localStorage.getItem('token')) {
            store.dispatch('showMessage', "Please login to access this page");
            next('/login');
          }
          else {
            next();
          }
        } catch (error) {
          console.error('Error fetching data:', error);
        }
    }

  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})


export default router;
