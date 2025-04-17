<template>
    <nav class="navbar">
      <div class="logout-container">
        <button class="logout-btn" @click="handleLogout">
          Déconnexion
        </button>
      </div>
    </nav>
  </template>
  
  <script setup lang="ts">
    import router from '../router';
    import { logout } from '../service/AuthService';

    console.log('navbar loaded');
    async function handleLogout(){
        await logout();
        router.push('/login')
    }
  </script>

<style scoped>
/* Style de la navbar */
.navbar {
  background-color: #333;
  color: white;
  padding: 10px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  z-index: 10;
}

/* Style pour le logo */
.logo {
  font-size: 1.5rem;
  font-weight: bold;
}

/* Style pour le container du bouton de déconnexion */
.logout-container {
  display: flex;
  justify-content: flex-end;
}

/* Style du bouton de déconnexion */
.logout-btn {
  background-color: #e74c3c;
  color: white;
  border: none;
  padding: 8px 16px;
  font-size: 1rem;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.logout-btn:hover {
  background-color: #c0392b;
}
</style>
  