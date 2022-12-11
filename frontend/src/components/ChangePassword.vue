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
            <img class="mx-auto rounded-circle" :src="profileImage" style="width:200px">
          </div>
          <div class="p-2" style="margin-right:400px">
            <div class="info-containter" >
              <div class="field">
                <div class="p-float-label">
                  <Password id="oldPassword" v-model="v$.oldPassword.$model" :class="{'p-invalid':v$.oldPassword.$invalid && submitted}" toggleMask>
                    <template #header>
                      <h6>Enter your password</h6>
                    </template>
                  </Password>
                  <label for="oldPassword" :class="{'p-error':v$.oldPassword.$invalid && submitted}">Password*</label>
                </div>
                <small v-if="(v$.oldPassword.$invalid && submitted) || v$.oldPassword.$pending.$response" class="p-error">{{v$.oldPassword.required.$message.replace('Value', 'oldPassword')}}</small>
              </div>
              <div class="field">
                <div class="p-float-label">
                  <Password id="NewPassword" v-model="v$.newPassword.$model" :class="{'p-invalid':v$.newPassword.$invalid && submitted}" toggleMask>
                    <template #header>
                      <h6>Enter your new password</h6>
                    </template>
                  </Password>
                  <label for="NewPassword" :class="{'p-error':v$.newPassword.$invalid && submitted}">New Password*</label>
                </div>
                <small v-if="(v$.newPassword.$invalid && submitted) || v$.newPassword.$pending.$response" class="p-error">{{v$.newPassword.required.$message.replace('Value', 'newPassword')}}</small>
              </div>
              <div class="field">
                <div class="p-float-label">
                  <Password id="NewPassword2" v-model="v$.newPassword2.$model" :class="{'p-invalid':v$.newPassword2.$invalid && submitted}" toggleMask>
                    <template #header>
                      <h6>Repeat your new password</h6>
                    </template>
                  </Password>
                  <label for="NewPassword2" :class="{'p-error':v$.newPassword2.$invalid && submitted}">Repeat new Password*</label>
                </div>
                <small v-if="(v$.newPassword2.$invalid && submitted) || v$.newPassword2.$pending.$response" class="p-error">{{v$.newPassword2.required.$message.replace('Value', 'newPassword2')}}</small>
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
import {required} from '@vuelidate/validators'
import { useVuelidate } from '@vuelidate/core'

export default {
  components: {
    Header,
    Footer
  },
  setup: () => ({ v$: useVuelidate() }),
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
      submitted: false,
      profileImage: null,
      addUserForm: {
        oldPassword: null,
        newPassword: null,
        newPassword2: null
      },
      showLoginMessage: false
    }
  },
  validations () {
    return {
      oldPassword: {
        required
      },
      newPassword2: {
        required
      },
      newPassword: {
        required
      }
    }
  },
  methods: {
    goUpdatePassword () {
      var data = {
        'email': this.email,
        'old_password': this.oldPassword,
        'new_password': this.newPassword,
        'new_password2': this.newPassword2
      }
      var config = {
        method: 'post',
        url: 'https://doogking.azurewebsites.net/api/change-password/',
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
          this.showSuccessMessage = true
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
      this.oldPassword = ''
      this.newPassword = ''
      this.newPassword2 = ''
      this.submitted = false
    },
    getProfileImage () {
      // const pathHouses = 'http://127.0.0.1:8000/api/housing/'
      var config = {
        method: 'get',
        url: 'https://doogking.azurewebsites.net/api/profiles/' + this.userId + '/',
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Authorization': 'Token ' + this.token,
          'Content-Type': 'multipart/form-data'
        }
      }
      console.log('Token ' + this.token)
      axios(config)
        .then(response => {
          (this.profileImage = response.data.image)
          console.log(this.profileImage)
        })
        .catch(function (response) {
        })
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
    if (localStorage.userId) {
      this.userId = localStorage.userId
    }
    if (localStorage.token) {
      this.token = localStorage.token
    }
    this.getProfileImage()
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
