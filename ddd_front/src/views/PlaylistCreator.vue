<script setup lang="ts">
import { onMounted, ref } from 'vue';
import Navbar from './Navbar.vue';
import { useRouter } from 'vue-router';
import {findCountries} from '../service/CountryService'
import {findSongsByCountry} from '../service/CountryService'
import {generatePlaylist} from '../service/SongService'
import { getUserGroups } from '../service/AuthService';

interface Song {
  name: string;
  artists: string;
}

const showModal = ref(false);

const router = useRouter();
const token = localStorage.getItem('token');
const countries = ref<string[]>([]);
const songsByCountrySource = ref<{}>([]);

const selectedCountrySource = ref<string>('');
const selectedCountryCible = ref<string>('');
const selectedSong = ref<Song| null>(null);

const resultSongSource = ref<string>('');
const resultSongSourceArtists = ref<string>('');
const resultTempo = ref<string>('');
const resultMode = ref<string>('');
const resultDanceability = ref<string>('');
const resultEnergy = ref<string>('');
const resultValence = ref<string>('');
const resultPlaylist = ref<Song[] | null>(null);

onMounted(async () => {
  const groups = await getUserGroups() as string[];
  let isAdmin = groups.includes('ddd_admin');
  let isPlaylistCreator = groups.includes('ddd_playlist_creator');
  console.log(groups);
  if (!token) {
    router.push('/login');
  }
  else if(token && isAdmin || isPlaylistCreator){
    countries.value = await findCountries();
  }
  else{
    router.push('/');
  }
});

async function countryChange(){
    songsByCountrySource.value = await findSongsByCountry(selectedCountrySource.value);
}

async function validateSelection(){
  let countrySource = selectedCountrySource.value;
  let songSource = selectedSong.value?.name;
  let countryCible = selectedCountryCible.value;
  let response;
  if(songSource){
    response = await generatePlaylist(countrySource, songSource, countryCible)
    resultSongSource.value = response['song_source'];
    resultSongSourceArtists.value = response['song_source_artists'];
    resultTempo.value = response['tempo'];
    resultMode.value = response['mode'];
    resultDanceability.value = response['danceability'];
    resultEnergy.value = response['energy'];
    resultValence.value = response['valence'];
    resultPlaylist.value = response['playlist_generated'];
    console.log(resultPlaylist.value)
    showModal.value = true;
  }
}

</script>
<template>
  <div class="playlist-page">
    <Navbar />
    <h1>Playlist Creator</h1>

    <div class="form-group">
      <label for="country-select">Choisis un pays source :</label>
      <select v-model="selectedCountrySource" id="country-select" @change="countryChange">
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
        <option v-for="song in songsByCountrySource" :key="song" :value="song">
          {{ song['name'] }} - {{ song['artists'] }}
        </option>
      </select>
    </div>

    <div class="form-group">
      <label for="country-select">Choisis un pays cible :</label>
      <select v-model="selectedCountryCible" id="country-select">
        <option disabled value="">-- Sélectionner --</option>
        <option v-for="country in countries" :key="country" :value="country">
          {{ country }}
        </option>
      </select>
    </div>

    <button class="validate-button" @click="validateSelection">Valider</button>
  </div>
  <!-- Lightbox -->
  <div v-if="showModal" class="modal-overlay" @click.self="showModal = false">
    <div class="modal-content">
      <h2>Résultat de la génération</h2>
      <div class="result-block">
        <h3>🎵 Chanson Source</h3>
        <p><strong>Nom :</strong> {{ resultSongSource }}</p>
        <p><strong>Artistes :</strong> {{ resultSongSourceArtists }}</p>
      </div>
      <div class="result-block">
        <h3>🎧 Caractéristiques</h3>
        <p><strong>Tempo :</strong> {{ resultTempo }}</p>
        <p><strong>Mode :</strong> {{ resultMode }}</p>
        <p><strong>Énergie :</strong> {{ resultEnergy }}</p>
        <p><strong>Positivité :</strong> {{ resultValence }}</p>
        <p><strong>Dansabilité :</strong> {{ resultDanceability }}</p>
      </div>
      <div class="result-block">
        <h3>📜 Playlist Générée</h3>
        <div v-if="resultPlaylist && resultPlaylist.length">
          <ul>
            <li v-for="(song, index) in resultPlaylist" :key="index">
              {{ song.name }} - {{ song.artists }}
            </li>
          </ul>
        </div>
        <div v-else>
          <p>Aucun résultat trouvé pour cette combinaison.</p>
        </div>
      </div>
      <button @click="showModal = false" class="close-btn">Fermer</button>
    </div>
  </div>
</template>
  
<style scoped>
.playlist-page {
  width: 600px;
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

/* LightBox */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 999;
}

.modal-content {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  max-width: 600px;
  width: 90%;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
  font-family: 'Segoe UI', sans-serif;
  text-align: left;
  color: #555;
  overflow-y: scroll;
  height: 80%;
}

.result-block {
  margin-bottom: 20px;
}

.result-block h3 {
  margin-bottom: 10px;
  color: #333;
}

.close-btn {
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #d9534f;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-weight: bold;
}

.close-btn:hover {
  background-color: #c9302c;
}
</style>
