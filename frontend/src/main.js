import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false

router.beforeEach((to, from, next) => {
  document.title = to.meta.title || 'Vibezz'; // Update title based on meta title of the route
  next();
});

new Vue({
  router,
  render: function (h) { return h(App) }
}).$mount('#app')
