import Vue from 'vue';
import VueRouter from 'vue-router';
import EditorPage from '../components/EditorPage.vue';
import GalleryPage from '../components/GalleryPage.vue';

const routes = [
  { path: '/', component: EditorPage },
  { path: '/gallery/', component: GalleryPage },
]

const router = new VueRouter({
  mode: 'history',
  routes
});

Vue.use(VueRouter);

new Vue({
  router,
  watch: {
    $route(to, from) {
      window.scrollTo(0, 0);
    },
  },
  mounted() {
  }
}).$mount('#app');
