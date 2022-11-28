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
                  style="max-width: 39em; margin:1em;">
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
          <Dialog :visible="showSuccessMessage" :breakpoints="{ '960px': '80vw' }" :style="{ width: '30vw' }" position="top">
            <div class="flex align-items-center flex-column pt-6 px-3">
              <i class="pi pi-check-circle" :style="{fontSize: '5rem', color: 'var(--green-500)' }"></i>
              <h5 style="margin-top: 1em">Reservation Successful!</h5>
              <p style="text-align: center">
                Reservation created with Start date: <b>{{ this.checkInDate }}</b> and End date: <b>{{ this.checkOutDate }}</b>.
              </p>
            </div>
            <template #footer>
              <div class="flex justify-content-center">
                <Button label="OK" @click="toggleDialogSuccess" class="p-button-text" />
              </div>
            </template>
          </Dialog>

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

          <div class="flex justify-content-center">
            <div class="card">
              <h5 class="text-center" style="margin-top: 1.5em;">{{ house.city}}</h5>
              <a class="text-center" style="text-decoration: none; font-size: 15px; color: #a0a0a0;">{{house.street}}, {{house.street_number}}, {{house.floor}}, {{house.door}}, {{house.house_dimension}}</a>
              <Toast/>
              <span id="favContainer" v-if="house.favorite==true">
                        <Button id="favButtonGrid" icon="pi pi-heart-fill" @click="changeFavorite()" class="p-button-rounded"/>
                      </span>
              <span id="favContainer" v-else>
                        <Button id="favButtonGrid" icon="pi pi-heart" @click="changeFavorite()" class="p-button-rounded"/>
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
                    <div id="fieldRow" style="margin-top: 0.5em;position:absolute;right: 1em;">
                      <Rating :value="house.rating" :stars="5" :readonly="true" :cancel="false" class="ui-rating"></Rating>
                    </div>
                  </div>
                </div>
                <div class="field">
                  <hr style="margin-top: -1em;" class="solid"/>
                </div>
                <div class="field">
                  <div class="p-float-label">
                    <Calendar id="checkInDate" :showIcon="true" v-model="v$.checkInDate.$model" :class="{'p-invalid':v$.checkInDate.$invalid && submitted || (checkInDate !== null && !validInDate)}"/>
                    <label for="checkOutDate" :class="{'p-error':v$.checkInDate.$invalid && submitted}">Check-in*</label>
                  </div>
                  <small v-if="(v$.checkInDate.$invalid && submitted) || v$.checkInDate.$pending.$response" class="p-error">{{v$.checkInDate.required.$message.replace('Value', 'Check-in')}}</small>
                  <small v-if="checkInDate !== null && !validInDate" class="p-error">Check-in date has to be greater or equal than current date.</small>
                </div>
                <div class="field">
                  <div class="p-float-label">
                    <Calendar id="checkOutDate" :showIcon="true" v-model="v$.checkOutDate.$model" :class="{'p-invalid':v$.checkOutDate.$invalid && submitted || (checkOutDate !== null && checkInDate >= checkOutDate) || (checkOutDate !== null && !validOutDate)}"/>
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
      logged: null,
      username: null,
      token: null,
      house_id: null,
      checkInDate: null,
      checkOutDate: null,
      dates2: null,
      totalPrice: 0,
      validInDate: true,
      validOutDate: true,
      loaderActive: false,
      user_id: null,
      submitted: false,
      showSuccessMessage: false,
      showErrorMessage: false,
      showLoginMessage: false,
      error: '',
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
      axios.get(pathHouses, headers).then(response => (this.house = response.data))
    },
    getHouseImages () {
      const headers = {'Access-Control-Allow-Origin': '*'}
      const pathImageHouses = 'https://doogking.azurewebsites.net/api/housing_images/housing/' + this.house_id + '/'
      axios.get(pathImageHouses, headers).then(response => (this.houseImages = response.data))
    },
    makeReservation () {
      const headers = {'Access-Control-Allow-Origin': '*',
        'Authorization': 'Token ' + this.token
      }
      const parameters = {
        housing: 'https://doogking.azurewebsites.net/api/housing/' + this.house_id + '/',
        customer: 'https://doogking.azurewebsites.net/api/housing/' + this.user_id + '/',
        start_date: new Date(this.checkInDate),
        end_date: new Date(this.checkOutDate)
      }
      const path = 'https://doogking.azurewebsites.net/api/reservations/'
      axios.post(path, parameters, headers)
        .then((res) => {
          this.showSuccessMessage = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          this.error = error
          this.showErrorMessage = true
        })
    },
    handleSubmit (isFormValid) {
      this.submitted = true
      if (isFormValid && this.checkOutDate !== null && this.checkInDate < this.checkOutDate) {
        if (this.logged === true) {
          this.makeReservation()
        } else {
          this.showLoginMessage = true
        }
      }
    },
    goToLogin () {
      // eslint-disable-next-line standard/object-curly-even-spacing
      this.$router.push({ path: '/login'})
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
    toggleDialogSuccess () {
      this.showSuccessMessage = !this.showSuccessMessage
      if (!this.showSuccessMessage) {
        this.resetForm()
      }
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
    }
  },
  created () {
    this.logged = this.$route.query.logged === 'true'
    this.username = this.$route.query.username
    this.username = this.$route.query.username
    this.email = this.$route.query.email
    this.user_id = this.$route.query.user_id
    this.token = this.$route.query.token
    this.house_id = this.$route.query.house_id
    if (this.logged === undefined) {
      this.logged = false
    }
    this.getHouse()
    this.getHouseImages()
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
  height: 26em;
  border-radius: 2em 2em 0 0;
  border: 5px solid #1c1b29;
}

#thumbnailImage{
  height: 5em;
  width: 7em;
  border-radius: 0.5em;
  border: 3px solid #1c1b29;
}

.form-demo .card {
  margin-top: 1rem;
  border-radius: 1rem;
  width: 35rem;
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
