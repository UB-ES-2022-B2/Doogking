<template>
  <footer class="footer">
    <div class="container">
      <div class="row">
        <div class="footer-col">
          <h4>DoogKing</h4>
          <ul>
            <li><a href="#">Sobre nosotros</a></li>
            <li><a href="#">Servicios</a></li>
            <li><a href="#">Política de privacidad</a></li>
            <li><a href="#">Regístrate</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Soporte</h4>
          <ul>
            <li><a href="#">FAQ</a></li>
            <li><a href="#">Reclamaciones</a></li>
            <li><a href="#">Atención al cliente</a></li>
            <li><a href="#">Opciones de pago</a></li>
            <li><a href="#">Contacto corporativo</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Alojamientos</h4>
          <ul>
            <li><a href="#">Ciudades</a></li>
            <li><a href="#">Regiones</a></li>
            <li><a href="#">Países</a></li>
            <li><a href="#">Casas</a></li>
            <li><a href="#">Pisos</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Síguenos</h4>
          <div class="social-links">
            <a href="#"><i class="fab fa-facebook-f"></i></a>
            <a href="#"><i class="fab fa-twitter"></i></a>
            <a href="#"><i class="fab fa-instagram"></i></a>
            <a href="#"><i class="fab fa-linkedin-in"></i></a>
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
  padding: 70px 0;
  position: relative;
  margin-top: 200px;
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
  background-color: #F06449;
  height: 2px;
  box-sizing: border-box;
  width: 50px;
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
