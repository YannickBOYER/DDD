<script setup lang="ts">
import { onMounted, ref } from 'vue';
import Navbar from './Navbar.vue';
import { useRouter } from 'vue-router';
import {findCountries} from '../service/CountryService'
import {findSongsByCountry} from '../service/CountryService'

interface Song {
  name: string;
  artists: string;
}

const router = useRouter();
const token = localStorage.getItem('token');
const countries = ref<string[]>([]);
const songsByCountryCible = ref<{}>([]);

const selectedCountry = ref<string>('');
const selectedSong = ref<Song| null>(null);

onMounted(async () => {
  if (!token) {
    router.push('/login');
  }else{
    countries.value = await findCountries();
  }
});

async function countryChange(){
    songsByCountryCible.value = await findSongsByCountry(selectedCountry.value);
}

async function validateSelection(){
    console.log(selectedSong.value?.name)
}

</script>
<template>
    <div class="playlist-page">
      <Navbar />
      <h1>Playlist Creator</h1>
  
      <div class="form-group">
        <label for="country-select">Choisis un pays :</label>
        <select v-model="selectedCountry" id="country-select" @change="countryChange">
          <option disabled value="">-- Sélectionner --</option>
          <option v-for="country in countries" :key="country" :value="country">
            {{ country }}
          </option>
        </select>
      </div>
  
      <div class="form-group">
        <label for="song-select">Choisis une musique :</label>
        <select v-model="selectedSong" id="song-select">
          <option disabled value="">-- Sélectionner --</option>
          <option v-for="song in songsByCountryCible" :key="song" :value="song">
            {{ song['name'] }} - {{ song['artists'] }}
          </option>
        </select>
      </div>
  
      <button class="validate-button" @click="validateSelection">Valider</button>
    </div>
  </template>
  
<style scoped>
.playlist-page {
  max-width: 600px;
  margin: 80px auto;
  padding: 20px;
  background-color: #fafafa;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  font-family: 'Segoe UI', sans-serif;
  text-align: center;
}

h1 {
  margin-bottom: 30px;
  color: #333;
}

.form-group {
  margin-bottom: 20px;
  text-align: left;
  min-width: 50%;
  width: 50%;
}

label {
  display: block;
  margin-bottom: 8px;
  font-weight: 600;
  color: #555;
}

select {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border-radius: 6px;
  border: 1px solid #ccc;
  background-color: white;
  color: #555;
  box-sizing: border-box;
  min-width: 200%;
}

.validate-button {
  margin-top: 20px;
  padding: 12px 24px;
  font-size: 16px;
  border-radius: 6px;
  border: none;
  background-color: #4CAF50;
  color: white;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.validate-button:hover {
  background-color: #45a049;
}
</style>
