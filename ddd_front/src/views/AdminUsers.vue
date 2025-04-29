<script setup lang="ts">
import { onMounted, ref } from 'vue';
import Navbar from './Navbar.vue';
import { useRouter } from 'vue-router';
import { getUserGroups } from '../service/AuthService';
import { findUsers, deleteUser, type User } from '../service/UserService';

const router = useRouter();
const token = localStorage.getItem('token');
const users = ref<User[]>([]);
const error = ref<string | null>(null);
const loadingId = ref<number | null>(null);

onMounted(async () => {
  if (!token) return router.push('/login');
  const groups = await getUserGroups() as string[];
  if (!groups.includes('admin')) return router.push('/');
  try {
    users.value = await findUsers();
  } catch (e: any) {
    error.value = e.message;
  }
});

async function removeUser(id: number) {
  if (!confirm('Supprimer cet utilisateur ?')) return;
  loadingId.value = id;
  try {
    await deleteUser(id);
    users.value = users.value.filter(u => u.id !== id);
  } catch (e: any) {
    error.value = e.message;
  } finally {
    loadingId.value = null;
  }
}
</script>

<template>
  <div class="admin-users-page">
    <Navbar />
    <h1>Gestion des utilisateurs</h1>
    <p v-if="error" class="error">{{ error }}</p>
    <table v-if="users.length">
      <thead>
        <tr>
          <th>Username</th>
          <th>Email</th>
          <th>Groupes</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="u in users" :key="u.id">
          <td>{{ u.username }}</td>
          <td>{{ u.email }}</td>
          <td>{{ u.groups.join(', ') }}</td>
          <td>
            <button
              @click="removeUser(u.id)"
              :disabled="loadingId === u.id"
            >
              {{ loadingId === u.id ? '…' : 'Supprimer' }}
            </button>
          </td>
        </tr>
      </tbody>
    </table>
    <p v-else>Aucun utilisateur trouvé.</p>
  </div>
</template>

<style scoped>
.admin-users-page {
  width: 800px;
  margin: auto;
  padding: 20px;
  background: #fafafa;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  font-family: 'Segoe UI', sans-serif;
}
h1 { color: #333; text-align: center; margin-bottom: 20px; }
table { width: 100%; border-collapse: collapse; }
th, td { color: black; padding: 8px; border: 1px solid #ddd; text-align: left; }
.error { color: #c00; margin-bottom: 1em; }
button {
  padding: 6px 12px;
  border: none;
  border-radius: 4px;
  background: #d9534f;
  color: white;
  cursor: pointer;
}
button[disabled] { opacity: 0.6; cursor: default; }
button:hover:not([disabled]) { background: #c9302c; }
</style>
