<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import Navbar from './Navbar.vue';
import { getUserGroups } from '../service/AuthService';

// Variables réactives
const isAdmin = ref(false);
const isAnalyst = ref(false);
const isPlaylistCreator = ref(false);

const router = useRouter();
const token = localStorage.getItem('token');

// Vérification du token et des groupes utilisateur
onMounted(async () => {
  if (!token) {
    router.push('/login');
  } else {
    const groups = await getUserGroups() as string[];
    isAdmin.value = groups.includes('admin');
    isAnalyst.value = groups.includes('analyst');
    isPlaylistCreator.value = groups.includes('playlist_creator');
  }
});

function handleAnalyst(){
  router.push('/analyst');
}

function handlePlaylistCreator(){
  router.push('/playlist-creation');
}

function handleAdminUsers(){
  router.push('/admin-users');
}
</script>

<template>
    <Navbar />
    <div class="home-page">  
        <h1>Home-page</h1>
        <div class="tiles-container">
            <div v-if="isAdmin || isAnalyst" class="tile" @click="handleAnalyst">
                <h2>Analyst</h2>
                <p>Analyste data</p>
            </div>
            <div v-if="isAdmin || isPlaylistCreator" class="tile" @click="handlePlaylistCreator">
                <h2>Playlist maker</h2>
                <p>Créateur de playlist dans un pays cible</p>
            </div>
            <div v-if="isAdmin" class="tile" @click="handleAdminUsers">
                <h2>User Admin</h2>
                <p>Gestion des utilisateurs</p>
            </div>
        </div>
    </div>
</template>

<style scoped>
.home-page {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  padding-top: 80px; /* Pour laisser de l'espace en dessous de la navbar */
}

.tiles-container {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px; /* Espacement entre les tuiles */
}

.tile {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 20px;
  width: 250px;
  height: 150px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  transition: transform 0.3s ease;
  cursor: pointer;
}

.tile:hover {
  transform: translateY(-10px);
}

.tile h2 {
  font-size: 1.5rem;
  margin-bottom: 10px;
  color: #333;
}

.tile p {
  font-size: 1rem;
  color: #555;
}
</style>