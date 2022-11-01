<template>
  <div class="flex-wraper">
   <Header></Header>
  <form>
    <h3>Reset Password</h3>
    <div class="form-group">
        <label>Verification number</label>
        <input type="password" class="form-control" id="verificationPassword" v-model="verificationNumber" placeholder="Verification Number" required/>
      </div>
      <div class="form-group">
        <label>Password</label>
        <input type="password" class="form-control" id="password" v-model="password" placeholder="Password" required/>
      </div>
    <div class="form-group">
      <label>Password confirm</label>
      <input type="password" class="form-control" v-model="confirmPassword" id="passwordConfirm" placeholder="Password confirm" required/>
    </div>
    <button class="btn btn-primary btn-block" @click="resetPassword">Submit</button>
  </form>
    </div>
</template>

<script>
// import axios from "axios"

import Header from './Header'
import Footer from './Footer'
import axios from 'axios'
export default {
  components: {
    Header,
    Footer
  },
  name: 'ContactUs',
  data () {
    return {
      verificationNumber: '',
      password: ' ',
      confirmPassword: ' '
    }
  },
  methods: {
    resetPassword () {
      try {
        if (this.password === this.confirmPassword) {
          const headers = {'Access-Control-Allow-Origin': '*'}
          const parameters = {
            verificationNumber: this.verificationNumber,
            password: this.password
          }
          const path = 'AFEGIRENDPOINT'
          axios.get(path, parameters, headers)
            .then((res) => {
              this.token = res.data.token
            })
          this.$router.push({path: '/'})
        } else {
          alert('Password Mismatch!')
        }
      } catch (error) {
        // eslint-disable-next-line
        console.log({error})
      }
    }
  }
}
</script>
