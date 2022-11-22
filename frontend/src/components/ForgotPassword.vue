<template>
  <div class="flex-wrapper">
    <Header></Header>
    <div class="form-demo">
      <Dialog :visible="showErrorMessage" :breakpoints="{ '960px': '80vw' }" :style="{ width: '30vw' }" position="top">
        <div class="flex align-items-center flex-column pt-6 px-3">
          <i class="pi pi-info-circle" :style="{fontSize: '5rem', color: 'var(--red-500)' }"></i>
          <h5 style="margin-top: 1em">Registration Error!</h5>
          <p style="text-align: center">
            Please enter a valid email
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
            <div class="field" style="margin-top: -0.5em">
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
import {email, required} from '@vuelidate/validators'
import { useVuelidate } from '@vuelidate/core'

export default {
  components: {
    Header,
    Footer
  },
  setup: () => ({ v$: useVuelidate() }),
  name: 'ForgotPassword',
  data () {
    return {
      email: '',
      showSuccessMessage: false,
      showErrorMessage: false,
      submitted: false,
      error: ''
    }
  },
  validations () {
    return {
      email: {
        required,
        email
      }
    }
  },
  methods: {
    handleSubmit (isFormValid) {
      this.submitted = true

      if (isFormValid) {
        this.sendEmail()
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
      this.submitted = false
    },
    goToLogin () {
      // eslint-disable-next-line standard/object-curly-even-spacing
      this.$router.push({ path: '/login'})
    },
    sendEmail () {
      try {
        const headers = {'Access-Control-Allow-Origin': '*'}
        const path = 'https://doogking.azurewebsites.net/api/reset/?email=' + this.email
        console.log(path)
        axios.get(path, headers)
          .then((res) => {
            this.token = res.data.token
          })
        // eslint-disable-next-line standard/object-curly-even-spacing
        this.$router.push({path: '/reset'})
      } catch (error) {
        // eslint-disable-next-line
        this.error = error
        this.showErrorMessage = true
      }
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
