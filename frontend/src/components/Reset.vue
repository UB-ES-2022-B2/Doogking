<template>
  <div class="flex-wraper">
   <Header></Header>
    <div id="app">
    <div class="body">
      <div id="container-reset" class="container">
        <div class="card" style="width: 30rem; background-color: #4f5050; color: white;">
          <h3>Reset password</h3>
          <h4>Enter the new password</h4>
          <h5>_____________________________________</h5>
          <div class="form-label-group"><label for="inputPassword">Password</label> <input id="inputPassword" class="form-control" required="" type="password" /></div>
          <div class="group-buttons"><button class="btn btn-lg btn-block" name="changePassword">Save</button></div>
        </div>
      </div>
    </div>
    </div>
   <Footer></Footer>
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
