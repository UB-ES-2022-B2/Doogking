<template>
  <div class="flex-wraper">
    <Header></Header>
    <div id="container-reset" class="container">
      <div class="card" style="width: 30rem; background-color: #4f5050; color: white;">
        <h3>Reset Password</h3>
        <div class="form-group">
          <label>Email</label>
          <input type="text" class="form-control" v-model="email" placeholder="Email" required/>
        </div>
        <div class="form-group">
          <label>Verification number</label>
          <input type="text" class="form-control" v-model="verificationNumber" placeholder="Verification Number"
                 required/>
        </div>
        <div class="form-group">
          <label>Password</label>
          <input type="password" class="form-control" v-model="password" placeholder="Password" required/>
        </div>
        <div class="form-group">
          <label>Password confirm</label>
          <input type="password" class="form-control" v-model="confirmPassword" placeholder="Password confirm"
                 required/>
        </div>
        <div class="submitButton">
        <button class="btn btn-lg btn-block" @click="resetPassword">Submit</button>
        </div>
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>
<style>
.flex-wrapper {
  display: flex;
  min-height: 75vh;
  flex-direction: column;
  justify-content: flex-start;
}
#container-forgotPassword {
padding: 1em;
text-align: center;
}
.card {
padding: 2em;
margin: 0 auto;
}
.submitButton > :first-child {
  margin-top: 0.5em;
  background-color: #4F5050;
  border-color: #4F5050;
  outline-style: none;
  border: none;
  color: white;
}
</style>
<script>
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
