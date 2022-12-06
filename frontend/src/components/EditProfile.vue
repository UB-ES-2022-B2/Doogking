<template>
  <form onsubmit="return false;">
    <div class="flex-wrapper">
      <Header></Header>
      <Dialog :visible="showLoginMessage" :breakpoints="{ '960px': '80vw' }" :style="{ width: '30vw' }" position="top">
        <div class="flex align-items-center flex-column pt-6 px-3">
          <i class="pi pi-info-circle" :style="{fontSize: '5rem', color: 'var(--red-500)' }"></i>
          <h5 style="margin-top: 1em">Login Error!</h5>
          <p style="text-align: center">
            You need to be logged in to access your profile
          </p>
        </div>
        <template #footer>
          <div class="flex justify-content-center">
            <Button label="OK" @click="toggleDialogLogin" class="p-button-text" />
          </div>
        </template>
      </Dialog>
      <div id="app">
        <div class="body">
          <div class="d-flex flex-row">
            <div class="p-2" style="margin-left:50px">
              <img class="mx-auto rounded-circle" src="@/assets/avatar.png" style="width:200px">
            </div>
            <div class="p-2" style="margin-right:400px">
              <div class="info-containter" >
                <div class="form-label-group">
                  <label for="inputEmail" style="color:white">Email</label>
                  <input type="email" id="inputEmail" class="form-control"
                         autofocus v-model="addUserForm.email" aria-describedby="inputGroupPrepend2">
                </div>
                <div class="form-label-group">
                  <label for="inputUsername" style="color:white">Username</label>
                  <input type="username" id="inputUsername" class="form-control"
                         autofocus v-model="addUserForm.username" aria-describedby="inputGroupPrepend2">
                </div>
                <div class="group-buttons">
                  <button class="btn btn-lg btn-block" type="button" @click="goUpdateInfo">Update Info</button>
                  <button class="btn btn-lg btn-block" style="color: #8dd0ff" type="button" @click="goToProfile">Return</button>
                </div>
              </div>
            </div>
            <div>
              <button class="btn btn-lg btn-block" type="button" style="background-color: #D03739; color:white" @click="deleteProfile">Delete account</button>
            </div>
          </div>
        </div>
      </div>
      <Footer></Footer>
    </div>
  </form>
</template>
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
      email: null,
      userId: null,
      token: null,
      showSuccessMessage: false,
      addUserForm: {
        email: null,
        username: null
      },
      showLoginMessage: false
    }
  },
  methods: {
    goUpdateInfo () {
      if (this.addUserForm.email === null) {
        this.addUserForm.email = this.email
      } if (this.addUserForm.username === null) {
        this.addUserForm.username = this.username
      }
      var data = JSON.stringify({
        'email': this.addUserForm.email,
        'first_name': this.addUserForm.username
      })
      var config = {
        method: 'patch',
        url: 'https://doogking.azurewebsites.net/api/profiles/' + this.userId + '/',
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Authorization': 'Token ' + this.token,
          'Content-Type': 'application/json'
        },
        data: data
      }
      console.log('Token ' + this.token)
      axios(config)
        .then(function (response) {
        }).catch(function (response) {})
    },
    goToProfile () {
      this.$router.push({path: '/profile'})
    },
    deleteProfile () {
      var config = {
        method: 'delete',
        url: 'https://doogking.azurewebsites.net/api/deleteProfile/' + this.userId + '/',
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Authorization': 'Token ' + this.token,
          'Content-Type': 'application/json'
        }
      }
      axios(config)
        .then(function (response) {
        }).catch(function (response) {})
      this.logged = false
      this.$router.push({path: '/'})
    },
    toggleDialogLogin () {
      this.showLoginMessage = !this.showLoginMessage
      if (!this.showLoginMessage) {
        this.$router.push({path: '/'})
      }
    }
  },
  mounted () {
    if (localStorage.username) {
      this.logged = true
      this.username = localStorage.username
    }
    if (localStorage.userId) {
      this.userId = localStorage.userId
    }
    if (localStorage.token) {
      this.token = localStorage.token
    }
    if (localStorage.email) {
      this.email = localStorage.email
    }
    if (this.logged === false) {
      this.showLoginMessage = true
    }
  },
  created () {
  }
}
</script>

<style scoped>
.flex-wrapper {
  background-color: #2A323D;
  display: flex;
  min-height: 100vh;
  flex-direction: column;
  justify-content: flex-start;
  overflow-x: hidden;
  align-content: center;
}

.info-containter{
  text-align: left;
  padding-left: 60px;
  font-size: 16px;
}

.group-buttons > :first-child {
  margin-top: 0.5em;
  align-content: center;
  background-color: #8dd0ff;
  border-color: #2a323d;
  outline-style: none;
  border: none;
  color: #2a323d;
}
.changePassword-button > :first-child {
  margin-top: 0;
  align-content: center;
  background-color: white;
  outline-style: none;
  color: black;
}

.deleteAccount-button > :first-child {
  margin-top: 0;
  align-content: center;
  background-color: #CD3739;
  outline-style: none;
  color: white;
}
</style>
