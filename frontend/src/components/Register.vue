<template>
  <div class="flex-wrapper">
    <Header></Header>
  <div id="app">
    <div class="body">
      <div id="container-login" class="container">
        <div class="card" style="width: 30rem; color: white">
          <h3>Create account</h3>
          <h5>_____________________________________</h5>
          <div class="form-label-group">
            <label for="inputEmail">Email</label>
            <input type="email" id="inputEmail" class="form-control"
                   required autofocus v-model="addUserForm.email">
          </div>
          <div class="form-label-group">
            <label for="inputUsername">Username</label>
            <input type="username" id="inputUsername" class="form-control"
                   required autofocus v-model="addUserForm.username">
          </div>
          <div class="form-label-group">
            <label for="inputPassword">Password</label>
            <input type="password" id="inputPassword" class="form-control"
                   required v-model="addUserForm.password">
          </div>
          <!--<div class="form-label-group">
            <label for="inputStreet">Street</label>

            <input type="street" id="inputStreet" class="form-control"
                   required autofocus v-model="addUserForm.street">
          </div>
          <div class="form-label-group">

            <label for="inputStreetNumber">Street number</label>
            <input type="streetNumber" id="inputStreetNumber" class="form-control"
                   required autofocus v-model="addUserForm.streetNumber">
          </div>-->
          <div class="group-buttons">
            <button class="btn btn-lg btn-block" @click="checkRegister" name="createAccount">Create account</button>
            <button class="btn btn-lg btn-block" @click="goToLogin" name="goToLogIn">Login</button>
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
      email: null,
      username: null,
      password: null,
      // street: null,
      // streetNumber: null,
      token: null,
      addUserForm: {
        email: null,
        username: null,
        password: null
        // street: null,
        // streetNumber: null
      }
    }
  },
  methods: {
    checkLogin () {
      const parameters = {
        username: this.addUserForm.email,
        password: this.addUserForm.password
      }
      const headers = {'Access-Control-Allow-Origin': '*'}
      console.log(parameters)
      const path = 'https://doogking.azurewebsites.net/api/login/'
      axios.post(path, parameters, headers)
        .then((res) => {
          this.logged = true
          this.token = res.data.token
          this.$router.push({ path: '/', query: { username: this.addUserForm.username, logged: this.logged, token: this.token } })
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
          alert('Wrong username or password')
        })
    },
    checkRegister () {
      const headers = {'Access-Control-Allow-Origin': '*'}
      const parameters = {
        email: this.addUserForm.email,
        first_name: this.addUserForm.username,
        password: this.addUserForm.password
        // street: this.addUserForm.street,
        // street_number: this.addUserForm.streetNumber
      }
      const path = 'https://doogking.azurewebsites.net/api/profiles/'
      axios.post(path, parameters, headers)
        .then((res) => {
          this.checkLogin()
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
          alert('Wrong username or password')
        })
    },
    initCreateForm () {
      this.addUserForm.email = null
      this.addUserForm.username = null
      this.addUserForm.password = null
      // this.addUserForm.street = null
      // this.addUserForm.streetNumber = null
    },
    goToLogin () {
      // eslint-disable-next-line standard/object-curly-even-spacing
      this.$router.push({ path: '/login'})
    }
  },
  created () {
    this.initCreateForm()
  }
}
</script>
