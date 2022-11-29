<template>
  <div>
    <div class="flex-wrapper">
      <Header></Header>
      <div class="form-demo">
        <Dialog :visible="showSuccessMessage" :breakpoints="{ '960px': '80vw' }" :style="{ width: '30vw' }" position="top">
          <div class="flex align-items-center flex-column pt-6 px-3">
            <i class="pi pi-check-circle" :style="{fontSize: '5rem', color: 'var(--green-500)' }"></i>
            <h5 style="margin-top: 1em">Login Successful!</h5>
            <p style="text-align: center">
              Your account is logged in under username <b>{{ this.username }}</b>
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
            <h5 style="margin-top: 1em">Login Error!</h5>
            <p style="text-align: center">
              Please enter a valid email/password
            </p>
          </div>
          <template #footer>
            <div class="flex justify-content-center">
              <Button label="OK" @click="toggleDialogError" class="p-button-text" />
            </div>
          </template>
        </Dialog>

        <div class="flex justify-content-center">
          <div class="card">
            <h5 class="text-center" style="margin-bottom: -2rem; padding-top: 1rem">Login</h5>
            <form @submit.prevent="handleSubmit(!v$.$invalid)" class="p-fluid">
              <div class="field">
                <hr style="margin-bottom: 1.5rem;" class="solid"/>
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
              <div class="field">
                <div class="p-float-label">
                  <Password id="password" v-model="v$.password.$model" :class="{'p-invalid':v$.password.$invalid && submitted}" toggleMask>
                    <template #header>
                      <h6>Enter your password</h6>
                    </template>
                    <template #footer="sp">
                      {{sp.level}}
                      <Divider />
                      <p class="mt-2">Suggestions</p>
                      <ul class="pl-2 ml-2 mt-0" style="line-height: 1.5">
                        <li>At least one lowercase</li>
                        <li>At least one uppercase</li>
                        <li>At least one numeric</li>
                        <li>Minimum 8 characters</li>
                      </ul>
                    </template>
                  </Password>
                  <label for="password" :class="{'p-error':v$.password.$invalid && submitted}">Password*</label>
                </div>
                <small v-if="(v$.password.$invalid && submitted) || v$.password.$pending.$response" class="p-error">{{v$.password.required.$message.replace('Value', 'Password')}}</small>
              </div>
              <div class="field" style="margin-top: -1em">
                <label>Forgot your password? <a class="link" @click="goToForgotPassword" style="cursor: pointer; color: #8DD0FF; text-decoration: none; margin-top: -1em">Recover it now!</a></label>
              </div>
              <div class="field" style="margin-top: -1em">
                <Button id="submitButton" type="submit" label="Submit" class="mt-2"/>
              </div>
              <div class="field" style="margin-top: -1em">
                <label>Don't have an account yet? <a class="link" @click="goToRegister" style="cursor: pointer; color: #8DD0FF; text-decoration: none; margin-top: -1em">Register now!</a></label>
              </div>
            </form>
          </div>
        </div>
      </div>
      <Footer></Footer>
    </div>
  </div>
</template>

<script>
import Header from './Header'
import Footer from './Footer'
import axios from 'axios'
import { email, required } from '@vuelidate/validators'
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
      token: null,
      email: '',
      username: '',
      user_id: null,
      password: '',
      submitted: false,
      showSuccessMessage: false,
      showErrorMessage: false,
      error: ''
    }
  },
  validations () {
    return {
      email: {
        required,
        email
      },
      password: {
        required
      }
    }
  },
  created () {
  },
  methods: {
    handleSubmit (isFormValid) {
      this.submitted = true
      if (isFormValid) {
        this.checkLogin()
      }
    },
    toggleDialogSuccess () {
      this.showSuccessMessage = !this.showSuccessMessage
      if (!this.showSuccessMessage) {
        this.$router.push({ path: '/', query: { username: this.username, logged: this.logged, token: this.token, email: this.email, user_id: this.user_id } })
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
      this.email = ''
      this.password = ''
      this.submitted = false
    },
    checkLogin () {
      const parameters = {
        username: this.email,
        password: this.password
      }
      const headers = {'Access-Control-Allow-Origin': '*'}
      console.log(parameters)
      const path = 'https://doogking.azurewebsites.net/api/login/'
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

.form-demo .card {
  margin-top: 1.5rem;
  border-radius: 1rem;
  min-width: 30rem;
  background-color: #3d4755;
  color: white;
  margin-bottom: 1.5rem;
}

.form-demo .card form{
  margin-top: 2rem;
}

.form-demo .card .field{
  margin-bottom: 1.5rem;
  margin-left: 1rem;
  margin-right: 1rem;
}

.form-demo .card .field-checkbox{
  margin-bottom: 1.5rem;
  margin-left: 1rem;
  margin-right: 1rem;
}

.form-demo @media screen and (max-width: 960px) {
  .card {
    width: 80%;
  }
}
</style>
