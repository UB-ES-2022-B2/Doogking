<template>
  <footer class="footer">
    <div class="container">
      <div class="row">
        <div class="footer-col">
          <h4>DoogKing</h4>
          <ul>
            <li><a href="#" @click="goToAboutUs" id="aboutUs">About Us</a></li>
            <li><a href="#" @click="goToPrivacyPolicy" id="privacyPolicy">Privacy policy</a></li>
            <li><a href="#" @click="goToProfile" id="goToProfile" v-if="logged" >Profile</a></li>
            <li><a href="#" @click="goToRegister" id="goRegister">Register</a></li>
            <li><a href="#" @click="goToLogin" id="goRegister">Login</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Support</h4>
          <ul>
            <li><a href="#" @click="goToBusinessContact">Business contact</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Housing</h4>
          <ul>
            <li><a href="#" @click="addHouse" id="goToAddHouse">House Registry</a></li>
            <li><a href="#" @click="goToProfile" id="goToHouses" v-if="logged" >Your houses</a></li>
            <li><a href="#" @click="goToProfile" id="goToFavorites" v-if="logged" >Favorites</a></li>
            <li><a href="#" @click="goToProfile" id="goToReservations" v-if="logged" >Your reservations</a></li>
            <li><a href="#" @click="goToProfile" id="goToReserved" v-if="logged" >Your reserved houses</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Follow us</h4>
          <div class="social-links">
            <a href="https://www.facebook.com/profile.php?id=100087988193167" target="_blank"><fa :icon="['fab', 'facebook']" /></a>
            <a href="https://twitter.com/doogkingUB2022" target="_blank"><fa :icon="['fab', 'twitter']" /></a>
            <a href="https://www.instagram.com/doogking_ub_2022/" target="_blank"><fa :icon="['fab', 'instagram']" /></a>
            <a href="https://www.linkedin.com/in/doogking-ub-855804256/" target="_blank"><fa :icon="['fab', 'linkedin']" /></a>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  data () {
    return {
      logged: false,
      username: null,
      userId: null,
      token: null,
      email: null
    }
  },
  methods: {
    goToLogin () {
      this.$router.push({path: '/login'})
    },
    goToPrivacyPolicy () {
      this.$router.push({path: '/privacyPolicy'})
    },
    goToAboutUs () {
      this.$router.push({path: '/aboutUs'})
    },
    goToRegister () {
      this.$router.push({path: '/register'})
    },
    goToBusinessContact () {
      this.$router.push({path: '/businessContact'})
    },
    addHouse () {
      this.$router.push({path: '/houseRegistry'})
    },
    goToProfile () {
      if (this.logged) {
        this.$router.push({path: '/profile'})
      }
    },
    loadLocalStorage () {
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
    }
  },
  created () {
    this.loadLocalStorage()
  }
}
</script>

<style scoped>

body{
  line-height: 1.5;
  font-family: 'Poppins', sans-serif;
}
*{
  margin:0;
  padding:0;
  box-sizing: border-box;
}
.container{
  max-width: 1170px;
  margin:auto;
}
.row{
  display: flex;
  flex-wrap: wrap;
}

ul{
  list-style: none;
}

.footer{
  background-color: #24262b;
  padding: 5em 0;
  max-height: min-content;
  position: relative;
  margin-top: auto;
}

.footer-col{
  width: 25%;
  padding: 0 15px;
}
.footer-col h4{
  font-size: 18px;
  color: #ffffff;
  text-transform: capitalize;
  margin-bottom: 35px;
  font-weight: 500;
  position: relative;
}
.footer-col h4::before{
  content: '';
  position: absolute;
  left:0;
  bottom: -10px;
  background-color: #8DD0FF;
  height: 2px;
  box-sizing: border-box;
  width: 50px;
}

.footer-col :hover{
  color: #8DD0FF;
}

.footer-col ul li:not(:last-child){
  margin-bottom: 10px;
}
.footer-col ul li a{
  font-size: 16px;
  text-transform: capitalize;
  color: #ffffff;
  text-decoration: none;
  font-weight: 300;
  color: #bbbbbb;
  display: block;
  transition: all 0.3s ease;
}
.footer-col ul li a:hover{
  color: #ffffff;
  padding-left: 8px;
}
.footer-col .social-links a{
  display: inline-block;
  height: 40px;
  width: 40px;
  background-color: rgba(255,255,255,0.2);
  margin:0 10px 10px 0;
  text-align: center;
  line-height: 40px;
  border-radius: 50%;
  color: #ffffff;
  transition: all 0.5s ease;
}
.footer-col .social-links a:hover{
  color: #24262b;
  background-color: #ffffff;
}

/*responsive*/
@media(max-width: 767px){
  .footer-col{
    width: 50%;
    margin-bottom: 30px;
  }
}
@media(max-width: 574px){
  .footer-col{
    width: 100%;
  }
}
</style>
