<template>
  <div class="flex-wrapper">
    <Header></Header>
    <div class="form-demo">
      <Dialog :visible="showSuccessMessage" :breakpoints="{ '960px': '80vw' }" :style="{ width: '30vw' }" position="top">
        <div class="flex align-items-center flex-column pt-6 px-3">
          <i class="pi pi-check-circle" :style="{fontSize: '5rem', color: 'var(--green-500)' }"></i>
          <h5 style="margin-top: 1em">New password created successfully!</h5>
          <p style="text-align: center">
            Your account now has your new password
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
          <h5 style="margin-top: 1em">Mail or verification number Error!</h5>
          <p style="text-align: center">
            Please enter a valid mail and verification number
          </p>
        </div>
        <template #footer>
          <div class="flex justify-content-center">
            <Button label="OK" @click="toggleDialogError" class="p-button-text" />
          </div>
        </template>
      </Dialog>

      <Dialog :visible="showPasswordMismatch" :breakpoints="{ '960px': '80vw' }" :style="{ width: '30vw' }" position="top">
        <div class="flex align-items-center flex-column pt-6 px-3">
          <i class="pi pi-info-circle" :style="{fontSize: '5rem', color: 'var(--red-500)' }"></i>
          <h5 style="margin-top: 1em">Password Error!</h5>
          <p style="text-align: center">
            Password mismatch
          </p>
        </div>
        <template #footer>
          <div class="flex justify-content-center">
            <Button label="OK" @click="toggleDialogMismatch" class="p-button-text" />
          </div>
        </template>
      </Dialog>

      <div class="flex justify-content-center">
        <div class="card">
          <h5 class="text-center" style="margin-bottom: -2rem; padding-top: 1rem">Recover password</h5>
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
                <InputText id="verificationNumber" v-model="v$.verificationNumber.$model" :class="{'p-invalid':v$.verificationNumber.$invalid && submitted}" />
                <label for="verificationNumber" :class="{'p-error':v$.verificationNumber.$invalid && submitted}">Verification number*</label>
              </div>
              <small v-if="(v$.verificationNumber.$invalid && submitted) || v$.verificationNumber.$pending.$response" class="p-error">{{v$.verificationNumber.required.$message.replace('Value', 'Name')}}</small>
            </div>
            <div class="field">
              <div class="p-float-label">
                <Password id="password" v-model="v$.password.$model" :class="{'p-invalid':v$.password.$invalid && submitted}" toggleMask>
                  <template #header>
                    <h6>Pick a password</h6>
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
                <label for="password" :class="{'p-error':v$.password.$invalid && submitted}">New password*</label>
              </div>
              <small v-if="(v$.password.$invalid && submitted) || v$.password.$pending.$response" class="p-error">{{v$.password.required.$message.replace('Value', 'Password')}}</small>
            </div>
            <div class="field">
              <div class="p-float-label">
                <Password id="confirmPassword" v-model="v$.confirmPassword.$model" :class="{'p-invalid':v$.confirmPassword.$invalid && submitted}" toggleMask>
                  <template #header>
                    <h6>Pick a password</h6>
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
                <label for="confirmPassword" :class="{'p-error':v$.confirmPassword.$invalid && submitted}">Confirm password*</label>
              </div>
              <small v-if="(v$.confirmPassword.$invalid && submitted) || v$.confirmPassword.$pending.$response" class="p-error">{{v$.confirmPassword.required.$message.replace('Value', 'Password')}}</small>
            </div>
            <div class="field">
              <Button id="submitButton" type="submit" label="Submit" class="mt-2"/>
            </div>
            <div class="field" style="margin-top: -1em">
              <label>Go back to <a class="link" @click="goToLogin" style="cursor: pointer; color: #8DD0FF; text-decoration: none; margin-top: -1em">Login</a></label>
            </div>
          </form>
        </div>
      </div>
    </div>
    <Footer></Footer>
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
  name: 'Reset',
  setup: () => ({ v$: useVuelidate() }),
  data () {
    return {
      email: this.$route.query.email,
      verificationNumber: this.$route.query.otp,
      password: '',
      confirmPassword: '',
      showSuccessMessage: false,
      showErrorMessage: false,
      showPasswordMismatch: false,
      submitted: false,
      error: ''
    }
  },
  validations () {
    return {
      email: {
        required,
        email
      },
      verificationNumber: {
        required
      },
      password: {
        required
      },
      confirmPassword: {
        required
      }
    }
  },
  methods: {
    resetPassword () {
      try {
        if (this.password === this.confirmPassword) {
          const headers = {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json'
          }
          const parameters = {
            email: this.email,
            otp: this.verificationNumber,
            password: this.password
          }
          const path = 'https://doogking.azurewebsites.net/api/reset/'
          axios.post(path, parameters, headers)
            .then((res) => {
              this.token = res.data.token
              this.showSuccessMessage = true
            })
            .catch((error) => {
              this.error = error
              this.showErrorMessage = true
            })
        } else {
          this.showPasswordMismatch = true
        }
      } catch (error) {
        this.showErrorMessage = true
      }
    },
    goToLogin () {
      this.$router.push({path: '/login'})
    },
    handleSubmit (isFormValid) {
      this.submitted = true

      if (isFormValid) {
        this.resetPassword()
      }
    },
    toggleDialogSuccess () {
      this.showSuccessMessage = !this.showSuccessMessage

      if (!this.showSuccessMessage) {
        this.goToLogin()
        this.resetForm()
      }
    },
    toggleDialogError () {
      this.showErrorMessage = !this.showErrorMessage

      if (!this.showErrorMessage) {
        this.email = ''
        this.verificationNumber = ''
      }
    },
    toggleDialogMismatch () {
      this.showPasswordMismatch = !this.showPasswordMismatch

      if (!this.showPasswordMismatch) {
        this.password = ''
        this.confirmPassword = ''
      }
    },
    resetForm () {
      this.email = ''
      this.password = ''
      this.confirmPassword = ''
      this.submitted = false
      this.verificationNumber = ''
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

.form-demo @media screen and (max-width: 960px) {
  .card {
    width: 80%;
  }
}
</style>
