// src/router/index.ts
import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Home from '../views/Home.vue'
import Analys from '../views/Analyst.vue'
import PlaylistCreator from '../views/PlaylistCreator.vue'
import AdminUsers from '../views/AdminUsers.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/login', name: 'Login', component: Login },
  { path: '/analyst', name: 'analyst', component: Analys },
  { path: '/playlist-creation', name: 'playlist-creation', component: PlaylistCreator },
  { path: '/admin-users', name: 'admin-users', component: AdminUsers },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
