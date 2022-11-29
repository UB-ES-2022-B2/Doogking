<template>
  <form onsubmit="return false;">
    <div class="flex-wrapper">
      <Header></Header>
      <div id="app">
        <div class="body">
          <div class="d-flex flex-row">
            <div class="p-2" style="margin-left:50px">
              <img class="mx-auto rounded-circle" src="@/assets/avatar.png" style="width:200px">
            </div>
            <div class="p-2" style="margin-right:300px">
              <div class="info-containter" >
                <div class="form-label-group">
                  <label for="inputEmail" style="color:white">Email</label>
                  <input type="email" style="color: #2a323d" id="inputEmail" class="form-control"
                         autofocus v-model="addUserForm.email" aria-describedby="inputGroupPrepend2">
                </div>
                <div class="form-label-group">
                  <label for="inputUsername" style="color:white">Username</label>
                  <input type="username" style="color: #2a323d" id="inputUsername" class="form-control"
                         autofocus v-model="addUserForm.username" aria-describedby="inputGroupPrepend2">
                </div>
                <div class="group-buttons">
                  <button class="btn btn-lg btn-block" type="button" @click="goUpdateInfo">
                    Update Info</button>
                  <button class="btn btn-lg btn-block" type="button" @click="goToProfile">
                     Close</button>
                </div>
              </div>
            </div>
            <div class="changePassword-button" align-content="left">
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
      logged: null,
      username: null,
      email: null,
      user_id: null,
      token: null,
      showSuccessMessage: false,
      addUserForm: {
        email: null,
        username: null
      }
    }
  },
  methods: {
    goUpdateInfo () {
      var data = JSON.stringify({
        'email': this.addUserForm.email,
        'first_name': this.addUserForm.username
      })
      var config = {
        method: 'patch',
        url: 'https://doogking.azurewebsites.net/api/profiles/' + this.user_id + '/',
        headers: {
          'Authorization': 'Token' + this.token,
          'Content-Type': 'application/json'
        },
        data: data
      }
      axios(config)
        .then(function (response) {
        }).catch(function (response) {})
    },
    goToProfile () {
      this.$router.push({ path: '/profile', query: { username: this.username, logged: this.logged, token: this.token, email: this.email, user_id: this.user_id } })
    }
  },
  created () {
    this.logged = this.$route.query.logged === 'true'
    this.username = this.$route.query.username
    this.email = this.$route.query.email
    this.user_id = this.$route.query.user_id
    this.token = this.$route.query.token
    if (this.logged === undefined) {
      this.logged = false
    }
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
