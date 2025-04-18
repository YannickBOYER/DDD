// src/router/index.ts
import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Home from '../views/Home.vue'
import Analys from '../views/Analys.vue'
import PlalystCreator from '../views/PlaylistCreator.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/login', name: 'Login', component: Login },
  { path: '/analys', name: 'analys', component: Analys },
  { path: '/playlist-generation', name: 'playlist-generation', component: PlalystCreator },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
