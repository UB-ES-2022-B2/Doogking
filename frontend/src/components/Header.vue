<template>
  <div>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <!-- Navbar icon and brand -->
      <nav class="navbar navbar-dark">
        <div class="container-fluid">
          <a class="navbar-brand" @click="goToHomepage" style="cursor: pointer">
            <img src="@/assets/logoDog.png" alt="" width="30" height="24" class="d-inline-block align-top" style="color: #8DD0FF;">
            DOOGKING
          </a>
        </div>
      </nav>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <!-- Navbar main links -->
      <div class="navbar-collapse collapse w-100 order-1 order-md-0 dual-collapse2" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a v-if="this.$route.name ==='Homepage'" class="nav-link" @click="goToHomepage" style="color: #8DD0FF; cursor: pointer">Homepage</a>
            <a v-else class="nav-link" @click="goToHomepage" style="cursor: pointer">Homepage</a>
          </li>
          <li class="nav-item">
            <a v-if="this.$route.name ==='Help'" class="nav-link" style="color: #8DD0FF; cursor: pointer">Support</a>
            <a v-else class="nav-link" style="cursor: pointer">Support</a>
          </li>
          <li class="nav-item">
            <a v-if="this.$route.name ==='Property'" class="nav-link" style="color: #8DD0FF; cursor: pointer">House registry</a>
            <a v-else class="nav-link" style="cursor: pointer">House registry</a>
          </li>
          <li class="nav-item">
            <a v-if="this.$route.name ==='AboutUs'" class="nav-link" style="color: #8DD0FF; cursor: pointer"><fa :icon="['fas', 'circle-info'] " /></a>
            <a v-else class="nav-link" style="cursor: pointer"><fa :icon="['fas', 'circle-info'] " /></a>
          </li>
        </ul>
      </div>
      <!-- User dropdown -->
      <ul class="nav navbar-nav navbar-right" v-if="logged===false">
        <div>
          <b-dropdown no-caret id="dropdown-right" border="transparent" right text="Right align" class="lang-dropdown">
            <template #button-content>
              <span class="loginIcon">
              <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
              </svg>
                Account
              </span>
            </template>
            <b-dropdown-item @click="goToLogin"><fa :icon="['fas', 'right-to-bracket']" /> Login</b-dropdown-item>
            <b-dropdown-divider></b-dropdown-divider>
            <b-dropdown-item @click="goToRegister"><fa :icon="['fas', 'user']" /> Create account</b-dropdown-item>
          </b-dropdown>
        </div>
      </ul>
      <ul class="nav navbar-nav navbar-right" v-else>
        <div>
          <b-dropdown no-caret id="dropdown-right" border="transparent" right text="user" class="lang-dropdown">
            <template #button-content>
              <span class="loginIcon">
              <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
              </svg>
                {{username}}
              </span>
            </template>
            <b-dropdown-item @click="goToProfile"><fa :icon="['fas', 'user']" /> Profile</b-dropdown-item>
            <b-dropdown-divider></b-dropdown-divider>
            <b-dropdown-item @click="logOut"><fa :icon="['fas', 'right-from-bracket']" /> Logout</b-dropdown-item>
          </b-dropdown>
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
      username: null,
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
        this.$router.push({ path: '/profile', query: { username: this.username, logged: this.logged, token: this.token } })
      }
    },
    logOut () {
      // eslint-disable-next-line standard/object-curly-even-spacing
      this.$router.push({ path: '/'})
    },
    goToHomepage () {
      // eslint-disable-next-line standard/object-curly-even-spacing
      if (this.logged) {
        this.$router.push({ path: '/', query: { username: this.username, logged: this.logged, token: this.token } })
      } else {
        // eslint-disable-next-line standard/object-curly-even-spacing
        this.$router.push({ path: '/'})
      }
    }
  },
  created () {
    this.logged = this.$route.query.logged === 'true'
    this.username = this.$route.query.username
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
