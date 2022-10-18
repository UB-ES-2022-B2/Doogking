<template>
  <div class="flex-wrapper">
  <Header></Header>
  <div id="app">
    <div class="body">
      <div id="container-login" class="container">
        <div v-if="!creatingAccount" class="card" style="width: 30rem; background-color: #4f5050; color: white">
          <h3>Iniciar sesión</h3>
          <h5>_____________________________________</h5>
          <div class="form-label-group">
            <label for="inputEmail">Nombre de usuario</label>
            <input type="username" id="inputUsername" class="form-control"
                   required autofocus v-model="addUserForm.username">
          </div>
          <div class="form-label-group">
            <label for="inputPassword">Contraseña</label>
            <input type="password" id="inputPassword" class="form-control"
                   required v-model="addUserForm.password">
          </div>
          <div class="group-buttons">
            <button class="btn btn-lg btn-block" @click="checkLogin" name="signIn">Iniciar sesión</button>
            <button class="btn btn-lg btn-block" @click="goToRegister" name="createAccount">Crear cuenta</button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <Footer></Footer>
  </div>
</template>

<style scoped>
.flex-wrapper {
  display: flex;
  min-height: 100vh;
  flex-direction: column;
  justify-content: flex-start;
}

#container-login {
  padding: 2em;
  text-align: center;
}
.card {
  padding: 2em;
  margin: 0 auto;
}
.form-label-group {
  text-align: left;
}
.card > :not(:first-child) {
  margin-top: 1em;
}
.card > :first-child {
  margin-top: 0;
}
.group-buttons > :not(:first-child) {
  margin-top: 0;
  background-color: #6c757d;
  border-color: #6c757d;
  outline-style: none;
  border: none;
  color: white;
}
.group-buttons > :first-child {
  margin-top: 0;
  background-color: #6c757d;
  border-color: #6c757d;
  outline-style: none;
  border: none;
  color: white;
}

.btn:hover {
  color: #F06449;
  border-color: #6c757d;
}

</style>

<script>
import Header from './Header'
import Footer from './Footer'

import axios from 'axios'
export default {
  components: {
    Header,
    Footer
  },
  data () {
    return {
      logged: false,
      username: null,
      password: null,
      token: null,
      creatingAccount: false,
      addUserForm: {
        username: null,
        password: null
      }
    }
  },
  created () {
  },
  methods: {
    checkLogin () {
      const parameters = {
        username: this.addUserForm.username,
        password: this.addUserForm.password
      }
      const headers = {'Access-Control-Allow-Origin': '*'}
      console.log(parameters)
      const path = 'http://localhost:8000/api/login/'
      axios.post(path, parameters, headers)
        .then((res) => {
          this.logged = true
          this.token = res.data.token
          this.$router.push({ path: '/', query: { username: this.addUserForm.username, logged: this.logged, token: this.token } })
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
          alert('Usuari o contraseña incorrecte')
        })
    },
    goToRegister () {
      // eslint-disable-next-line standard/object-curly-even-spacing
      this.$router.push({ path: '/register'})
    }
  }
}
</script>
