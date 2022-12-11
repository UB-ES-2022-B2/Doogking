<template>
  <div class="flex-wrapper">
    <Header></Header>
    <div v-if="loaderActive===true" style="position: absolute; top: 24%; left: 49%">
      <LoadingSpinner :active="true"/></div>
    <div id="houseContainer" v-else>
      <div id="galleriaContainer" class="houseDetails">
        <Galleria id="galleriaHouse" :value="houseImages" :responsiveOptions="responsiveOptions" :numVisible="3"
                  :showItemNavigators="true" :showItemNavigatorsOnHover="true"
                  :circular="true" :autoPlay="true" :transitionInterval="3000"
                  style="width: 46vw; margin:1em;">
          <template #item="{item}">
            <img id="imageHouse" :src="item.image" :alt="item.alt" style="width: 100%; display: block;" />
          </template>
          <template #thumbnail="{item}">
            <div class="grid grid-nogutter justify-content-center">
              <img id="thumbnailImage" :src="item.image" :alt="item.alt" style="display: block;" />
            </div>
          </template>
          <template #caption="{item}">
            <h4 style="margin-bottom: .5rem;">{{house.city}}</h4>
            <p>{{house.street}}, {{house.street_number}}, {{house.floor}}, {{house.door}}, {{house.house_dimension}}</p>
          </template>
        </Galleria>
      </div>
      <div id="detailsContainer" class="houseDetails">
        <div class="form-demo">
          <Dialog :visible="showErrorMessage" :breakpoints="{ '960px': '80vw' }" :style="{ width: '30vw' }" position="top">
            <div class="flex align-items-center flex-column pt-6 px-3">
              <i class="pi pi-info-circle" :style="{fontSize: '5rem', color: 'var(--red-500)' }"></i>
              <h5 style="margin-top: 1em">Reservation Error!</h5>
              <p style="text-align: center">
                There's a conflicting reservation with this date. Please enter a valid Check-in and Check-out date.
              </p>
            </div>
            <template #footer>
              <div class="flex justify-content-center">
                <Button label="OK" @click="toggleDialogError" class="p-button-text" />
              </div>
            </template>
          </Dialog>

          <Dialog :visible="showLoginMessage" :breakpoints="{ '960px': '80vw' }" :style="{ width: '30vw' }" position="top">
            <div class="flex align-items-center flex-column pt-6 px-3">
              <i class="pi pi-info-circle" :style="{fontSize: '5rem', color: 'var(--red-500)' }"></i>
              <h5 style="margin-top: 1em">Login Error!</h5>
              <p style="text-align: center">
                You need to be logged in to make a reservation
              </p>
            </div>
            <template #footer>
              <div class="flex justify-content-center">
                <Button label="OK" @click="toggleDialogLogin" class="p-button-text" />
              </div>
            </template>
          </Dialog>

          <Dialog :visible="showHouseMessage" :breakpoints="{ '960px': '80vw' }" :style="{ width: '30vw' }" position="top">
            <div class="flex align-items-center flex-column pt-6 px-3">
              <i class="pi pi-info-circle" :style="{fontSize: '5rem', color: 'var(--red-500)' }"></i>
              <h5 style="margin-top: 1em">House Error!</h5>
              <p style="text-align: center">
                The house you are trying to see doesn't exist.
              </p>
            </div>
            <template #footer>
              <div class="flex justify-content-center">
                <Button label="OK" @click="toggleDialogHouse" class="p-button-text" />
              </div>
            </template>
          </Dialog>

          <div class="flex justify-content-center">
            <div class="card">
              <h5 class="text-center" style="margin-top: 1.5em;">{{ house.city}}</h5>
              <a class="text-center" style="text-decoration: none; font-size: 15px; color: #a0a0a0;">{{house.street}}, {{house.street_number}}, {{house.floor}}, {{house.door}}, {{house.house_dimension}}</a>
              <Toast/>
              <span id="favContainer" v-if="house.url === 'favorite'">
                  <Button id="favButtonGrid" icon="pi pi-heart-fill" @click="removeFavorite(house.house_id), house.url = 'not favorite'" class="p-button-rounded"/>
                </span>
              <span id="favContainer" v-else>
                  <Button id="favButtonGrid" icon="pi pi-heart" @click="addHouseToFavorites(house.house_id), house.url = 'favorite'" class="p-button-rounded"/>
                </span>
              <Tag id="tagHost" :value="house.house_owner_name" icon="pi pi-user" style="color: white; background-color: #2A323D"></Tag>
              <form @submit.prevent="handleSubmit(!v$.$invalid)" class="p-fluid">
                <div class="field">
                  <hr style="margin-top: -1em;" class="solid"/>
                </div>
                <div class="field" style="margin-top: -1em">
                  <div id="fieldRowContainer">
                    <div id="fieldRow" style="margin-right: 1em">
                      <span id="priceContainer" class="text font-semibold"><a>{{house.price}}€</a> day</span>
                    </div>
                    <div v-if="logged">
                      <div id="fieldRow" style="margin-top: 0.5em;position:absolute;right: 40%;" v-if="changingRating">
                        <Rating id="yourRating" v-model="yourRating" :stars="5"/>
                      </div>
                      <div id="fieldRow" style="margin-top: 0.5em;position:absolute;right: 40%;" v-else>
                        <Rating id="houseRating" :value="house.rating" :stars="5" :readonly="true" :cancel="false" class="ui-rating"></Rating>
                      </div>
                      <ToggleButton v-model="changingRating" onLabel="Add rating" offLabel="Change rating" onIcon="pi pi-send" offIcon="pi pi-pencil" style="width: 10em; position:absolute;right: 1vw; margin-top: -0.2em;" />
                    </div>
                    <div id="fieldRow" style="margin-top: 0.5em;position:absolute;right: 1em;" v-else>
                      <Rating id="houseRating" :value="house.rating" :stars="5" :readonly="true" :cancel="false" class="ui-rating"></Rating>
                    </div>
                  </div>
                </div>
                <div class="field">
                  <hr style="margin-top: -1em;" class="solid"/>
                </div>
                <div class="field">
                  <div class="p-float-label">
                    <Calendar id="checkInDate" :showIcon="true" v-model="v$.checkInDate.$model" :disabledDates="invalidDates" :manualInput="false" :class="{'p-invalid':v$.checkInDate.$invalid && submitted || (checkInDate !== null && !validInDate)}"/>
                    <label for="checkOutDate" :class="{'p-error':v$.checkInDate.$invalid && submitted}">Check-in*</label>
                  </div>
                  <small v-if="(v$.checkInDate.$invalid && submitted) || v$.checkInDate.$pending.$response" class="p-error">{{v$.checkInDate.required.$message.replace('Value', 'Check-in')}}</small>
                  <small v-if="checkInDate !== null && !validInDate" class="p-error">Check-in date has to be greater or equal than current date.</small>
                </div>
                <div class="field">
                  <div class="p-float-label">
                    <Calendar id="checkOutDate" :showIcon="true" v-model="v$.checkOutDate.$model" :disabledDates="invalidDates" :manualInput="false" :class="{'p-invalid':v$.checkOutDate.$invalid && submitted || (checkOutDate !== null && checkInDate >= checkOutDate) || (checkOutDate !== null && !validOutDate)}"/>
                    <label for="checkOutDate" :class="{'p-error':v$.checkOutDate.$invalid && submitted}">Check-out*</label>
                  </div>
                  <small v-if="(v$.checkOutDate.$invalid && submitted) || v$.checkOutDate.$pending.$response" class="p-error">{{v$.checkOutDate.required.$message.replace('Value', 'Check-out')}}</small>
                  <small v-if="checkOutDate !== null && checkInDate >= checkOutDate" class="p-error">Check-out date should be greater than check-in date.</small>
                  <small v-if="checkOutDate !== null && !validOutDate" class="p-error">Check-out date has to be greater or equal than current date.</small>
                </div>
                <div class="field" style="margin-top:-0.2em;">
                  <Accordion :multiple="true" :activeIndex="[]">
                    <AccordionTab header="Description">
                      <p>{{house.description}}</p>
                    </AccordionTab>
                  </Accordion>
                </div>
                <div class="field" style="margin-top: 3.2em" v-if="this.logged===true"></div>
                <div class="field" style="margin-top: -0.5em" v-else></div>
                <div class="field">
                  <div id="fieldRowContainer">
                    <div id="fieldRow" style="margin-right: 1em">
                      <a>Total</a>
                    </div>
                    <div id="fieldRow" style="position:absolute; right: 1em;">
                      <a>{{totalPrice}}€</a>
                    </div>
                  </div>
                </div>
                <div class="field">
                  <hr style="margin-top: -1em;" class="solid"/>
                </div>
                <div class="field" style="margin-top: -1em;">
                  <Button id="submitButton" type="submit" label="Reserve" class="mt-2"/>
                </div>
                <div class="field" style="margin-top: -1em" v-if="this.logged===false">
                  <label>Want to reserve? <a id="loginLink" class="link" @click="goToLogin" style="cursor: pointer; color: #8DD0FF; text-decoration: none; margin-top: -1em">Login now!</a></label>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
    <Footer id="footer"></Footer>
  </div>
</template>

<script>
import Header from './Header'
import Footer from './Footer'
import LoadingSpinner from './LoadingSpinner'
import axios from 'axios'
import { useVuelidate } from '@vuelidate/core'
import { required } from '@vuelidate/validators'
export default {
  name: 'HouseDetails',
  components: {
    Header,
    Footer,
    LoadingSpinner
  },
  setup: () => ({ v$: useVuelidate() }),
  data () {
    return {
      logged: false,
      username: null,
      token: null,
      house_id: null,
      checkInDate: null,
      checkOutDate: null,
      dates2: null,
      yourRating: 0,
      numberOfDays: 0,
      totalPrice: 0,
      validInDate: true,
      changingRating: true,
      validOutDate: true,
      loaderActive: false,
      userId: null,
      submitted: false,
      showSuccessMessage: false,
      showErrorMessage: false,
      showLoginMessage: false,
      myFavorites: [],
      showHouseMessage: false,
      error: '',
      invalidDates: [],
      house: {
        'city': 'City',
        'street': 'street',
        'street_number': 'street_number',
        'floor': 'floor',
        'door': 'door',
        'house_dimension': 'house_dimension'
      },
      houseImages: [{}],
      responsiveOptions: [
        {
          breakpoint: '1024px',
          numVisible: 5
        },
        {
          breakpoint: '768px',
          numVisible: 3
        },
        {
          breakpoint: '560px',
          numVisible: 1
        }
      ]
    }
  },
  watch: {
    // whenever checkInDate or checkOutDate change, these functions will run
    checkInDate () {
      if (this.checkOutDate != null) {
        this.getTotalPrice()
      }
      this.checkInDateValid()
    },
    checkOutDate () {
      if (this.checkInDate != null) {
        this.getTotalPrice()
      }
      this.checkOutDateValid()
    }
  },
  validations () {
    return {
      checkInDate: {
        required
      },
      checkOutDate: {
        required
      }
    }
  },
  methods: {
    getHouse () {
      const headers = {'Access-Control-Allow-Origin': '*'}
      const pathHouses = 'https://doogking.azurewebsites.net/api/housing/' + this.house_id + '/'
      axios.get(pathHouses, headers)
        .then((response) => {
          this.house = response.data
          var found = false
          for (let j = 0; j < this.myFavorites.length && found === false; j++) {
            if (this.house.house_id === this.myFavorites[j].housing.house_id) {
              this.house.url = 'favorite'
              found = true
            }
          }
        })
        .catch((error) => {
          this.error = error
          this.showHouseMessage = true
        })
    },
    getHouseImages () {
      const headers = {'Access-Control-Allow-Origin': '*'}
      const pathImageHouses = 'https://doogking.azurewebsites.net/api/housing_images/housing/' + this.house_id + '/'
      axios.get(pathImageHouses, headers).then(response => (this.houseImages = response.data))
    },
    getReservations () {
      const headers = {'Access-Control-Allow-Origin': '*'}
      const pathReservations = 'https://doogking.azurewebsites.net/api/reservations/?housing=' + this.house_id
      axios.get(pathReservations, headers)
        .then((res) => {
          for (let i = 0; i < res.data.length; i++) {
            var reservationStartDate = new Date(res.data[i].start_date)
            var reservationEndDate = new Date(res.data[i].end_date)
            var differenceInTimeRes = reservationEndDate.getTime() - reservationStartDate.getTime()
            // To calculate the no. of days between two dates
            var differenceInDaysRes = differenceInTimeRes / (1000 * 3600 * 24)
            let invalidDate = new Date(reservationStartDate.getTime())
            for (let i = 0; i <= differenceInDaysRes; i++) {
              this.invalidDates.push(new Date(invalidDate.getTime()))
              invalidDate.setDate(invalidDate.getDate() + 1)
            }
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          this.error = error
        })
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
          this.getHouse()
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
        this.$toast.add({severity: 'warn', summary: 'Warn message', detail: 'You need to login to add favorites', life: 2000})
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
            this.$toast.add({severity: 'info', summary: 'Favorite', detail: 'House added to your favorites list. You can see it in you profile', life: 3000})
          })
          .catch((error) => {
            this.error = error
          })
      }
    },
    handleSubmit (isFormValid) {
      this.submitted = true
      if (isFormValid && (this.checkOutDate !== null) && (this.checkInDate !== null) &&
        (this.checkInDate < this.checkOutDate) && (this.validInDate) && (this.validOutDate)) {
        if (this.logged === true) {
          this.goToPayment()
        } else {
          this.showLoginMessage = true
        }
      }
    },
    goToLogin () {
      // eslint-disable-next-line standard/object-curly-even-spacing
      this.$router.push({ path: '/login'})
    },
    // eslint-disable-next-line camelcase
    goToPayment () {
      localStorage.start_date = this.checkInDate.toDateString()
      localStorage.end_date = this.checkOutDate.toDateString()
      localStorage.house_id = this.house_id
      localStorage.pricePerDay = this.house.price
      localStorage.totalPrice = this.totalPrice
      localStorage.numberOfDays = this.numberOfDays
      localStorage.axiosStartDate = this.checkInDate.getFullYear() + '-' + this.checkInDate.toLocaleString('default', { month: '2-digit' }) + '-' + this.checkInDate.toLocaleString('default', { day: '2-digit' })
      localStorage.axiosEndDate = this.checkOutDate.getFullYear() + '-' + this.checkOutDate.toLocaleString('default', { month: '2-digit' }) + '-' + this.checkOutDate.toLocaleString('default', { day: '2-digit' })
      this.$router.push({path: '/payment', query: {house_id: this.house_id}})
    },
    goToHomepage () {
      this.$router.push({path: '/'})
    },
    checkInDateValid () {
      const today = new Date()
      today.setHours(0, 0, 0, 0)
      if (this.checkInDate < today) {
        this.validInDate = false
      } else {
        this.validInDate = true
      }
    },
    checkOutDateValid () {
      const today = new Date()
      today.setHours(0, 0, 0, 0)
      if (this.checkOutDate < today) {
        this.validOutDate = false
      } else {
        this.validOutDate = true
      }
    },
    getTotalPrice () {
      if (this.checkInDate < this.checkOutDate) {
        var date1 = new Date(this.checkInDate)
        var date2 = new Date(this.checkOutDate)
        var differenceInTime = date2.getTime() - date1.getTime()
        // To calculate the no. of days between two dates
        var differenceInDays = differenceInTime / (1000 * 3600 * 24)
        this.numberOfDays = differenceInDays
        this.totalPrice = differenceInDays * this.house.price
        if (isNaN(this.totalPrice)) {
          this.totalPrice = 0
        }
      } else {
        this.totalPrice = 0
      }
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
    resetForm () {
      this.checkOutDate = null
      this.checkInDate = null
    },
    toggleDialogError () {
      this.showErrorMessage = !this.showErrorMessage
      if (!this.showErrorMessage) {
        this.resetForm()
      }
    },
    toggleDialogLogin () {
      this.showLoginMessage = !this.showLoginMessage
      if (!this.showLoginMessage) {
        this.resetForm()
      }
    },
    toggleDialogHouse () {
      this.showHouseMessage = !this.showHouseMessage
      if (!this.showHouseMessage) {
        this.resetForm()
        this.goToHomepage()
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
        this.getUserFavorites()
      }
    }
  },
  created () {
    this.house_id = this.$route.query.house_id
    this.loadLocalStorage()
    this.getHouse()
    this.getHouseImages()
    this.getReservations()
    this.showLoader()
    setTimeout(() => {
      this.hideLoader()
    }, 800)
  }
}
</script>

<style scoped>
#houseContainer {
  display: flex;
  margin-left: 2em;
}
.houseDetails {
  flex: 1;
}
#fieldRowContainer {
  display: flex;
}
#fieldRow {
  float: left;
}
.houseDetails:first-child {
}
.flex-wrapper {
  background-color: #2A323D;
  display: flex;
  min-height: 100vh;
  flex-direction: column;
  justify-content: flex-start;
  overflow-x: hidden;
  align-content: center;
}
#imageHouse{
  height: 30.7vw;
  border-radius: 2em 2em 0 0;
  border: 5px solid #1c1b29;
}
#thumbnailImage{
  height: 6vw;
  width: 8.5vw;
  border-radius: 0.5em;
  border: 3px solid #1c1b29;
}
.form-demo .card {
  margin-top: 1rem;
  border-radius: 1rem;
  width: 41vw;
  background-color: #3d4755;
  color: white;
  margin-bottom: 1.5rem;
}
.form-demo .card form{
  margin-top: 2rem;
}
.form-demo .card .field{
  margin-bottom: 1.5rem;
  margin-left: 1rem;
  margin-right: 1rem;
}
.form-demo .card .field-checkbox{
  margin-bottom: 1.5rem;
  margin-left: 1rem;
  margin-right: 1rem;
}
.form-demo @media screen and (max-width: 960px) {
  .card {
    width: 80%;
  }
}
#favContainer{
  position:absolute;
  top: 0.7em;
  right: 1em;
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
#tagHost{
  position:absolute;
  top:1em;
  left:1.5em;
}
#priceContainer{
  font-size: 1em;
}
#priceContainer a{
  font-size: 1.5em;
}
</style>
