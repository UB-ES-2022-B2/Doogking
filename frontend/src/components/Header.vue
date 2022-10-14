<template>
  <div>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <!-- Icono de NAVBAR -->
      <nav class="navbar navbar-dark">
        <div class="container-fluid">
          <a class="navbar-brand" href="/">
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
            <router-link to="/" class="nav-link">Soporte</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/" class="nav-link">Registrar alojamiento</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/" class="nav-link"><fa :icon="['fas', 'circle-info']" /></router-link>
          </li>
        </ul>
      </div>
      <!-- USER DROPDOWN -->
      <ul class="nav navbar-nav navbar-right" v-if="logged==false">
        <div>
          <b-dropdown no-caret id="dropdown-right" border="transparent" right text="Right align" class="lang-dropdown">
            <template #button-content>
              <span class="loginIcon">
                Usuario
              <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
              </svg>
              </span>
            </template>
            <b-dropdown-item href="/login">Iniciar sesión   <fa :icon="['fas', 'right-to-bracket']" /></b-dropdown-item>
            <b-dropdown-divider></b-dropdown-divider>
            <b-dropdown-item href="/register">Crear cuenta   <fa :icon="['fas', 'user']" /></b-dropdown-item>
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
              </span>
            </template>
            <b-dropdown-item href="/">Perfil   <fa :icon="['fas', 'user']" /></b-dropdown-item>
            <b-dropdown-divider></b-dropdown-divider>
            <b-dropdown-item href="/">Cerrar sesión   <fa :icon="['fas', 'right-from-bracket']" /></b-dropdown-item>
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
    go_to_login () {
      // eslint-disable-next-line standard/object-curly-even-spacing
      this.$router.push({ path: '/login'})
    },
    login () {
      // eslint-disable-next-line standard/object-curly-even-spacing
      this.logged = true
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
  color: #F06449;
}
.nav-item .nav-link {
  color: white;
}
.nav-item .nav-link:hover {
  color: #F06449;
}

.loginIcon:hover{
  color: #F06449;
}
</style>
