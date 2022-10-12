<template>
  <div>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <!-- Icono de NAVBAR -->
      <nav class="navbar navbar-dark">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">
            <img src="@/assets/logoDog.png" alt="" width="30" height="24" class="d-inline-block align-top" style="color: #F06449;">
            DoogKing
          </a>
        </div>
      </nav>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="navbar-collapse collapse w-100 order-1 order-md-0 dual-collapse2" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link to="/" class="nav-link active" aria-current="page" style="color: #F06449;">Inicio</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/login" class="nav-link">Información</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/login" class="nav-link">Soporte</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/login" class="nav-link">Registrar alojamiento</router-link>
          </li>
        </ul>
      </div>
      <div class="vl" style=" border-left: 0.1em solid white; height: 4em;"></div>
      <ul class="nav navbar-nav navbar-right">
        <div v-if="logged" class="container-profile">
          <b-nav-item-dropdown right>
            <template #button-content>
              <em>Usuario</em>
            </template>
            <b-dropdown-item href="#" @click="go_to_login">Perfil</b-dropdown-item>
            <b-dropdown-item href="#" @click="go_to_login">Cerrar sesión</b-dropdown-item>
          </b-nav-item-dropdown>
        </div>
        <div v-else class="container-signin">
          <b-nav-item-dropdown right>
            <template #button-content>
              <div class="loginIcon">
                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                  <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                  <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
                </svg>
              </div>
            </template>
            <b-dropdown-item href="/register">Registro</b-dropdown-item>
            <b-dropdown-item href="/login" @click="goToLogin">Iniciar sesión</b-dropdown-item>
          </b-nav-item-dropdown>
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
      username: null,
      token: null
    }
  },
  methods: {
    goToLogin () {
      // eslint-disable-next-line standard/object-curly-even-spacing
      this.$router.push({ path: '/login'})
    },
    goToRegister () {
      // eslint-disable-next-line standard/object-curly-even-spacing
      this.$router.push({ path: '/register'})
    },
    login () {
      // eslint-disable-next-line standard/object-curly-even-spacing
      this.logged = true
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
}
</script>

<style scoped>
.navbar-brand {
  color: #F06449;
}
.nav-item .nav-link {
  color: white;
}
.nav-item .nav-link:hover {
  color: #F06449;
}

.loginIcon{
  color: white;
}

.loginIcon:hover{
  color: #F06449;
}
</style>
