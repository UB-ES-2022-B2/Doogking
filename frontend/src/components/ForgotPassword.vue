<template>
  <form @submit.prevent="sendEmail">
    <h3>Forgot password</h3>
      <div class="form-group">
        <label>Email</label>
        <input type="email" name="email" class ="form-control" v-model="email" placeholder="Email"/>
      </div>
      <button class="btn btn-primary btn-block">Submit</button>
  </form>
</template>

<script>
import * as emailjs from 'emailjs-com'

export default {
  name: 'ContactUs',
  data () {
    return {
      email: '',
      reset_password: ''
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
        console.log({error})
      }
      this.$router.push({path: '/reset'})
    }
  }
}
</script>
