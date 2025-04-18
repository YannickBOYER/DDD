<script setup lang="ts">
import { onMounted } from 'vue';
import Navbar from './Navbar.vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const token = localStorage.getItem('token');
onMounted(async () => {
  if (!token) {
    router.push('/login');
  }
});
</script>
<template>
    <Navbar />
    <h1>Analyse</h1>
</template>