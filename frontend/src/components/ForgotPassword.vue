<template>
  <form @submit.prevent="sendEmail">
    <div class="flex-wrapper">
      <Header></Header>
      <div class="body">
        <div class="col-lg-6 col-md-12 m-auto">
          <b-alert v-model="showDismissibleAlert" variant="danger" dismissible>
            <h4 class="alert-heading">Oops, something went wrong</h4>
            <p>Please enter a valid email.</p>
          </b-alert>
        </div>
        <div id="container-forgotPassword" class="container">
          <div v-if="!forgotPassword" class="card" style="width: 30rem; background-color: #4f5050; color: white">
          <h3>Forgot password ?</h3>
            <div class="form-group">
              <label>Enter the email adress associated with your account</label>
              <input type="email" name="email" class ="form-control" id="inputEmail" v-model="email" placeholder="Email"  aria-describedby="inputGroupPrepend2" required/>
            </div>
            <button class="btn btn-primary btn-block" id="Submit">Submit</button>
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
import axios from 'axios'
export default {
  components: {
    Header,
    Footer
  },
  name: 'ContactUs',
  data () {
    return {
      email: '',
      showDismissibleAlert: false
    }
  },
  methods: {
    sendEmail (e) {
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
        console.log({error})
        this.showDismissibleAlert = true
      }
    }
  }
}
</script>
