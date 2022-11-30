<template>
  <div>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid" style="margin-top:0.3em;">
      <!-- Navbar main links -->
      <div class="navbar-collapse collapse w-100 order-1 order-md-0 dual-collapse2" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <a class="navbar-brand" @click="goToHomepage" id="main_homepage" style="cursor: pointer; font-family: 'Brush Script MT'; font-size: 1.5em; margin-left: 0.5em;">
            <img src="@/assets/logoDog.png" id="main_logo" alt="" width="30" height="24" class="d-inline-block align-top" style="color: #8DD0FF;">
            Doogking
          </a>
          <li class="nav-item">
            <a v-if="this.$route.name ==='Homepage'" class="nav-link" @click="goToHomepage" style="color: #8DD0FF; cursor: pointer">Homepage</a>
            <a v-else class="nav-link" @click="goToHomepage" style="cursor: pointer">Homepage</a>
          </li>
          <li class="nav-item">
            <a v-if="this.$route.name ==='BusinessContact'" class="nav-link" style="color: #8DD0FF; cursor: pointer">Support</a>
            <a v-else class="nav-link" style="cursor: pointer" @click="goToBusinessContact">Support</a>
          </li>
          <li class="nav-item">
            <a v-if="this.$route.name ==='Property'" class="nav-link" style="color: #8DD0FF; cursor: pointer">House registry</a>
            <a href="https://doogking.azurewebsites.net/api/housing/" v-else class="nav-link" style="cursor: pointer" target="_blank">House registry</a>
          </li>
          <li class="nav-item">
            <a v-if="this.$route.name ==='AboutUs'" class="nav-link" @click="goToAboutUs" style="color: #8DD0FF; cursor: pointer"><fa :icon="['fas', 'circle-info'] " /></a>
            <a v-else class="nav-link" @click="goToAboutUs" style="cursor: pointer"><fa :icon="['fas', 'circle-info'] " /></a>
          </li>
        </ul>
      </div>
      <!-- User dropdown -->
      <ul class="nav navbar-nav navbar-right" v-if="logged===false">
        <div>
          <SplitButton label="Account" icon="pi pi-user" @click="goToLogin" :model="itemsNotLogged" class="p-button-secondary mb-2"></SplitButton>
        </div>
      </ul>
      <ul class="nav navbar-nav navbar-right" v-else>
        <div>
          <SplitButton :label="this.username" icon="pi pi-user" @click="goToProfile" :model="itemsLogged" class="p-button-secondary mb-2"></SplitButton>
        </div>
      </ul>
    </div>
  </nav>
    <div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      logged: null,
      itemsNotLogged: [
        {
          label: 'Login',
          icon: 'pi pi-sign-in',
          command: () => {
            this.goToLogin()
          }
        },
        {
          label: 'Register',
          icon: 'pi pi-user-plus',
          command: () => {
            this.goToRegister()
          }
        }
      ],
      itemsLogged: [
        {
          label: 'Profile',
          icon: 'pi pi-user',
          command: () => {
            this.goToProfile()
          }
        },
        {
          label: 'Log out',
          icon: 'pi pi-sign-out',
          command: () => {
            this.logOut()
          }
        }
      ],
      username: null,
      email: null,
      user_id: null,
      token: null
    }
  },
  methods: {
    goToRegister () {
      // eslint-disable-next-line standard/object-curly-even-spacing
      this.$router.push({ path: '/register'})
    },
    goToLogin () {
      // eslint-disable-next-line standard/object-curly-even-spacing
      this.$router.push({ path: '/login'})
    },
    goToProfile () {
      // eslint-disable-next-line standard/object-curly-even-spacing
      if (this.logged) {
        this.$router.push({ path: '/profile', query: { username: this.username, logged: this.logged, token: this.token, email: this.email, user_id: this.user_id } })
      }
    },
    goToAboutUs () {
      // eslint-disable-next-line standard/object-curly-even-spacing
      this.$router.push({ path: '/aboutUs', query: {username: this.username, logged: this.logged, token: this.token, email: this.email, user_id: this.user_id} })
    },
    logOut () {
      this.logged = false
      // eslint-disable-next-line standard/object-curly-even-spacing
      this.$router.push({ path: '/'})
    },
    goToBusinessContact () {
      // eslint-disable-next-line standard/object-curly-even-spacing
      this.$router.push({ path: '/businessContact', query: { username: this.username, logged: this.logged, token: this.token, email: this.email, user_id: this.user_id } })
    },
    goToHomepage () {
      // eslint-disable-next-line standard/object-curly-even-spacing
      if (this.logged) {
        this.$router.push({ path: '/', query: { username: this.username, logged: this.logged, token: this.token, email: this.email, user_id: this.user_id } })
      } else {
        // eslint-disable-next-line standard/object-curly-even-spacing
        this.$router.push({ path: '/'})
      }
    }
  },
  created () {
    this.logged = this.$route.query.logged === 'true'
    this.username = this.$route.query.username
    this.email = this.$route.query.email
    this.user_id = this.$route.query.user_id
    this.token = this.$route.query.token
    if (this.logged === undefined) {
      this.logged = false
    }
  }
}
</script>

<style scoped>
.navbar-brand {
  color: #8DD0FF;
}
.nav-item .nav-link {
  color: white;
}
.nav-item .nav-link:hover {
  color: #8DD0FF;
}

.loginIcon:hover{
  color: #8DD0FF;
}
</style>
