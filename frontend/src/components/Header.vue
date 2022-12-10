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
        <Button id="post" type="submit"  style="margin-right: 10px; border-radius: 12px" @click="addHouse" v-if="logged===true"><fa  style="margin-right:10px" :icon="['fas', 'plus']"/>Post House</Button>
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
      logged: false,
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
      userId: null,
      token: null
    }
  },
  methods: {
    goToRegister () {
      this.$router.push({path: '/register'})
    },
    goToLogin () {
      this.$router.push({path: '/login'})
    },
    goToProfile () {
      if (this.logged) {
        this.$router.push({path: '/profile'})
      }
    },
    goToAboutUs () {
      this.$router.push({path: '/aboutUs'})
    },
    addHouse () {
      this.$router.push({path: '/houseRegistry'})
    },
    logOut () {
      this.logged = false
      localStorage.removeItem('username')
      localStorage.removeItem('userId')
      localStorage.removeItem('token')
      localStorage.removeItem('email')
      this.$router.push({path: '/'})
    },
    goToBusinessContact () {
      this.$router.push({path: '/businessContact'})
    },
    goToHomepage () {
      this.$router.push({path: '/'})
    }
  },
  mounted () {
    if (localStorage.username) {
      this.logged = true
      this.username = localStorage.username
    }
    if (localStorage.userId) {
      this.userId = localStorage.userId
    }
    if (localStorage.token) {
      this.token = localStorage.token
    }
    if (localStorage.email) {
      this.email = localStorage.email
    }
  },
  created () {
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
