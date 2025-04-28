<script setup lang="ts">
import { onMounted, ref } from 'vue';
import Navbar from './Navbar.vue';
import { useRouter } from 'vue-router';
import { getUserGroups } from '../service/AuthService';
import {findAll} from '../service/CountryService'

interface CountryData {
  name: string
  popularity: number
  danceability: number
  energy: number
  valence: number
  social_media_users: number
  total_population: number
}


const router = useRouter();
const token = localStorage.getItem('token');
const countries = ref<CountryData[] | null>(null);

onMounted(async () => {
  const groups = await getUserGroups() as string[];
  let isAdmin = groups.includes('ddd_admin');
  let isAnalyst = groups.includes('ddd_analyst');
  if (!token) {
    router.push('/login');
  }else if(token && isAdmin || isAnalyst){
    countries.value = await findAll();
    console.log(countries)
  }
  else{
    router.push('/');
  }
});
</script>
<template>
    <Navbar />
    <h1>Analyse</h1>
    <table>
    <thead>
      <tr>
        <th>Pays</th>
        <th>Popularité</th>
        <th>Danceabilité</th>
        <th>Énergie</th>
        <th>Valence</th>
        <th>Utilisateurs Réseaux Sociaux</th>
        <th>Population Totale</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="country in countries" :key="country.name">
        <td>{{ country.name }}</td>
        <td>{{ country.popularity }}</td>
        <td>{{ country.danceability }}</td>
        <td>{{ country.energy }}</td>
        <td>{{ country.valence }}</td>
        <td>{{ country.social_media_users }}</td>
        <td>{{ country.total_population }}</td>
      </tr>
    </tbody>
  </table>
</template>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}
th, td {
  border: 1px solid #ccc;
  padding: 8px;
  text-align: center;
}
th {
  background-color: #6d6d6d;
}
</style>