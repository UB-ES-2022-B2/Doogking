<template>
  <div>
      <div class="flex-wrapper">
        <Header></Header>
        <div id="app">
          <div class="pageFeaturedImage">
            <img  class = featuredImage--desktopOnly wp-post-image src="@/assets/aboutUs.png">
          </div>
          <div class="container">
            <div class="page-header"><h1 class="h1">About Us</h1></div>
            <p></p>
            <div class="page-header" style="margin-top:50px"><h4 class="h4"> Our Story <hr></h4></div>
            <p></p>
            <div class="page__entryContent">
              <p class="info-aboutUs" id="info_about_us">
                We’re Doogking, a national, pet-loving community on a mission to create a
                world where pets enjoy their owners’ vacations just as much as they do!

                Founded in 2022 when a group of 6 computer science students where
                creating a web for one of their assignments, and has since grown to over 1 thousand
                Hosts who have welcomed more than half million pets arrivals in almost every Spain city.
                We've connected thousands of pet owners and pet sitters worldwide
                through their mutual trust and love of animals. Which means when it comes to pet
                sitting, we’ve got it covered.
              </p>
            </div>
            <p></p>
            <div class="page-header" style="margin-top:50px"><h4 class="h4"> Brought together by a love of pets <hr></h4></div>
            <p>

            </p>
            <div class="page__entryContent">
              <p class="info-aboutUs">
                Our community of pet lovers help each other by offering unlimited pet and
                home care in exchange for a free place to stay. Pet owners can travel with
                confidence knowing they’ve secured the very best care for their best friend.
                While sitters get to stay in unique homes around the world and enjoy the company
                of pets. It’s a win-win for everyone… especially for the pets!
              </p>
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
  text-color:#bbbbbb;
}

.page-header{
  color:#bbbbbb;
}

.info-aboutUs{
  color:#bbbbbb;
}

</style>
