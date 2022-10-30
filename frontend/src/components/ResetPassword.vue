<template>
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
</template>

<style scoped>

.flex-wrapper {
  display: flex;
  min-height: 100vh;
  flex-direction: column;
  justify-content: flex-start;
}

#container-reset {
  padding: 2em;
  text-align: center;
}
.card {
  padding: 2em;
  margin: 0 auto;
  background-color: #4f5050;
}
.form-label-group {
  text-align: left;
}
.card > :not(:first-child) {
  margin-top: 1em;
}
.card > :first-child {
  margin-top: 0;
}
.group-buttons > :not(:first-child) {
  margin-top: 0;
  background-color: #6c757d;
  border-color: #6c757d;
  outline-style: none;
  border: none;
  color: white;
}
.group-buttons > :first-child {
  margin-top: 0;
  background-color: #6c757d;
  border-color: #6c757d;
  outline-style: none;
  border: none;
  color: white;
}

.btn:hover {
  color: #F06449;
  border-color: #6c757d;
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
  data () {
    return {
      password: null,
      addUserForm: {
        password: null,
      }
    }
  },
  methods: {
    checkReset () {
      const parameters = {
        password: this.addUserForm.password
      }
      const headers = {'Access-Control-Allow-Origin': '*'}
      console.log(parameters)
      const path = 'https://doogking.azurewebsites.net/api/login/'
      axios.post(path, parameters, headers)
        .then((res) => {
          this.$router.push({ path: '/login' })
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
        })
    },
    initCreateForm () {
      this.addUserForm.password = null
    },
    goToLogin () {
      this.$router.push({ path: '/login'})
    }
  },
  created () {
    this.initCreateForm()
  }
}
</script>

