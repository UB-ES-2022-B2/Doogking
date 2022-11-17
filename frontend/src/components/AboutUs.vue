<template>
  <div>
      <div class="flex-wrapper">
        <Header></Header>
        <div id="app">
          <div class="pageFeaturedImage">
            <img  class = featuredImage--desktopOnly wp-post-image src="@/assets/aboutUs.png">
          </div>
          <div class="container">
            <div class="page-header"><h1 class="h2">About Us</h1></div>
            <div class="page__entryContent">
              <p>Doogking was born in 2022 when a group of 6 computer science students where
                creating a web for one of theire assignments, and has since grown to over 1 thousend
                Hosts who have welcomed more than 1 million guest arrivals in almost every Spain city.
                Every day, Hosts offer unique stays and experiences that make it possible for guests to
                connect with communities in a more authentic way.</p>
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

.pageFeaturedImage {
  height: 0;
  padding-bottom: 35%;
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
}

</style>
