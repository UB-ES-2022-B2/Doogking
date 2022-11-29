<template>
  <div>
      <div class="flex-wrapper">
        <Header></Header>
        <div id="app">
          <div class="container">
            <div class="page-header"><h1 class="h1">Business Contact</h1></div>
            <p></p>
            <p></p>
            <p></p>
            <p></p>
            <div class="page__entryContent">
              <p class="info-businessContact">
                Dear Customer,
              <p></p>
              <p class="info-businessContact">
                Thank you for wanting to contact our customer service. All your opinions, doubts and comments are of
                interest to us and help us to improve.
              <p></p>
              <p class="info-businessContact">
                Here are the different methods:
              <p class="info-businessContact">
              <p></p>
              <p class="info-businessContact">
              <pre style='display:inline'>&#09;</pre>email: doogking2022@gmail.com
              <p></p>
              <p class="info-businessContact">
              <pre style='display:inline'>&#09;</pre>instagram: goodking2022
              <p></p>
              <p class="info-businessContact">
              <pre style='display:inline'>&#09;</pre>phone: 938 462 301
              <p></p>
            </div>
          </div>
        </div>
        <Footer></Footer>
      </div>
  </div>
</template>

<script>
import Header from './Header'
import Footer from './Footer'
export default {
  components: {
    Header,
    Footer
  }

}
</script>

<style>

.flex-wrapper {
  background-color: #2A323D;
  display: flex;
  min-height: 100vh;
  flex-direction: column;
  justify-content: flex-start;
  overflow-x: hidden;
  align-content: center;
}

.pageFeaturedImage img {
  position: absolute;
  top: 72px;
  left: 0;
  width: 100%;
  height: 75%;
  -o-object-fit: cover;
  object-fit: cover;
}
iframe, img {
  max-width: 100%;
}
img {
  border-style: none;
}
.container {
  max-width: 750px;
  width: 100%;
  margin-right: auto;
  margin-left: auto;
  margin-bottom: 100px;
  padding-right: 80px;
  padding-left: 80px;
  text-rendering: optimizeLegibility;
  text-align: left;
  text-color:#bbbbbb;
}

.page-header{
  color:#bbbbbb;
}

.info-businessContact{
  color:#bbbbbb;
}

</style>
