<template>
  <form>
    <div class="flex-wrapper">
    <Header></Header>
    <div id="app">
      <div class="col-lg-6 col-md-12 m-auto">
        <b-alert v-model="showDismissibleAlert" variant="danger" dismissible>
          <h4 class="alert-heading">Oops, something went wrong</h4>
          <p>Please enter a valid username/password.</p>
        </b-alert>
      </div>
      <div class="body">
        <div id="container-login" class="container">
          <div v-if="!creatingAccount" class="card" style="width: 30rem; background-color: #4f5050; color: white">
            <h3>Iniciar sesión</h3>
            <hr>
            <div class="form-label-group">
              <label for="inputEmail">Username</label>
              <input type="username" id="inputUsername" class="form-control"
                     autofocus v-model="addUserForm.username" aria-describedby="inputGroupPrepend2" required>
            </div>
            <div class="form-label-group">
              <label for="inputPassword">Password</label>
              <input type="password" id="inputPassword" class="form-control" v-model="addUserForm.password" aria-describedby="inputGroupPrepend2" required>
            </div>
            <div class="group-buttons">
              <button class="btn btn-lg btn-block" type="submit" @click="checkLogin" name="signIn">Login</button>
              <button class="btn btn-lg btn-block" @click="goToRegister" name="createAccount">Create account</button>
            </div>
            <div class="forgotPassword-button">
              <button class="btn btn-lg btn-block" @click="goToForgotPassword" name="forgotPassword">Forgot Password</button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <Footer></Footer>
    </div>
  </form>
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
  margin-top: 1em;
  background-color: #6c757d;
  border-color: #6c757d;
  outline-style: none;
  border: none;
  color: white;
}
.group-buttons > :first-child {
  margin-top: 1em;
  background-color: #6c757d;
  border-color: #6c757d;
  outline-style: none;
  border: none;
  color: white;
}
.forgotPassword-button > :first-child {
  margin-top: 0.5em;
  background-color: #4F5050;
  border-color: #4F5050;
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
      },
      showDismissibleAlert: false
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
          this.showDismissibleAlert = true
        })
    },
    goToRegister () {
      // eslint-disable-next-line standard/object-curly-even-spacing
      this.$router.push({ path: '/register'})
    },
    goToForgotPassword () {
      // eslint-disable-next-line standard/object-curly-even-spacing
      this.$router.push({ path: '/forgotPassword'})
    }
  }
}
</script>
