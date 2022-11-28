<template>
  <form onsubmit="return false;">
    <div class="flex-wrapper">
      <Header></Header>
      <div id="app">
        <div class="body">
          <div class="d-flex flex-row">
            <div class="p-2" style="margin-left:50px">
              <img class="mx-auto rounded-circle" src="@/assets/avatar.png" style="width:200px">
              <div class="profileButton-button">
                <button class="btn btn-lg btn-block" name="forgotPassword"><u>Uploado Photo</u></button>
              </div>
            </div>
            <div class="p-2" style="margin-right:300px">
              <div class="info-containter" >
                <div class="form-label-group">
                  <label for="inputEmail">Email</label>
                  <input type="email" id="inputEmail" class="form-control"
                         autofocus v-model="addUserForm.email" aria-describedby="inputGroupPrepend2">
                </div>
                <div class="form-label-group">
                  <label for="inputUsername">Username</label>
                  <input type="username" id="inputUsername" class="form-control"
                         autofocus v-model="addUserForm.username" aria-describedby="inputGroupPrepend2">
                </div>
                <div class="group-buttons">
                  <button class="btn btn-lg btn-block" type="button" @click="goUpdateInfo">
                    Update Info</button>
                  <button class="btn btn-lg btn-block" type="submit" @click="goToProfile" name="editProfile">
                    close</button>
                </div>
              </div>
            </div>
            <div class="changePassword-button" align-content="left">
              <button class="btn btn-lg btn-block" type="submit" name="changePassword" aria-label="Left Align"><fa :icon="['fas', 'unlock-alt']"/><h6>Change Password</h6></button>
            </div>
            <div class="deleteAccount-button" align-content="left">
              <button class="btn btn-lg btn-block" type="submit" name="deleteAccount" aria-label="Left Align">Delete Account</button>
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

.info-containter{
  text-align: left;
  padding-left: 60px;
  font-size: 16px;
}

.group-buttons > :first-child {
  margin-top: 50px;
  background-color: #6c757d;
  border-color: #6c757d;
  outline-style: none;
  border: none;
  color: white;
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
