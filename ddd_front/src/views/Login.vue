<template>
    <div class="login-page">
      <h2>Connexion</h2>
      <form @submit.prevent="login">
        <input v-model="username" type="username" placeholder="Nom d'utilisateur" />
        <input v-model="password" type="password" placeholder="Mot de passe" />
        <button type="submit">Se connecter</button>
      </form>
    </div>
  </template>
  
  <script>
  import { login } from '@/service/AuthService'
  export default{
    data() {
      return {
        username: '',
        password: ''
      }
    },
    methods:{
        async login(){
            console.log(this.username)
            if(this.username && this.password){
                await login(this.username, this.password);
            }
        }
    }
  }
//   export default {
//     data() {
//       return {
//         email: '',
//         password: ''
//       }
//     },
//     methods: {
//       login() {
//         login()
//         // Authentification fictive
//         /*if (this.email && this.password) {
//           localStorage.setItem('auth', true)
//           this.$router.push('/dashboard')
//         }*/
//       }
//     }
//   }
  </script>