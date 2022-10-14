<template>
  <div>
    <Header></Header>
  <div id="app">
    <div class="body">
      <div id="container-login" class="container">
        <div class="card" style="width: 30rem; color: white">
          <h3>Crear Cuenta</h3>
          <h5>_____________________________________</h5>
          <div class="form-label-group">
            <label for="inputEmail">Email</label>
            <input type="email" id="inputUsername" class="form-control"
                   required autofocus v-model="addUserForm.email">
          </div>
          <div class="form-label-group">
            <label for="inputPassword">Nombre de usuario</label>
            <input type="username" id="inputPassword" class="form-control"
                   required autofocus v-model="addUserForm.username">
          </div>
          <div class="form-label-group">
            <label for="inputPassword">Contraseña</label>
            <input type="password" id="inputPassword" class="form-control"
                   required v-model="addUserForm.password">
          </div>
          <div class="form-label-group">
            <label for="inputPassword">Calle</label>
            <input type="street" id="inputPassword" class="form-control"
                   required autofocus v-model="addUserForm.street">
          </div>
          <div class="form-label-group">
            <label for="inputPassword">Número de calle</label>
            <input type="streetNumber" id="inputPassword" class="form-control"
                   required autofocus v-model="addUserForm.streetNumber">
          </div>
          <div class="group-buttons">
            <button class="btn btn-lg btn-block" @click="sendDataTest" name="createAccount">Crear cuenta</button>
            <button class="btn btn-lg btn-block" @click="goToLogin" name="goToLogIn">Ir a iniciar sesión</button>
          </div>
        </div>
      </div>
    </div>
  </div>
    <Footer></Footer>
  </div>
</template>

<style scoped>
#container-login {
  padding: 2em;
  text-align: center;
}
.card {
  padding: 2em;
  margin: 0 auto;
  background-color: #4f5050;
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
        password: null,
        email: null,
        street: null,
        streetNumber: null
      }
    }
  },
  created () {
  },
  methods: {
    checkRegister () {
      const parameters = {
        username: this.username,
        password: this.password
      }
      const path = 'http://localhost:5000/login'
      axios.post(path, parameters)
        .then((res) => {
          this.token = res.data.token
          this.$router.push({ path: '/', query: { username: this.addUserForm.username, logged: true, token: this.token } })
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
          alert('Usuari o contraseña incorrecte')
        })
    },
    initCreateForm () {
      this.creatingAccount = true
      this.addUserForm.username = null
      this.addUserForm.password = null
    },
    backToLogIn () {
      this.creatingAccount = false
    },
    goToLogin () {
      // eslint-disable-next-line standard/object-curly-even-spacing
      this.$router.push({ path: '/login'})
    },
    sendDataTest () {
      this.logged = true
      this.$router.push({ path: '/', query: { username: this.addUserForm.username, logged: this.logged, token: this.token } })
    },
    sendCreateForm () {
      const path = 'http://localhost:5000/account'
      const parameters = {
        username: this.addUserForm.username,
        password: this.addUserForm.password
      }
      axios.post(path, parameters)
        .then((res) => {
          this.username = this.addUserForm.username
          this.password = this.addUserForm.password
          this.creatingAccount = false
          this.checkLogin()
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error)
          alert("L'usuari ja existeix!")
        })
    }
  }
}
</script>
