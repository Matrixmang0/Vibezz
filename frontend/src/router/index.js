import { createRouter, createWebHistory } from 'vue-router';
import store from '../store';

import Home from '../views/Home.vue';
import Registration from '../views/Registration.vue';
import Login from '../views/Login.vue';
import Profile from '../views/Profile.vue';
import ChangePassword from '../views/ChangePassword.vue';
import MyStudio from '../views/MyStudio.vue';
import CreateAlbum from '../views/CreateAlbum.vue';
import EditAlbum from '../views/EditAlbum.vue';
import Album from '../views/Album.vue';
import CreateSong from '../views/CreateSong.vue';
import EditSong from '../views/EditSong.vue';
import UserAlbum from '../views/UserAlbum.vue';
import Song from '../views/Song.vue';
import Playlists from '../views/Playlists.vue';
import CreatePlaylist from '../views/CreatePlaylist.vue';
import RenamePlaylist from '../views/RenamePlaylist.vue';
import PlaylistSongs from '../views/PlaylistSongs.vue';

const routes = [

  {
    path: '/',
    name: 'Home',
    component: Home,
    beforeEnter: async (to, from, next) => {
      try {
        if (!localStorage.getItem('token')) {
          store.dispatch('showMessage', "Please login to access this page");
          next('/login');
          return;
        }

        const token = localStorage.getItem('token');

        const response = await fetch('http://127.0.0.1:5000/api/albums', {
          method: 'get',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token,
          },
        });

        if (response.ok) {
          const data = await response.json();
          to.meta.albums = data;
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

  {
    path: '/album/:albumId',
    name: 'Album',
    component: Album,
    meta: {
      title: 'Album'
    },  
    beforeEnter: async (to, from, next) => {
      try {
        if (!localStorage.getItem('token')) {
          store.dispatch('showMessage', "Please login to access this page");
          next('/login');
          return;
        }

        const token = localStorage.getItem('token');
        const albumId = to.params.albumId;

        const response1 = await fetch(`http://127.0.0.1:5000/api/${localStorage.getItem('user_id')}/albums/${albumId}/info`, {
          method: 'get',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token,
          },
        });

        if (response1.ok) {
          const data = await response1.json();
          if (data.msg === "No Albums found"){
            console.log("No Albums found");
            this.$router.go();
          }
          else{
            to.meta.album = data;
          }
        } else {
          console.error('Failed to fetch album data:', response1.status);
        }

        const response2 = await fetch(`http://127.0.0.1:5000/api/${localStorage.getItem('user_id')}/album/${albumId}`, {
          method: 'get',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token,
          },
        });

        if (response2.ok) {
          const data = await response2.json();
          if (data.msg === "No songs found"){
            to.meta.songExists = false;
            console.log("No songs found");
            next();
          }
          else{
            to.meta.songExists = true;
            to.meta.data = data;
            next();
          }
        } else {
          console.error('Failed to fetch songs data:', response2.status);
        }

      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
  },

  {
      path: '/create-song',
      name: 'CreateSong',
      component: CreateSong,
      meta: {
        title: 'Create Song'
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
            next();
          }
          else{
            to.meta.albums = data;
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
    path: '/album/edit/:albumId',
    name: 'EditAlbum',
    component: EditAlbum,
    meta: {
      title: 'Edit Album'
    },
    beforeEnter: async (to, from, next) => {
      try {
        if (!localStorage.getItem('token')) {
          store.dispatch('showMessage', "Please login to access this page");
          next('/login');
          return;
        }

        const token = localStorage.getItem('token');

        const response = await fetch(`http://127.0.0.1:5000/api/${localStorage.getItem('user_id')}/albums/${to.params.albumId}/info`, {
          method: 'get',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token,
          },
        });

        if (response.ok) {
          const data = await response.json();
          to.meta.album = data;
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
    path: '/song/edit/:songId',
    name: 'EditSong',
    component: EditSong,
    meta: {
      title: 'Edit Song'
    },
    beforeEnter: async (to, from, next) => {
      try {
        if (!localStorage.getItem('token')) {
          store.dispatch('showMessage', "Please login to access this page");
          next('/login');
          return;
        }

        const token = localStorage.getItem('token');

        const response1 = await fetch(`http://127.0.0.1:5000/api/${localStorage.getItem('user_id')}/songs/${to.params.songId}`, {
          method: 'get',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token,
          },
        });

        if (response1.ok) {
          const data = await response1.json();
          to.meta.song = data;
        } else {
          console.error('Failed to fetch user data:', response1.status);
        }

        const response2 = await fetch('http://127.0.0.1:5000/api/' + localStorage.getItem('user_id') +'/albums', {
          method: 'get',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token,
          },
        });

        if (response2.ok) {
          const data = await response2.json();
          if (data.msg === "No albums found"){
            next();
          }
          else{
            to.meta.albums = data;
            next();
          }
        } else {
          console.error('Failed to fetch album data:', response2.status);
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }
  },

    {
    path: '/user/album/:albumId',
    name: 'UserAlbum',
    component: UserAlbum,
    meta: {
      title: 'User Album'
    },  
    beforeEnter: async (to, from, next) => {
      try {

        const token = localStorage.getItem('token');
        const albumId = to.params.albumId;

        const response1 = await fetch(`http://127.0.0.1:5000/api/album/${albumId}`, {
          method: 'get',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token,
          },
        });

        if (response1.ok) {
          const data = await response1.json();
          if (data.msg === "No Albums found"){
            console.log("No Albums found");
            this.$router.go();
          }
          else{
            to.meta.album = data;
            next();
          }
        } else {
          console.error('Failed to fetch album data:', response1.status);
        }

      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
  },

  {
    path: '/play/song/:songId',
    name: 'Song',
    component: Song,
    meta: {
      title: 'Song'
    },  
    beforeEnter: async (to, from, next) => {
      try {

        const token = localStorage.getItem('token');
        const songId = to.params.songId;

        const response1 = await fetch(`http://127.0.0.1:5000/api/song/${songId}`, {
          method: 'get',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token,
          },
        });

        if (response1.ok) {
          const data = await response1.json();
          if (data.msg === "No Songs found"){
            console.log("No Songs found");
            this.$router.go();
          }
          else{
            to.meta.song = data;
            next();
          }
        } else {
          console.error('Failed to fetch album data:', response1.status);
        }

      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
  },

  {
    path: '/playlists',
    name: 'Playlists',
    component: Playlists,
    meta: {
      title: 'Playlists'
    },  
    beforeEnter: async (to, from, next) => {
      try {
        if (!localStorage.getItem('token')) {
          store.dispatch('showMessage', "Please login to access this page");
          next('/login');
          return;
        }

        const token = localStorage.getItem('token');
        const response = await fetch('http://127.0.0.1:5000/api/' + localStorage.getItem('user_id') +'/playlists', {
          method: 'get',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token,
          },
        });

        if (response.ok) {
          const data = await response.json();
          if (data.msg === "No playlists found"){
            to.meta.playlistExists = false;
            next();
          }
          else{
            to.meta.playlistExists = true;
            to.meta.playlists = data;
            next();
          }
        } else {
          console.error('Failed to fetch playlists data:', response.status);
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
  },

  {
      path: '/create-playlist',
      name: 'CreatePlaylist',
      component: CreatePlaylist,
      meta: {
        title: 'Create Playlist'
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
    },
  },

  {
      path: '/playlist/edit/:playlistId',
      name: 'RenamePlaylist',
      component: RenamePlaylist,
      meta: {
        title: 'Rename Playlist'
      },
      beforeEnter: async (to, from, next) => {
        try {
          if (!localStorage.getItem('token')) {
            store.dispatch('showMessage', "Please login to access this page");
            next('/login');
          }
          const token = localStorage.getItem('token');
          const playlistId = to.params.playlistId;

          const response = await fetch(`http://127.0.0.1:5000/api/${localStorage.getItem('user_id')}/playlist/${playlistId}`, { 
            method: 'get',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': 'Bearer ' + token,
            },
          });

          if (response.ok) {
            const data = await response.json();
            to.meta.playlist = data;
            next();
          } else {
            console.error('Failed to fetch playlist data:', response.status);
          }
        } catch (error) {
          console.error('Error fetching data:', error);
        }
    }

  },

  {
      path: '/playlist/:playlistId',
      name: 'PlaylistSongs',
      component: PlaylistSongs,
      meta: {
        title: 'Playlist Songs'
      },
      beforeEnter: async (to, from, next) => {
        try {
          if (!localStorage.getItem('token')) {
            store.dispatch('showMessage', "Please login to access this page");
            next('/login');
          }
          const token = localStorage.getItem('token');
          const playlistId = to.params.playlistId;

          const response1 = await fetch(`http://127.0.0.1:5000/api/${localStorage.getItem('user_id')}/playlist/${playlistId}`, { 
            method: 'get',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': 'Bearer ' + token,
            },
          });

          if (response1.ok) {
            const data = await response1.json();
            to.meta.playlist = data;
          } else {
            console.error('Failed to fetch playlist data:', response1.status);
          }

          const response2 = await fetch('http://127.0.0.1:5000/api/albums', {
            method: 'get',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': 'Bearer ' + token,
            },
          });

          if (response2.ok) {
            const data = await response2.json();
            to.meta.albums = data;
            console.log(to.meta.albums);
            next();
          } else {
            console.error('Failed to fetch user data:', response2.status);
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
