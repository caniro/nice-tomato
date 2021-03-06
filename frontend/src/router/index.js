import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/cctv',
    name: 'Cctv',
    component: () => import('../views/Cctv.vue')
  },
  {
    path: '/sensor',
    name: 'Sensor',
    component: () => import('../views/Sensor.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/detail',
    name: 'Detail',
    component: () => import('../views/Detail.vue')
  },
  {
    path: '/testchart',
    name: 'TestChart',
    component: () => import('../views/TestChart.vue')
  },
  {
    path: '/car',
    name: 'MonitoringCar',
    component: () => import('../views/MonitoringCar.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
