<template>
  <footer class="footer">
    <div class="container">
      <div class="row">
        <div class="footer-col">
          <h4>DoogKing</h4>
          <ul>
            <li><a href="#" @click="goToAboutUs" id="aboutUs">About Us</a></li>
            <li><a href="#">Services</a></li>
            <li><a href="#" @click="goToPrivacyPolicy" id="privacyPolicy">Privacy policy</a></li>
            <li><a href="#">Register</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Support</h4>
          <ul>
            <li><a href="#">FAQ</a></li>
            <li><a href="#">Complaints</a></li>
            <li><a href="#">Customer support</a></li>
            <li><a href="#">Payment options</a></li>
            <li><a href="#">Business contact</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Housing</h4>
          <ul>
            <li><a href="#">Cities</a></li>
            <li><a href="#">Regions</a></li>
            <li><a href="#">Countries</a></li>
            <li><a href="#">Houses</a></li>
            <li><a href="#">Flats</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Follow us</h4>
          <div class="social-links">
            <a href="#"><fa :icon="['fab', 'facebook']" /></a>
            <a href="#"><fa :icon="['fab', 'twitter']" /></a>
            <a href="#"><fa :icon="['fab', 'instagram']" /></a>
            <a href="#"><fa :icon="['fab', 'linkedin']" /></a>
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
      logged: false
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
    },
    goToPrivacyPolicy () {
      // eslint-disable-next-line standard/object-curly-even-spacing
      this.$router.push({path: '/privacyPolicy'})
    },
    goToAboutUs () {
      // eslint-disable-next-line standard/object-curly-even-spacing
      this.$router.push({ path: '/aboutUs'})
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
