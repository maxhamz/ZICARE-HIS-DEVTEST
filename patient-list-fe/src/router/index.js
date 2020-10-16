import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home'
import RegisterPage from '../views/RegisterPage'
import EditPage from '../views/EditPage'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/register',
    component: RegisterPage,
    name: 'RegisterPage'
  },
  {
    path: '/edit/:id',
    component: EditPage,
    name: 'EditPage'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router