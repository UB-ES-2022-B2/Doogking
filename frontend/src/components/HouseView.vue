<template>
  <div class="grid">
    <div class="col-12">
      <DataView class="dataView" :value="houses" :layout="layout" :paginator="true" :rows="12" :columns="4">
        <template #header>
          <div class="grid grid-nogutter">
            <div class="col-6 text-left">
              <MultiSelect id="multiSelectCities" v-model="selectedCities" :options="cities" optionLabel="name" placeholder="Select Countries" :filter="true" class="multiselect-custom"
                           style="min-width: 20rem; max-width: 20rem;">
                <template #value="slotProps">
                  <div class="country-item country-item-value" v-for="option of slotProps.value" :key="option.code">
                    <div>{{option.name}}</div>
                  </div>
                  <template v-if="!slotProps.value || slotProps.value.length === 0">
                    Select cities
                  </template>
                </template>
                <template #option="slotProps">
                  <div class="country-item">
                    <div>{{slotProps.option.name}}</div>
                  </div>
                </template>
              </MultiSelect>
              <Button id="searchButton" type="button" @click="getHouses()" icon="pi pi-search" style=""/>
            </div>
            <div class="col-6 text-right">
              <DataViewLayoutOptions v-model="layout" />
            </div>
            <Calendar class="calendarIcon" id="check_in" placeholder="Check-in" v-model="checkInDate" :showIcon="true" style="width: 9.65rem; margin-top: 0.5em; margin-right: 0.5em;"/>
            <Calendar class="calendarIcon" id="check_out" placeholder="Check-out" v-model="checkOutDate" @click="checkOutGreater()" :showIcon="true" style="width: 9.65rem; margin-top: 0.5em; margin-right: 0.5em;"/>
            <ConfirmPopup id="confirmPopup" ></ConfirmPopup>
            <Toast id="error_toast"/>
            <Button id="removeFiltersBtn" @click="confirmRemoveFilters($event)" icon="pi pi-times" style="background-color: indianred; border-color: indianred; color: white; margin-top: 0.5em;"/>
          </div>
          <div class="col-3 text-left">
            <h6 style="margin-top:0.5em; margin-bottom: 1.5em;">Price range per day: {{priceRangeValue}}</h6>
            <Slider id="priceRange" v-model="priceRangeValue" :step="5" :min="0" :max="500" :range="true" style="margin-left: 0.2vw; width: 20vw;"/>
          </div>
          <Divider id="gridDivider" v-if="layout=='grid'"></Divider>
        </template>
        <template #list="slotProps">
          <div class="col-12">
            <div class="flex flex-column md:flex-row align-items-center p-3 w-full">
              <img id="listImage" :src="slotProps.data.image" :alt="slotProps.data.city" class="my-4 md:my-0 w-9 md:w-10rem shadow-2 mr-5" />
              <div class="flex-1 text-center md:text-left">
                <div class="font-bold text-2xl">{{slotProps.data.city}}</div>
                <div class="mb-3">{{slotProps.data.street}},{{slotProps.data.street_number}},{{slotProps.data.floor}},{{slotProps.data.door}},{{slotProps.data.house_dimension}}</div>
                <Rating :value="slotProps.data.rating" :stars="5" :readonly="true" :cancel="false" class="ui-rating" style="padding-bottom: 0.5em"></Rating>
                <div class="flex align-items-center">
                  <Tag :value="slotProps.data.house_owner_name" icon="pi pi-user" style="color: white; background-color: #6c757d"></Tag>
                </div>
              </div>
              <div class="flex flex-row md:flex-column justify-content-between w-full md:w-auto align-items-center md:align-items-end mt-5 md:mt-0">
                  <span v-if="slotProps.data.url === 'favorite'">
                      <Button id="favButtonList" icon="pi pi-heart-fill" @click="removeFavorite(slotProps.data.house_id), slotProps.data.url = 'not favorite'" class="p-button-rounded"/>
                  </span>
                <span v-else>
                      <Button id="favButtonList" icon="pi pi-heart" @click="addHouseToFavorites(slotProps.data.house_id), slotProps.data.url = 'favorite'" class="p-button-rounded"/>
                  </span>
                <span class="text-2xl font-semibold mb-2 align-self-center md:align-self-end">{{slotProps.data.price}}??? day</span>
                <Button id="buttonViewList" label="View house" @click="seeHouseDetails(slotProps.data.house_id)" iconPos="right" class="buttonView"/>
              </div>
            </div>
          </div>
        </template>
        <template #grid="slotProps">
          <div id="gridLayout" style="box-sizing: border-box;">
            <div class="card m-3 card1">
              <div id ="container-image" class="container">
                <div id="container-effect">
                  <img id="card-img" :src="slotProps.data.image" alt="img">
                  <figcaption>
                    <Button id="buttonViewGrid" label="View house" @click="seeHouseDetails(slotProps.data.house_id)" class="buttonView" style="background-color: #1c1b29; color: white; border-radius: 1em; opacity: 0.7;"/>
                  </figcaption>
                </div>
                <span id="favContainer" v-if="slotProps.data.url === 'favorite'">
                  <Button id="favButtonGrid" icon="pi pi-heart-fill" @click="removeFavorite(slotProps.data.house_id), slotProps.data.url = 'not favorite'" class="p-button-rounded"/>
                </span>
                <span id="favContainer" v-else>
                  <Button id="favButtonGrid" icon="pi pi-heart" @click="addHouseToFavorites(slotProps.data.house_id), slotProps.data.url = 'favorite'" class="p-button-rounded"/>
                </span>
                <span id="priceContainer" class="text font-semibold"><a>{{slotProps.data.price}}???</a> day</span>
                <span id="loaderContainer" v-if="loaderActive===true">
                  <LoadingSpinnerGrid :active="true"/>
                </span>
              </div>
              <div id="card-details" class="details">
                <div class="flex align-items-center justify-content-between">
                  <h6>{{slotProps.data.city}}</h6>
                  <div class="flex align-items-center">
                    <Tag id="tagHost" :value="slotProps.data.house_owner_name" icon="pi pi-user" style="color: white; background-color: #2A323D"></Tag>
                    <Rating :value="slotProps.data.rating" :stars="5" :readonly="true" :cancel="false" class="ui-rating" style="padding-bottom: 0.5em"></Rating>
                  </div>
                </div>
                <p style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{{slotProps.data.street}},{{slotProps.data.street_number}},{{slotProps.data.floor}},{{slotProps.data.door}},{{slotProps.data.house_dimension}}</p>
              </div>
            </div>
          </div>
        </template>
      </DataView>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import LoadingSpinnerGrid from './LoadingSpinnerGrid'
export default {
  name: 'App',
  components: {
    LoadingSpinnerGrid
  },
  data () {
    return {
      logged: false,
      username: null,
      email: null,
      userId: null,
      token: null,
      houses: [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}],
      layout: 'grid',
      checkInDate: null,
      checkOutDate: null,
      priceRangeValue: [0, 500],
      minPrice: null,
      maxPrice: null,
      numHouses: null,
      myFavorites: [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}],
      loaderActive: false,
      selectedCities: [],
      cities: [
        {name: 'Barcelona', code: 'BCN'},
        {name: 'Girona', code: 'GI'},
        {name: 'Tarragona', code: 'TR'},
        {name: 'Lleida', code: 'LL'},
        {name: 'Madrid', code: 'MA'},
        {name: 'Valencia', code: 'VA'},
        {name: 'Sevilla', code: 'SV'},
        {name: 'Bilbao', code: 'BB'},
        {name: 'Zaragoza', code: 'ZG'},
        {name: 'M??laga', code: 'ML'},
        {name: 'Palma de Mallorca', code: 'MLL'},
        {name: 'Las Palmas de Gran Canaria', code: 'PGC'},
        {name: 'Hospitalet de Llobregat', code: 'HL'}
      ]
    }
  },
  methods: {
    confirmRemoveFilters (event) {
      this.$confirm.require({
        target: event.currentTarget,
        message: 'Do you want to remove all current filters?',
        icon: 'pi pi-info-circle',
        acceptClass: 'p-button-danger',
        accept: () => {
          this.$toast.add({severity: 'info', summary: 'Confirmed', detail: 'Filters removed', life: 3000})
          this.selectedCities = []
          this.checkInDate = null
          this.checkOutDate = null
          this.getHouses()
        },
        reject: () => {
        }
      })
    },
    onSearch () {
      if (this.checkOutDate !== null && this.checkInDate >= this.checkOutDate) {
        this.checkOutDate = null
        this.$toast.add({severity: 'error', summary: 'Error message', detail: 'Check-out date should be greater than check-in date', life: 2000})
      }
      this.getHouses()
      // this.selectedCities.length = 0
    },
    goToLogin () {
      this.$router.push({path: '/login'})
    },
    // eslint-disable-next-line camelcase
    seeHouseDetails (house_id) {
      this.$router.push({path: '/housedetails', query: {house_id: house_id}})
    },
    getUserFavorites () {
      var config = {
        method: 'get',
        url: 'https://doogking.azurewebsites.net/api/profiles/favourites/' + this.userId + '/',
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Authorization': 'Token ' + this.token
        }
      }
      axios(config)
        .then((response) => {
          this.myFavorites = response.data
          this.getHouses()
        })
        .catch((error) => {
          this.error = error
        })
    },
    // eslint-disable-next-line camelcase
    removeFavorite (house_id) {
      if (this.logged === false) {
        this.$toast.add({severity: 'warn', summary: 'Warn message', detail: 'You need to login to add favorites.', life: 2000})
      } else {
        var data = JSON.stringify({
          // eslint-disable-next-line camelcase
          'housing': house_id,
          'user': this.userId
        })
        var config = {
          method: 'delete',
          url: 'https://doogking.azurewebsites.net/api/favourites/',
          headers: {
            'Access-Control-Allow-Origin': '*',
            'Authorization': 'Token ' + this.token,
            'Content-Type': 'application/json'
          },
          data: data
        }
        axios(config)
          .then((response) => {
            this.$toast.add({severity: 'info', summary: 'Favorite', detail: 'House removed from your list of favorites.', life: 3000})
          })
          .catch((error) => {
            this.error = error
          })
      }
    },
    // eslint-disable-next-line camelcase
    addHouseToFavorites (house_id) {
      if (this.logged === false) {
        this.$toast.add({severity: 'warn', summary: 'Warn message', detail: 'You need to login to add favorites.', life: 2000})
      } else {
        var data = JSON.stringify({
          // eslint-disable-next-line camelcase
          'housing': 'https://doogking.azurewebsites.net/api/housing/' + house_id + '/',
          'user': 'https://doogking.azurewebsites.net/api/profiles/' + this.userId + '/'
        })
        var config = {
          method: 'post',
          url: 'https://doogking.azurewebsites.net/api/favourites/',
          headers: {
            'Access-Control-Allow-Origin': '*',
            'Authorization': 'Token ' + this.token,
            'Content-Type': 'application/json'
          },
          data: data
        }
        axios(config)
          .then((response) => {
            this.$toast.add({severity: 'info', summary: 'Favorite', detail: 'House added to your favorites list. You can see it in you profile.', life: 3000})
          })
          .catch((error) => {
            this.error = error
          })
      }
    },
    getHouses () {
      this.minPrice = this.priceRangeValue[0]
      this.maxPrice = this.priceRangeValue[1]
      // local: 127.0.0.1:8000, cloud: doogking.azurewebsites.net
      const headers = {'Access-Control-Allow-Origin': '*'}
      var pathHouses = 'https://doogking.azurewebsites.net/api/housing/?min_price=' + this.minPrice + '&max_price=' + this.maxPrice
      // Filter Cities
      if (this.selectedCities.length !== 0) {
        for (let i = 0; i < this.selectedCities.length; i++) {
          pathHouses += '&city=' + this.selectedCities[i].name
        }
      }
      if (this.checkOutDate !== null && this.checkInDate !== null) {
        // Check In
        const checkInString = this.checkInDate.toString()
        var checkIn = checkInString.substring(11, 15) + '-'
        var month = checkInString.substring(4, 7)
        var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        checkIn += (months.indexOf(month) + 1).toLocaleString('en-US', {minimumIntegerDigits: 2}) + '-' +
          checkInString.substring(8, 10)
        // Check Out
        const checkOutString = this.checkInDate.toString()
        var checkOut = checkOutString.substring(11, 15) + '-'
        month = checkOutString.substring(4, 7)
        checkOut += (months.indexOf(month) + 1).toLocaleString('en-US', {minimumIntegerDigits: 2}) + '-' +
          checkOutString.substring(8, 10)
        pathHouses += '&check_in=' + checkIn + '&check_out=' + checkOut
      }
      axios.get(pathHouses, headers)
        .then((response) => {
          this.houses = response.data
          for (let i = 0; i < this.houses.length; i++) {
            var found = false
            for (let j = 0; j < this.myFavorites.length && found === false; j++) {
              if (this.houses[i].house_id === this.myFavorites[j].housing.house_id) {
                this.houses[i].url = 'favorite'
                found = true
              }
            }
            console.log(response)
          }
        })
        .catch((error) => {
          this.error = error
        })
    },
    getNumHouses () {
      const headers = {'Access-Control-Allow-Origin': '*'}
      const pathHouses = 'https://doogking.azurewebsites.net/api/housing/'
      const promise = axios.get(pathHouses, headers)
      Promise.resolve(promise).then((value) => (this.numHouses = value.data.length))
    },
    showLoader () {
      this.loaderActive = true
    },
    hideLoader () {
      this.loaderActive = false
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
        this.getUserFavorites()
      }
    }
  },
  created () {
    this.loadLocalStorage()
    this.getHouses()
    this.getNumHouses()
    this.showLoader()
    setTimeout(() => {
      this.hideLoader()
    }, 800)
  }
}
</script>

<style scoped>
.col-12{
  padding-bottom: 0px;
}
#gridLayout{
  align-items: center;
  justify-content: center;
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
#buttonViewList{
  background-color: #6c757d;
  border-color: #6c757d;
  color: white;
}
#buttonViewGrid{
  background-color: #6c757d;
  border-color: #6c757d;
  color: white;
}
#buttonViewList:hover{
  background-color: #8DD0FF;
  border-color: #8DD0FF;
  outline-color: #8DD0FF;
  color: white;
}
#buttonViewGrid:hover{
  background-color: #8DD0FF;
  border-color: #8DD0FF;
  outline-color: #8DD0FF;
  color: white;
}
#buttonViewList:focus {
  box-shadow: 0 0 0 0.1em #8DD0FF;
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
#listImage{
  border-radius: 0.5em;
  border: 3px solid #1c1b29;
}
.p-dropdown {
  width: 14rem;
  font-weight: normal;
}
.product-name {
  font-size: 1.5rem;
  font-weight: 700;
}
.product-description {
  margin: 0 0 1rem 0;
}
.product-category-icon {
  vertical-align: middle;
  margin-right: .5rem;
}
.product-category {
  font-weight: 600;
  vertical-align: middle;
}
.multiselect-custom >>> .country-item-value {
  font-size: 0.8rem;
  padding: 0.1rem;
  border-radius: 3px;
  display: inline-flex;
  margin-right: .5rem;
  background-color: #6c757d;
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
#loaderContainer{
  position:absolute;
  top:40%;
  left:45%;
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
#calendarIcon >>> p-calendar >>> p-calendar-w-btn{
  bacground-color: white;
  color: white;
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
#favButtonList{
  color: indianred;
  background-color: #1c1b29;
  border-color: #1c1b29;
}
#favButtonList:hover{
  color: indianred;
  background-color: #1c1b29;
  border-color: #1c1b29;
}
#favButtonList:focus{
  color: indianred;
  background-color: #1c1b29;
  border-color: #1c1b29;
  outline-color: #1c1b29;
  box-shadow: 0 0 0 0.1em indianred;
}
</style>
