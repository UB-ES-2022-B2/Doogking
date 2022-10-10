<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>

<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark" >
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo03" aria-controls="navbarTogglerDemo03" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <a class="navbar-brand" style="color: #FFFFFF; margin-left: 1em; font-size: 2em;">DoogKing</a>
    </nav>
    <div v-if="creatingAccount==false" class="container">
      <h1 style="margin-left: 10.5em;">Iniciar sesión</h1>
      <div>
        <b-form @submit="onSubmitLogin" @reset="onResetLogin">
          <b-form-group
            id="input-group-1"
            label="Nombre de usuario"
            label-for="input-1"
          >
            <b-form-input
              id="input-1"
              v-model="loginForm.username"
              type="username"
              placeholder="Introduce tu nombre de usuario"
              required
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-2" label="Contraseña" label-for="input-2">
            <b-form-input
              id="input-2"
              v-model="loginForm.password"
              placeholder="Introduce la contraseña"
              required
            ></b-form-input>
          </b-form-group>

          <b-button type="submit" variant="primary">Confirmar</b-button>
          <b-button type="reset" variant="danger">Borrar</b-button>
        </b-form>
      </div>
      <button class="btn btn-success btn-lg" style="margin-top: 0.3em; margin-left: 22.35em; height: 2em; width: 12em; background-color: #181817; border-color: #181817;" @click="goToCreateAccount">Crear Cuenta</button>
      <button class="btn btn-success btn-lg" style="margin-top: 0.3em; margin-left: 22.35em; height: 2em; width: 12em; background-color: #00d200; border-color: #00d200;" @click="backToMatches">Volver a inicio</button>
    </div>
    <div v-else class="container">
      <h1 style="margin-left: 10.6em;">Crear cuenta</h1>
      <div>
        <b-form @submit="onSubmitCreate" @reset="onResetCreate">
          <b-form-group
            id="input-group-1"
            label="Nombre de usuario"
            label-for="input-1"
          >
            <b-form-input
              id="input-1"
              v-model="addUserForm.username"
              type="username"
              placeholder="Introduce tu nombre de usuario"
              required
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-2" label="Contraseña" label-for="input-2">
            <b-form-input
              id="input-2"
              v-model="addUserForm.password"
              placeholder="Introduce la contraseña"
              required
            ></b-form-input>
          </b-form-group>

          <b-button type="submit" variant="primary">Confirmar</b-button>
          <b-button type="reset" variant="danger">Borrar</b-button>
        </b-form>
      </div>
      <button class="btn btn-success btn-lg" style="margin-top: 0.3em; margin-left: 22.35em; height: 2em; width: 12em; background-color: #00d200; border-color: #00d200;" @click="backToLogin">Iniciar sesión</button>
    </div>
  </div>
</template>
<script>

import axios from 'axios'
export default {
  data () {
    return {
      logged: false,
      token: null,
      creatingAccount: false,
      loginForm: {
        username: null,
        password: null
      },
      addUserForm: {
        username: null,
        password: null
      }
    }
  },
  methods: {
    goToCreateAccount () {
      this.creatingAccount = true
    },
    backToLogin () {
      this.creatingAccount = false
    },
    backToMatches () {
      this.$router.push({ path: '/' })
    },
    initLoginForm () {
      this.loginForm.username = null
      this.loginForm.password = null
    },
    initCreateForm () {
      this.creatingAccount = true
      this.addUserForm.username = null
      this.addUserForm.password = null
    },
    checkLogin () {
      const parameters = {
        username: this.loginForm.username,
        password: this.loginForm.password
      }
      const path = 'http://localhost:5000/login'
      axios.post(path, parameters)
        .then((res) => {
          this.logged = true
          this.token = res.data.token
          this.$router.push({ path: '/', query: { username: this.loginForm.username, logged: this.logged, token: this.token } })
          this.initLoginForm()
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
          alert(error.response)
        })
    },
    register () {
      const parameters = {
        username: this.addUserForm.username,
        password: this.addUserForm.password
      }
      const path = 'http://localhost:5000/account'
      axios.post(path, parameters)
        .then(() => {
          alert('User registered')
          this.backToLogin()
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error)
          alert(error.response)
        })
    },
    onSubmitLogin (event) {
      event.preventDefault()
      this.checkLogin()
    },
    onResetLogin (event) {
      event.preventDefault()
      // Reset our form values
      this.initLoginForm()
    },
    onSubmitCreate (event) {
      event.preventDefault()
      this.register()
    },
    onResetCreate (event) {
      event.preventDefault()
      // Reset our form values
      this.initCreateForm()
    }
  },
  created () {
  }
}
</script>
