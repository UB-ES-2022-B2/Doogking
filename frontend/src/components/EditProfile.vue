<template>
  <form>
    <div class="flex-wrapper">
      <Header></Header>
      <div id="app">
        <div class="body">
          <div class="d-flex flex-row">
            <div class="p-2" style="margin-left:50px">
              <img class="mx-auto rounded-circle" src="@/assets/avatar.png" style="width:200px">
              <div class="profileButton-button">
                <button class="btn btn-lg btn-block" @click="goToUploadPhoto" name="forgotPassword"><u>Uploado Photo</u></button>
              </div>
            </div>
            <div class="p-2" style="margin-right:300px">
              <div class="info-containter" >
                <div>
                  <label for="inputEmail">Email</label>
                  <input type="email" id="inputEmail" class="form-control">
                </div>
                <div>
                  <label for="inputUsername" style="margin-top:20px">Username</label>
                  <input type="email" id="inputEmail" class="form-control">
                </div>
                <div class="group-buttons">
                  <button class="btn btn-lg btn-block" type="submit" @click="goToUpdateInfo" name="editProfile">
                    Update info</button>
                </div>
              </div>
            </div>
            <div class="changePassword-button" align-content="left">
              <button class="btn btn-lg btn-block" type="submit" @click="goToChangePassword" name="changePassword" aria-label="Left Align"><fa :icon="['fas', 'unlock-alt']"/><h6>Change Password</h6></button>
            </div>
            <div class="deleteAccount-button" align-content="left">
              <button class="btn btn-lg btn-block" type="submit" @click="goToDeleteAccount" name="deleteAccount" aria-label="Left Align">Delete Account</button>
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

export default {
  components: {
    Header,
    Footer
  },
  data () {
    return {
      email: null,
      username: null,
      password: null,
      token: null,
      logged: false
    }
  },
  created () {
    this.logged = this.$route.query.logged === 'true'
    this.username = this.$route.query.username
    this.email = this.$route.query.email
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
