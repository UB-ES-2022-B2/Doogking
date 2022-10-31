<template>
  <div class="flex-wraper">
   <Header></Header>
  <form>
    <h3>Reset Password</h3>
     <div class="form-group">
        <label>Email</label>
        <input type="text" class="form-control" v-model="email" placeholder="Email" required/>
      </div>
     <div class="form-group">
        <label>Verification number</label>
        <input type="text" class="form-control" v-model="verificationNumber" placeholder="Verification Number" required/>
      </div>
      <div class="form-group">
        <label>Password</label>
        <input type="password" class="form-control" v-model="password" placeholder="Password" required/>
      </div>
    <div class="form-group">
      <label>Password confirm</label>
      <input type="password" class="form-control" v-model="confirmPassword" placeholder="Password confirm" required/>
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
      email: this.$route.query.email,
      verificationNumber: this.$route.query.otp,
      password: '',
      confirmPassword: ''
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
          const path = 'https://doogking.awurewebsites.net/api/reset/'
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
