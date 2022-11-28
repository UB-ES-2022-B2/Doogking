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
                <form @submit.prevent="handleSubmit(!v$.$invalid)" class="p-fluid">
                  <div class="field">
                    <hr style="margin-bottom: 1.5rem;" class="solid"/>
                    <div class="p-float-label">
                      <InputText id="username" v-model="v$.username.$model" :class="{'p-invalid':v$.username.$invalid && submitted}" />
                      <label for="username" :class="{'p-error':v$.username.$invalid && submitted}">Username*</label>
                    </div>
                    <small v-if="(v$.username.$invalid && submitted) || v$.username.$pending.$response" class="p-error">{{v$.username.required.$message.replace('Value', 'Name')}}</small>
                  </div>
                  <div class="field">
                    <div class="p-float-label p-input-icon-right">
                      <i class="pi pi-envelope" />
                      <InputText id="email" v-model="v$.email.$model" :class="{'p-invalid':v$.email.$invalid && submitted}" aria-describedby="email-error"/>
                      <label for="email" :class="{'p-error':v$.email.$invalid && submitted}">Email*</label>
                    </div>
                    <span v-if="v$.email.$error && submitted">
                            <span id="email-error" v-for="(error, index) of v$.email.$errors" :key="index">
                            <small class="p-error">{{error.$message}}</small>
                            </span>
                        </span>
                    <small v-else-if="(v$.email.$invalid && submitted) || v$.email.$pending.$response" class="p-error">{{v$.email.required.$message.replace('Value', 'Email')}}</small>
                  </div>
                </form>
                <div class="group-buttons">
                  <button class="btn btn-lg btn-block" type="submit" @click="goToProfile" name="editProfile">
                    Update Info</button>
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
      token: null
    }
  },
  methods: {
    goToProfile () {
      const parameters = {
        username: this.email,
        password: this.password
      }
      const headers = {'Access-Control-Allow-Origin': '*'}
      console.log(parameters)
      const path = 'https://doogking.azurewebsites.net/api/profile/'
      axios.post(path, parameters, headers)
        .then((res) => {
          this.logged = true
          this.token = res.data.token
          this.showSuccessMessage = true
          this.username = res.data.profile.first_name + res.data.profile.last_name
          this.user_id = res.data.profile.id
        })
        .catch((error) => {
          // eslint-disable-next-line
          this.error = error
          this.showErrorMessage = true
        })
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
