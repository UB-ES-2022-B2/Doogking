<template>
  <form @submit.prevent="sendEmail">
    <div class="flex-wrapper">
      <Header></Header>
      <div class="body">
        <div id="container-forgotPassword" class="container">
          <div v-if="!forgotPassword" class="card" style="width: 30rem; background-color: #4f5050; color: white">
          <h3>Forgot password ?</h3>
            <div class="form-group">
              <label>Enter the email adress associated with your account</label>
              <input type="email" name="email" class ="form-control" v-model="email" placeholder="Email"/>
            </div>
            <button class="btn btn-primary btn-block">Submit</button>
          </div>
        </div>
      </div>
    </div>
    <Footer></Footer>
  </form>
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
</style>

<script>
import Header from './Header'
import Footer from './Footer'
import * as emailjs from 'emailjs-com'
export default {
  components: {
    Header,
    Footer
  },
  name: 'ContactUs',
  data () {
    return {
      email: '',
      reset_password: '',
      forgotPassword: false
    }
  },
  methods: {
    sendEmail (e) {
      try {
        emailjs.sendForm('service_doogking', 'template_6flombd', e.target,
          'v_pteFmOs0hEWfD7U', {
            email: this.email
          })
      } catch (error) {
        // eslint-disable-next-line
        console.log({error})
      }
      // eslint-disable-next-line standard/object-curly-even-spacing
      this.$router.push({path: '/reset'})
    }
  }
}
</script>
