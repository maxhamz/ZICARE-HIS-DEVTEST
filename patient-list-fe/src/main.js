  
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Vuex from 'vuex'
import VueResource from 'vue-resource'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import Toasted from 'vue-toasted'
// Install BootstrapVue
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)
Vue.use(VueResource)
Vue.use(Toasted, {
  duration: 3000,
  position: 'top-right'
})

Vue.use(Vuex)

Vue.config.productionTip = false
Vue.http.options.crossOrigin = true
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')