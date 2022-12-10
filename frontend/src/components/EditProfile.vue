<template>
  <form onsubmit="return false;">
    <div class="flex-wrapper">
      <Header></Header>
      <Dialog :visible="showSuccessMessage" :breakpoints="{ '960px': '80vw' }" :style="{ width: '30vw' }" position="top">
        <div class="flex align-items-center flex-column pt-6 px-3">
          <i class="pi pi-info-circle" :style="{fontSize: '5rem', color: 'var(--green-500)' }"></i>
          <h5 style="margin-top: 1em">Edit Profile Successful!</h5>
          <p style="text-align: center">
            Your email/username has been changed
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
          <h5 style="margin-top: 1em">Edit Profile Error!</h5>
          <p style="text-align: center">
            Please enter a valid email/username
          </p>
        </div>
        <template #footer>
          <div class="flex justify-content-center">
            <Button label="OK" @click="toggleDialogError" class="p-button-text" />
          </div>
        </template>
      </Dialog>
      <Dialog :visible="imageProfileButton"  :style="{ width: '30vw' }" @update:visible="closeDialog" position="top">
        <div class="flex align-items-center flex-column pt-6 px-5">
          <h3>Upload your profile picture</h3>
          <FileUpload  name="demo[]" :customUpload="true" @uploader="myUploader($event)" :multiple="true" accept="image/*" :maxFileSize="1000000">
            <template #empty>
              <div class="flex align-items-center justify-content-center flex-column">
                <i class="pi pi-cloud-upload border-2 border-circle p-5 text-8xl text-400 border-400" />
                <p class="mt-4 mb-0">Drag and drop files here to upload.</p>
              </div>
            </template>
          </FileUpload>
        </div>
        <template #footer>
        </template>
      </Dialog>
      <div id="app">
        <div class="body">
          <h2 style="margin-right:150px; color: #8dd0ff">Hey {{username}}, edit your profile!</h2>
          <div class="d-flex flex-row">
            <div class="p-2" style="margin-left:50px">
              <img class="mx-auto rounded-circle" :src="profileImage" style="width:200px">
              <div class="group-buttons">
                <button class="btn btn-lg btn-block" type="submit" @click="goToChangeProfileImage">Update Profile</button>
              </div>
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
              <button class="btn btn-lg btn-block" type="submit" style="color: #8dd0ff" @click="goToChangePassword" name="editProfile" aria-label="Left Align"><fa :icon="['fas', 'unlock']"/><h6>Change Password</h6></button>
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
      showErrorMessage: false,
      imageProfileButton: false,
      profileImage: null,
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
    goToProfile () {
      this.$router.push({path: '/profile'})
    },
    goToChangePassword () {
      this.$router.push({path: '/changePassword'})
    },
    goToChangeProfileImage () {
      this.imageProfileButton = true
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
        .then((response) => {
          console.log(JSON.stringify(response.data))
          this.showSuccessMessage = true
        })
        .catch((error) => {
          this.error = error
          this.showErrorMessage = true
        })
    },
    toggleDialogSuccess () {
      this.showSuccessMessage = !this.showSuccessMessage
      if (!this.showSuccessMessage) {
        this.$router.push({ path: '/profile' })
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
      this.addUserForm.email = ''
      this.addUserForm.username = ''
      this.addUserForm.newPassword2 = ''
      this.submitted = false
    },
    myUploader (event) {
      const formData = new FormData()
      formData.append('image', event.files[0])
      var config = {
        method: 'patch',
        url: 'https://doogking.azurewebsites.net/api/profiles/' + this.userId + '/',
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Authorization': 'Token ' + this.token,
          'Content-Type': 'multipart/form-data'
        },
        data: formData
      }
      console.log('Token ' + this.token)
      axios(config)
        .then((response) => {
          this.showSuccessMessage = true
        }).catch(function (response) {})
    },
    closeDialog () {
      this.imageProfileButton = false
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
