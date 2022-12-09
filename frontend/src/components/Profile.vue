<template>
  <form>
    <div class="flex-wrapper">
      <Header></Header>
      <Dialog :visible="showLoginMessage" :breakpoints="{ '960px': '80vw' }" :style="{ width: '30vw' }" position="top">
        <div class="flex align-items-center flex-column pt-6 px-3">
          <i class="pi pi-info-circle" :style="{fontSize: '5rem', color: 'var(--red-500)' }"></i>
          <h5 style="margin-top: 1em">Login Error!</h5>
          <p style="text-align: center">
            You need to be logged in to access your profile
          </p>
        </div>
        <template #footer>
          <div class="flex justify-content-center">
            <Button label="OK" @click="toggleDialogLogin" class="p-button-text" />
          </div>
        </template>
      </Dialog>
      <div id="app">
        <div class="body">
          <div class="d-flex flex-row">
            <div class="p-2" style="margin-left:50px">
              <img class="mx-auto rounded-circle" src="@/assets/avatar.png" style="width:200px">
            </div>
            <div class="p-2" style="margin-right:200px">
              <div class="info-containter" ><h2>{{username}}</h2>
                <div class="reviewButton">
                  <fa :icon="['fas', 'star']"/>
                  <fa :icon="['fas', 'star']"/>
                  <fa :icon="['fas', 'star']"/>
                  <fa :icon="['fas', 'star']"/>
                  <fa :icon="['fas', 'star-half']"/>
                </div>
                <div class="about-me"><h7>About me:</h7></div>
                <div class="row">
                  <div class="col"><fa :icon="['fas', 'star']"/>      34 reviews</div>
                  <div class="w-100"></div>
                  <div class="col"><fa :icon="['fas', 'envelope']"/>          {{email}}</div>
                  <div class="w-100"></div>
                  <div class="col"><fa :icon="['fas', 'house']"/>       {{numHouses}}</div>
                </div>
              </div>
            </div>
            <div class="profile2Button-button" align-content="left">
              <button class="btn btn-lg btn-block" type="submit" @click="goToEditProfile" name="editProfile" aria-label="Left Align"><fa :icon="['fas', 'pen-to-square']"/><h6>Edit Profile</h6></button>
              <button class="btn btn-lg btn-block" type="submit" style="color:#8dd0ff" @click="logOut" name="editProfile" aria-label="Left Align"><fa :icon="['fas', 'right-from-bracket']"/><h6>Log out</h6></button>
            </div>
            <br>
          </div>
          <hr>
        </div>
      </div>
      <Carousel :value="myHouses" :page="0" :numVisible="3" :numScroll="1" class="custom-carousel" :circular="true" :autoplayInterval="3000">
        <template #header>
          <h5 style="text-align: left; margin-left: 6vw; color: white;">My houses</h5>
          <hr style="width:90vw; color: white; margin-left: auto; margin-right: auto; margin-bottom:1vw" class="solid"/>
        </template>
        <template #item="slotProps">
          <div class="product-item">
            <div class="product-item-content">
              <div class="card" style="margin:auto;">
                <div id ="container-image" class="container">
                  <div id="container-effect">
                    <img id="card-img" :src="slotProps.data.image" alt="img">
                    <figcaption>
                      <Button id="buttonViewGrid" label="View house" @click="seeMyHouseDetails(slotProps.data.house_id)" class="buttonView" style="background-color: #1c1b29; color: white; border-radius: 1em; opacity: 0.7;"/>
                    </figcaption>
                  </div>
                  <Toast/>
                  <span id="favContainer" v-if="slotProps.data.favorite==true">
                      <Button id="favButtonGrid" icon="pi pi-heart-fill" @click="changeFavorite()" class="p-button-rounded"/>
                  </span>
                  <span id="favContainer" v-else>
                        <Button id="favButtonGrid" icon="pi pi-heart" @click="changeFavorite()" class="p-button-rounded"/>
                  </span>
                  <span id="priceContainer" class="text font-semibold" style="color:white"><a>{{slotProps.data.price}}€</a> day</span>
                  <span id="loaderContainer" v-if="loaderActive===true">
                  <LoadingSpinnerGrid :active="true"/>
                </span>
                </div>
                <div id="card-details" class="details">
                  <div class="flex align-items-center justify-content-between">
                    <h6 style="color:white">{{slotProps.data.city}}</h6>
                    <div class="flex align-items-center">
                      <Tag id="tagHost" :value="slotProps.data.house_owner_name" icon="pi pi-user" style="color: white; background-color: #2A323D"></Tag>
                      <Rating :value="slotProps.data.rating" :stars="5" :readonly="true" :cancel="false" class="ui-rating" style="padding-bottom: 0.5em"></Rating>
                    </div>
                  </div>
                  <p style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{{slotProps.data.street}}, {{slotProps.data.street_number}}, {{slotProps.data.floor}}, {{slotProps.data.door}}, {{slotProps.data.house_dimension}}</p>
                </div>
              </div>
            </div>
          </div>
        </template>
      </Carousel>
    <Carousel :value="myReservations" :page="0" :numVisible="3" :numScroll="1" class="custom-carousel" :circular="true" :autoplayInterval="3000">
      <template #header>
        <h5 style="text-align: left; margin-left: 6vw; color: white;">My reservations</h5>
        <hr style="width:90vw; color: white; margin-left: auto; margin-right: auto; margin-bottom:1vw" class="solid"/>
      </template>
      <template #item="slotProps">
        <div class="product-item">
          <div class="product-item-content">
            <div class="card" id="cardReservation" style="margin:auto;">
              <div id ="container-image" class="container">
                <div id="container-effect">
                  <img id="card-img" :src="slotProps.data.housing.image" alt="img">
                  <figcaption>
                    <Button id="buttonViewGrid" label="View house" @click="seeMyReservationDetails(slotProps.data.housing.house_id, slotProps.data.start_date, slotProps.data.end_date)" class="buttonView" style="background-color: #1c1b29; color: white; border-radius: 1em; opacity: 0.7;"/>
                  </figcaption>
                </div>
                <Toast/>
                <span id="favContainer" v-if="slotProps.data.favorite==true">
                      <Button id="favButtonGrid" icon="pi pi-heart-fill" @click="changeFavorite()" class="p-button-rounded"/>
                  </span>
                <span id="favContainer" v-else>
                        <Button id="favButtonGrid" icon="pi pi-heart" @click="changeFavorite()" class="p-button-rounded"/>
                  </span>
                <span id="priceContainer" class="text font-semibold" style="color:white"><a>{{slotProps.data.price}}€</a> day</span>
                <span id="loaderContainer" v-if="loaderActive===true">
                  <LoadingSpinnerGrid :active="true"/>
                </span>
              </div>
              <div id="card-details" class="details">
                <div class="flex align-items-center justify-content-between">
                  <h6 style="color:white">{{slotProps.data.housing.city}}</h6>
                  <div class="flex align-items-center">
                    <Tag id="tagHost" :value="slotProps.data.housing.house_owner_name" icon="pi pi-user" style="color: white; background-color: #2A323D"></Tag>
                    <Rating :value="slotProps.data.housing.rating" :stars="5" :readonly="true" :cancel="false" class="ui-rating" style="padding-bottom: 0.5em"></Rating>
                  </div>
                </div>
                <p style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Start date: {{slotProps.data.start_date}}, End date: {{slotProps.data.end_date}}</p>
                <p style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis; margin-top: -1.1em;">{{slotProps.data.housing.street}}, {{slotProps.data.housing.street_number}}, {{slotProps.data.housing.floor}}, {{slotProps.data.housing.door}}, {{slotProps.data.housing.house_dimension}}</p>
              </div>
            </div>
          </div>
        </div>
      </template>
    </Carousel>
      <Carousel :value="myReservedHouses" :page="0" :numVisible="3" :numScroll="1" class="custom-carousel" :circular="true" :autoplayInterval="3000">
        <template #header>
          <h5 style="text-align: left; margin-left: 6vw; color: white;">My houses reserved by other users</h5>
          <hr style="width:90vw; color: white; margin-left: auto; margin-right: auto; margin-bottom:1vw" class="solid"/>
        </template>
        <template #item="slotProps">
          <div class="product-item">
            <div class="product-item-content">
              <div class="card" id="cardReservation" style="margin:auto;">
                <div id ="container-image" class="container">
                  <div id="container-effect">
                    <img id="card-img" :src="slotProps.data.housing.image" alt="img">
                    <figcaption>
                      <Button id="buttonViewGrid" label="View house" @click="seeMyReservedDetails(slotProps.data.housing.house_id, slotProps.data.start_date, slotProps.data.end_date)" class="buttonView" style="background-color: #1c1b29; color: white; border-radius: 1em; opacity: 0.7;"/>
                    </figcaption>
                  </div>
                  <Toast/>
                  <span id="favContainer" v-if="slotProps.data.favorite==true">
                      <Button id="favButtonGrid" icon="pi pi-heart-fill" @click="changeFavorite()" class="p-button-rounded"/>
                  </span>
                  <span id="favContainer" v-else>
                        <Button id="favButtonGrid" icon="pi pi-heart" @click="changeFavorite()" class="p-button-rounded"/>
                  </span>
                  <span id="priceContainer" class="text font-semibold" style="color:white"><a>{{slotProps.data.price}}€</a> day</span>
                  <span id="loaderContainer" v-if="loaderActive===true">
                  <LoadingSpinnerGrid :active="true"/>
                </span>
                </div>
                <div id="card-details" class="details">
                  <div class="flex align-items-center justify-content-between">
                    <h6 style="color:white">{{slotProps.data.housing.city}}</h6>
                    <div class="flex align-items-center">
                      <Tag id="tagHost" :value="slotProps.data.housing.house_owner_name" icon="pi pi-user" style="color: white; background-color: #2A323D"></Tag>
                      <Rating :value="slotProps.data.housing.rating" :stars="5" :readonly="true" :cancel="false" class="ui-rating" style="padding-bottom: 0.5em"></Rating>
                    </div>
                  </div>
                  <p style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Start date: {{slotProps.data.start_date}}, End date: {{slotProps.data.end_date}}</p>
                  <p style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis; margin-top: -1.1em;">{{slotProps.data.housing.street}}, {{slotProps.data.housing.street_number}}, {{slotProps.data.housing.floor}}, {{slotProps.data.housing.door}}, {{slotProps.data.housing.house_dimension}}</p>
                </div>
              </div>
            </div>
          </div>
        </template>
      </Carousel>
      <Footer></Footer>
    </div>
  </form>
</template>

<script>
import Header from './Header'
import Footer from './Footer'
import axios from 'axios'
import LoadingSpinnerGrid from './LoadingSpinnerGrid'

export default {
  components: {
    Header,
    Footer,
    LoadingSpinnerGrid
  },
  data () {
    return {
      logged: false,
      username: null,
      email: null,
      myHouses: [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}],
      numReservations: 0,
      myReservations: [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}],
      numReserved: 0,
      myReservedHouses: [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}],
      loaderActive: false,
      userId: null,
      token: null,
      showLoginMessage: false,
      numHouses: null
    }
  },
  methods: {
    logOut () {
      this.logged = false
      localStorage.removeItem('username')
      localStorage.removeItem('userId')
      localStorage.removeItem('token')
      localStorage.removeItem('email')
      this.$router.push({path: '/'})
    },
    goToEditProfile () {
      this.$router.push({path: '/editProfile'})
    },
    getUserHouses () {
      const headers = {'Access-Control-Allow-Origin': '*'}
      const pathHouses = 'https://doogking.azurewebsites.net/api/housing/?owner=' + this.userId
      axios.get(pathHouses, headers)
        .then(response => (this.myHouses = response.data))
        .catch((error) => {
          this.error = error
        })
    },
    getUserReservations () {
      var config = {
        method: 'get',
        url: 'https://doogking.azurewebsites.net/api/reservations/?customer=' + this.userId,
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Authorization': 'Token ' + this.token
        }
      }
      axios(config)
        .then((response) => {
          this.myReservations = response.data
          if (response.data.length === 0) {
            this.myReservations = null
          }
        })
        .catch((error) => {
          this.myReservations = null
          this.error = error
        })
    },
    getUserReservedHouses () {
      const headers = {'Access-Control-Allow-Origin': '*'}
      const pathReservations = 'https://doogking.azurewebsites.net/api/reservations/?owner=' + this.userId
      axios.get(pathReservations, headers)
        .then((response) => {
          this.myReservedHouses = response.data
          if (response.data.length === 0) {
            this.myReservedHouses = null
          }
        })
        .catch((error) => {
          this.myReservedHouses = null
          this.error = error
        })
    },
    getNumHouses () {
      const headers = {'Access-Control-Allow-Origin': '*'}
      const pathHouses = 'https://doogking.azurewebsites.net/api/housing/?owner=' + this.userId
      const promise = axios.get(pathHouses, headers)
      Promise.resolve(promise).then((value) => (this.numHouses = value.data.length))
    },
    // eslint-disable-next-line camelcase
    seeMyHouseDetails (house_id) {
      this.$router.push({path: '/myHouseDetails', query: {house_id: house_id}})
    },
    // eslint-disable-next-line camelcase
    seeMyReservationDetails (house_id, start_date, end_date) {
      // eslint-disable-next-line camelcase
      localStorage.start_date = start_date
      // eslint-disable-next-line camelcase
      localStorage.end_date = end_date
      this.$router.push({path: '/myReservationDetails', query: {house_id: house_id}})
    },
    // eslint-disable-next-line camelcase
    seeMyReservedDetails (house_id, start_date, end_date) {
      // eslint-disable-next-line camelcase
      localStorage.start_date = start_date
      // eslint-disable-next-line camelcase
      localStorage.end_date = end_date
      this.$router.push({path: '/myReservationDetails', query: {house_id: house_id}})
    },
    showLoader () {
      this.loaderActive = true
    },
    hideLoader () {
      this.loaderActive = false
    },
    changeFavorite () {
      if (this.logged === false) {
        this.$toast.add({severity: 'warn', summary: 'Warn message', detail: 'You need to login to add favorites', life: 2000})
      }
    },
    toggleDialogLogin () {
      this.showLoginMessage = !this.showLoginMessage
      if (!this.showLoginMessage) {
        this.$router.push({path: '/'})
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
      if (this.logged === false) {
        this.showLoginMessage = true
      }
    }
  },
  created () {
    this.loadLocalStorage()
    this.getUserHouses()
    this.getUserReservations()
    this.getUserReservedHouses()
    this.showLoader()
    setTimeout(() => {
      this.hideLoader()
    }, 500)
  }
}
</script>

<style scoped>
.flex-wrapper {
  background-color: #2A323D;
  display: flex;
  min-height: 100vh;
  flex-direction: column;
  justify-content: flex-start;
  overflow-x: hidden;
  align-content: center;
}
.profileButton-button > :first-child {
  margin-top: 0.5em;
  align-content: center;
  background-color: white;
  border-color: white;
  outline-style: none;
  border: none;
  color: black;
}

.profile2Button-button > :first-child {
  margin-top: 0;
  align-content: center;
  background-color: #8dd0ff;
  border-color: #2a323d;
  outline-style: none;
  border: none;
  color: #2a323d;
}

.info-containter{
  text-align: left;
  padding-left: 40px;
  font-size: 16px;
  color: white;
}

.about-me{
  margin-top: 15px;
  color: white;
}

.row{
  padding-left: 50px;
  color: white;
}

.card{
  background-color: #1c1b29;
  border-radius: 20px;
  box-shadow: 0 0 30px rgba(0,0,0,0.18);
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  overflow: hidden;
  text-overflow: ellipsis;
  width: 22.3vw;
  height: 22vw;
}

#cardReservation{
  background-color: #1c1b29;
  border-radius: 20px;
  box-shadow: 0 0 30px rgba(0,0,0,0.18);
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  overflow: hidden;
  text-overflow: ellipsis;
  width: 22.3vw;
  height: 23vw;
}

#container-image{
  position: relative;
  box-sizing: border-box;
  padding: 0;
  margin: 0;
}
#card-img{
  clip-path: polygon(0 0,100% 0, 100% 85%, 0 100%);
  display: block;
  border-radius: 20px 20px 0 0;
  overflow: hidden;
  width: 22.3vw;
  height: 14vw;
}
#container-effect {
  background-color: #000;
  display: inline-block;
  overflow: hidden;
  border-radius: 20px 20px 0 0;
  clip-path: polygon(0 0,100% 0, 100% 85%, 0 100%);
}
#container-effect * {
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  -webkit-transition: all 0.35s ease;
  transition: all 0.35s ease;
}
#container-effect:before,
#container-effect:after {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  -webkit-transition: all 0.35s ease;
  transition: all 0.35s ease;
  background-color: #8DD0FF;
  border-left: 3px solid #fff;
  border-right: 3px solid #fff;
  content: '';
  opacity: 0.6;
  z-index: 1;
}
#container-effect:before {
  -webkit-transform: skew(45deg) translateX(-155%);
  transform: skew(45deg) translateX(-155%);
}
#container-effect:after {
  -webkit-transform: skew(45deg) translateX(155%);
  transform: skew(45deg) translateX(155%);
}
#container-effect figcaption {
  top: 50%;
  left: 50%;
  position: absolute;
  z-index: 2;
  -webkit-transform: translate(-50%, -50%) scale(0.5);
  transform: translate(-50%, -50%) scale(0.5);
  opacity: 0;
}
#container-effect:hover > #card-img,
#container-effect.hover > #card-img {
  opacity: 0.5;
}
#container-effect:hover:before{
  -webkit-transform: skew(45deg) translateX(-55%);
  transform: skew(45deg) translateX(-55%);
}
#container-effect:hover:after,
#container-effect.hover:after {
  -webkit-transform: skew(45deg) translateX(55%);
  transform: skew(45deg) translateX(55%);
}
#container-effect:hover figcaption,
#container-effect.hover figcaption {
  -webkit-transform: translate(-50%, -50%) scale(1);
  transform: translate(-50%, -50%) scale(1);
  opacity: 1;
}
#card-details{
  padding: 20px 10px;
}
#card-details>h6{
  color: #ffffff;
  font-weight: 600;
  margin: 10px 0 15px 0;
}
#card-details>p{
  color: #a0a0a0;
  font-size: 15px;
  line-height: 30px;
  font-weight: 400;
}

#buttonViewGrid{
  background-color: #6c757d;
  border-color: #6c757d;
  color: white;
}

#buttonViewGrid:hover{
  background-color: #8DD0FF;
  border-color: #8DD0FF;
  outline-color: #8DD0FF;
  color: white;
}

#buttonViewGrid:focus {
  box-shadow: 0 0 0 0.1em #8DD0FF;
  background-color: #8DD0FF;
  border-color: #8DD0FF;
  outline-color: #8DD0FF;
  color: white;
}

#tagHost{
  position:absolute;
  top:1em;
  left:1em;
}
#favContainer{
  position:absolute;
  top:0.5em;
  right:0.5em;
}

#priceContainer{
  position:absolute;
  top:90%;
  right:0.5em;
  font-size: 1em;
}
#priceContainer a{
  font-size: 1.5em;
}

#favButtonGrid{
  color: indianred;
  background-color: #2A323D;
  border-color: #2A323D;
}
#favButtonGrid:hover{
  color: indianred;
  background-color: #2A323D;
  border-color: #2A323D;
}
#favButtonGrid:focus{
  color: indianred;
  background-color: #2A323D;
  border-color: #2A323D;
  box-shadow: 0 0 0 0.1em indianred;
}

.product-item .product-item-content {
  border: 1px solid var(--surface-border);
  border-radius: 3px;
  margin: .3rem;
  padding: 2rem 0;
}

#loaderContainer{
  position:absolute;
  top:40%;
  left:45%;
}
</style>
