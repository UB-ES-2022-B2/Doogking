<template>
  <form onsubmit="return false;">
  <div class="flex-wrapper">
    <Header></Header>
    <Dialog :visible="showSuccessMessage" :breakpoints="{ '960px': '80vw' }" :style="{ width: '30vw' }" position="top">
      <div class="flex align-items-center flex-column pt-6 px-3">
        <i class="pi pi-info-circle" :style="{fontSize: '5rem', color: 'var(--green-500)' }"></i>
        <h5 style="margin-top: 1em">Change Profile Successful!</h5>
        <p style="text-align: center">
          Your password has been changed
        </p>
      </div>
      <template #footer>
        <div class="flex justify-content-center">
          <Button label="OK" @click="toggleDialogSuccess" class="p-button-text" />
        </div>
      </template>
    </Dialog>
    <Dialog :visible="showErrorMessage" :breakpoints="{ '960px': '80vw' }" :style="{ width: '30vw' }" position="top">
    <div class="flex align-items-center flex-column pt-6 px-3">
      <i class="pi pi-info-circle" :style="{fontSize: '5rem', color: 'var(--red-500)' }"></i>
      <h5 style="margin-top: 1em">Change Password Error!</h5>
      <p style="text-align: center">
        Please enter a valid password
      </p>
    </div>
    <template #footer>
      <div class="flex justify-content-center">
        <Button label="OK" @click="toggleDialogError" class="p-button-text" />
      </div>
    </template>
    </Dialog>
    <div id="app">
      <div class="body">
        <h2 style="margin-right:300px; color: #8dd0ff">Change your password</h2>
        <div class="d-flex flex-row">
          <div class="p-2" style="margin-left:50px">
            <img class="mx-auto rounded-circle" src="@/assets/avatar.png" style="width:200px">
          </div>
          <div class="p-2" style="margin-right:400px">
            <div class="info-containter" >
              <div class="form-label-group">
                <label for="inputOldPassword" style="color:white">Password</label>
                <input type="OldPassword" id="inputOldPassword" class="form-control"
                       autofocus v-model="addUserForm.oldPassword" aria-describedby="inputGroupPrepend2">
              </div>
              <div class="form-label-group">
                <label for="inputNewPassword" style="color:white">New Password</label>
                <input type="NewPassword" id="inputUsername" class="form-control"
                       autofocus v-model="addUserForm.newPassword" aria-describedby="inputGroupPrepend2">
              </div>
              <div class="form-label-group">
                <label for="inputNewPassword2" style="color:white">Repeat New Password</label>
                <input type="NewPassword2" id="inputNewPassword2" class="form-control"
                       autofocus v-model="addUserForm.newPassword2" aria-describedby="inputGroupPrepend2">
              </div>
              <div class="group-buttons">
                <button class="btn btn-lg btn-block" type="button" @click="goUpdatePassword">Update Password</button>
                <button class="btn btn-lg btn-block" style="color: #8dd0ff" type="button" @click="goToEditProfile">Return</button>
              </div>
            </div>
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
      oldPassword: null,
      newPassword: null,
      newPassword2: null,
      showSuccessMessage: false,
      showErrorMessage: false,
      addUserForm: {
        oldPassword: null,
        newPassword: null,
        newPassword2: null
      },
      showLoginMessage: false
    }
  },
  methods: {
    goUpdatePassword () {
      var data = JSON.stringify({
        'email': this.email,
        'old_password': this.addUserForm.oldPassword,
        'new_password': this.addUserForm.newPassword,
        'new_password2': this.addUserForm.newPassword2
      })
      var config = {
        method: 'post',
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
        .then((response) => {
          console.log(JSON.stringify(response.data))
          this.showErrorMessage = true
        })
        .catch((error) => {
          this.error = error
          this.showErrorMessage = true
        })
    },
    goToEditProfile () {
      this.$router.push({path: '/editProfile'})
    },
    handleSubmit (isFormValid) {
      this.submitted = true
      if (isFormValid) {
        this.checkLogin()
      }
    },
    toggleDialogSuccess () {
      this.showSuccessMessage = !this.showSuccessMessage
      if (!this.showSuccessMessage) {
        this.$router.push({ path: '/editProfile' })
        this.resetForm()
      }
    },
    toggleDialogError () {
      this.showErrorMessage = !this.showErrorMessage

      if (!this.showErrorMessage) {
        this.resetForm()
      }
    },
    resetForm () {
      this.addUserForm.oldPassword = ''
      this.addUserForm.newPassword = ''
      this.addUserForm.newPassword2 = ''
      this.submitted = false
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
