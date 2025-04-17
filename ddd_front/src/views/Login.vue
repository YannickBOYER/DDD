<template>
  <div class="login-page">
    <h2>Connexion</h2>
    <form @submit.prevent="login" class="login-form">
      <input v-model="username" type="text" placeholder="Nom d'utilisateur" class="input-field" />
      <input v-model="password" type="password" placeholder="Mot de passe" class="input-field" />
      <button type="submit" class="submit-btn">Se connecter</button>
    </form>
  </div>
</template>

<script>
import { login } from '../service/AuthService';

export default {
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    async login() {
      console.log(this.username);
      if (this.username && this.password) {
        let isLogin = await login(this.username, this.password);
        if (isLogin) {
          this.$router.push('/');
        }
      }
    }
  }
};
</script>

<style scoped>
/* Style pour la page de connexion */
.login-page {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

h2 {
  margin-bottom: 20px;
  font-size: 2rem;
  color: #fff;
}

/* Style pour le formulaire */
.login-form {
  display: flex;
  flex-direction: column;
  gap: 15px;
  width: 100%;
  max-width: 400px;
  background-color: white;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

/* Style pour les champs de saisie */
.input-field {
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 100%;
}

/* Style pour le bouton de soumission */
.submit-btn {
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 10px 20px;
  font-size: 1rem;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.submit-btn:hover {
  background-color: #45a049;
}
</style>