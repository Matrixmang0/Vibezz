import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';

router.beforeEach((to, from, next) => {
  document.title = to.meta.title || 'Vibezz'; 
  next();
});

const app = createApp(App);
app.use(router);
app.use(store);
app.mount('#app');