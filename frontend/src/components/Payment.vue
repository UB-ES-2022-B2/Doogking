<template>
  <div class="flex-wrapper">
    <Header></Header>
    <div v-if="loaderActive===true" style="position: absolute; top: 24%; left: 49%">
      <LoadingSpinner :active="true"/></div>
    <div id="paymentContainer" v-else>
      <div id="paymentMethodContainer" class="payDetails">
        <div class="form-demo">
          <div class="flex justify-content-center">
            <div class="card">
              <h5 class="text-left" style="margin-top: 1.5em; margin-left: 1rem;">Payment method</h5>
              <a class="text-left" style="text-decoration: none; font-size: 15px; color: #a0a0a0; margin-left: 1rem;">Select your payment method</a>
              <Toast/>
              <form @submit.prevent="handleSubmit(!v$.$invalid)" class="p-fluid">
                <div class="field">
                  <hr style="margin-top: -1em;" class="solid"/>
                </div>
                <div class="field" style="margin-top: -1em">
                  <div id="fieldRowContainer">
                    <div id="fieldRow" style="margin-right: 1em">
                      <span id="priceContainer" class="text font-semibold"><a></a>Credit card</span>
                    </div>
                    <div id="fieldRow" style="margin-top: 0.5em;position:absolute;right: 1em;">
                      <div class="icons">
                        <img src="https://i.imgur.com/2ISgYja.png" width="30">
                        <img src="https://i.imgur.com/W1vtnOV.png" width="30">
                        <img src="https://i.imgur.com/35tC99g.png" width="30">
                        <img src="https://i.imgur.com/2ISgYja.png" width="30">
                      </div>
                    </div>
                  </div>
                </div>
                <div class="field">
                  <hr style="margin-top: -1em;" class="solid"/>
                </div>
                <div class="field">
                  <div class="p-float-label">
                    <InputMask id="cardNumber" v-model="v$.cardNumber.$model" mask="9999-9999-9999-9999" placeholder="                               xxxx-xxxx-xxxx-xxxx" :class="{'p-invalid':v$.cardNumber.$invalid && submitted}"/>
                    <label for="cardNumber" :class="{'p-error':v$.cardNumber.$invalid && submitted}">Card number* <i class="pi pi-credit-card"></i></label>
                  </div>
                  <small v-if="(v$.cardNumber.$invalid && submitted) || v$.cardNumber.$pending.$response" class="p-error">{{v$.checkInDate.required.$message.replace('Value', 'Card number')}}</small>
                </div>
                <div class="field">
                  <div class="p-float-label">
                    <Calendar id="expiryDate" :showIcon="true" v-model="v$.expiryDate.$model" :manualInput="false" :class="{'p-invalid':v$.expiryDate.$invalid && submitted || (expiryDate !== null && !validExpiryDate)}"/>
                    <label for="expiryDate" :class="{'p-error':v$.expiryDate.$invalid && submitted}">Expiry date*</label>
                  </div>
                  <small v-if="(v$.expiryDate.$invalid && submitted) || v$.expiryDate.$pending.$response" class="p-error">{{v$.expiryDate.required.$message.replace('Value', 'Expiry date')}}</small>
                  <small v-if="expiryDate !== null && !validExpiryDate" class="p-error">Expiry date has to be greater or equal than current date.</small>
                </div>
                <div class="field">
                  <div class="p-float-label">
                    <InputMask id="cvc" v-model="v$.cvc.$model" mask="999" placeholder="                   xxx" :class="{'p-invalid':v$.cvc.$invalid && submitted}"/>
                    <label for="cvc" :class="{'p-error':v$.cvc.$invalid && submitted}">CVC/CVV*</label>
                  </div>
                  <small v-if="(v$.cvc.$invalid && submitted) || v$.cvc.$pending.$response" class="p-error">{{v$.cvc.required.$message.replace('Value', 'CVC/CVV')}}</small>
                </div>
                <div class="field-checkbox" style="margin-top:-0.2em;">
                  <Checkbox style="margin-left: 1rem;" id="accept" name="accept" value="Accept" v-model="v$.accept.$model" :class="{'p-invalid':v$.accept.$invalid && submitted}" />
                  <label for="accept" style="font-size: 0.7em;" :class="{'p-error': v$.accept.$invalid && submitted}">By proceeding, you confirm that you are of legal age under the laws of your state and agree to the End User License Agreement (EULA).*</label>
                </div>
                <div class="field" style="margin-top: 3.2em" v-if="this.logged===true"></div>
                <div class="field" style="margin-top: -0.5em" v-else></div>
                <div class="field">
                  <div id="fieldRowContainer">
                    <div id="fieldRow" style="margin-right: 1em">
                      <i class="pi pi-lock"></i><a> Your transaction is secured with ssl certificate</a>
                    </div>
                    <div id="fieldRow" style="position:absolute; right: 1em;">
                      <a></a>
                    </div>
                  </div>
                </div>
                <div class="field">
                  <hr style="margin-top: -1em;" class="solid"/>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
      <div id="submitContainer" class="payDetails">
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
              <h5 class="text-left" style="margin-top: 1.5em; margin-left: 1rem;">Summary</h5>
              <a class="text-left" style="text-decoration: none; font-size: 15px; color: #a0a0a0; margin-left: 1rem;">These are the details of your reservation. Please verify the data before sending</a>
              <Toast/>
              <form @submit.prevent="handleSubmit(!v$.$invalid)" class="p-fluid">
                <div class="field">
                  <hr style="margin-top: -1em;" class="solid"/>
                </div>
                <div class="field" style="margin-top: 2em;">
                  <div class="p-float-label">
                    <Calendar id="checkInDate" :showIcon="true" v-model="v$.checkInDate.$model" :disabledDates="invalidDates"  style="pointer-events: none;" :manualInput="false"/>
                    <label for="checkInDate">Check-in</label>
                  </div>
                </div>
                <div class="field">
                  <div class="p-float-label">
                    <Calendar id="checkOutDate" :showIcon="true" v-model="v$.checkOutDate.$model" :disabledDates="invalidDates" style="pointer-events: none;" :manualInput="false"/>
                    <label for="checkOutDate">Check-out</label>
                  </div>
                </div>
                <div class="field" style="margin-top: 3.2em" v-if="this.logged===true"></div>
                <div class="field" style="margin-top: -0.5em" v-else></div>
                <div class="field">
                  <div id="fieldRowContainer">
                    <div id="fieldRow" style="margin-right: 1em; font-size: 0.8em;">
                      <a>Price per day</a>
                    </div>
                    <div id="fieldRow" style="position:absolute; right: 1em; font-size: 0.8em;">
                      <a>{{pricePerDay}}€</a>
                    </div>
                  </div>
                </div>
                <div class="field">
                  <div id="fieldRowContainer">
                    <div id="fieldRow" style="margin-right: 1em;  font-size: 0.8em;">
                      <a>Number of days</a>
                    </div>
                    <div id="fieldRow" style="position:absolute; right: 1em; font-size: 0.8em;">
                      <a>{{numberOfDays}} day</a>
                    </div>
                  </div>
                </div>
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
                  <Button id="submitButton" type="submit" label="Submit" class="mt-2"/>
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
      cardNumber: null,
      checkInDate: null,
      checkOutDate: null,
      axiosStartDate: null,
      axiosEndDate: null,
      expiryDate: null,
      validExpiryDate: null,
      cvc: null,
      dates2: null,
      numberOfDays: 0,
      totalPrice: 0,
      validInDate: true,
      validOutDate: true,
      loaderActive: false,
      userId: null,
      pricePerDay: 0,
      submitted: false,
      showSuccessMessage: false,
      showErrorMessage: false,
      showLoginMessage: false,
      showHouseMessage: false,
      error: '',
      accept: null,
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
    expiryDate () {
      this.checkValidExpiryDate()
    }
  },
  validations () {
    return {
      checkInDate: {
        required
      },
      checkOutDate: {
        required
      },
      cardNumber: {
        required
      },
      expiryDate: {
        required
      },
      cvc: {
        required
      },
      accept: {
        required
      }
    }
  },
  methods: {
    makeReservation () {
      var data = JSON.stringify({
        'housing': 'https://doogking.azurewebsites.net/api/housing/' + this.house_id + '/',
        'customer': 'https://doogking.azurewebsites.net/api/profiles/' + this.userId + '/',
        'start_date': this.axiosStartDate,
        'end_date': this.axiosEndDate
      })
      var config = {
        method: 'post',
        url: 'https://doogking.azurewebsites.net/api/reservations/',
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Authorization': 'Token ' + this.token,
          'Content-Type': 'application/json'
        },
        data: data
      }
      axios(config)
        .then((response) => {
          console.log(JSON.stringify(response.data))
          this.showSuccessMessage = true
        })
        .catch((error) => {
          console.log(error)
          this.error = error
          this.showErrorMessage = true
        })
    },
    handleSubmit (isFormValid) {
      this.submitted = true
      if (isFormValid) {
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
    checkValidExpiryDate () {
      const today = new Date()
      today.setHours(0, 0, 0, 0)
      if (this.expiryDate < today) {
        this.validExpiryDate = false
      } else {
        this.validExpiryDate = true
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
        this.$router.push({path: '/housedetails', query: {house_id: this.house_id}})
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
      }
      if (localStorage.start_date) {
        this.checkInDate = localStorage.start_date
      }
      if (localStorage.end_date) {
        this.checkOutDate = localStorage.end_date
      }
      if (localStorage.house_id) {
        this.house_id = localStorage.house_id
      }
      if (localStorage.pricePerDay) {
        this.pricePerDay = localStorage.pricePerDay
      }
      if (localStorage.numberOfDays) {
        this.numberOfDays = localStorage.numberOfDays
      }
      if (localStorage.totalPrice) {
        this.totalPrice = localStorage.totalPrice
      }
      if (localStorage.axiosStartDate) {
        this.axiosStartDate = localStorage.axiosStartDate
      }
      if (localStorage.axiosEndDate) {
        this.axiosEndDate = localStorage.axiosEndDate
      }
    }
  },
  created () {
    this.house_id = this.$route.query.house_id
    this.loadLocalStorage()
    this.showLoader()
    setTimeout(() => {
      this.hideLoader()
    }, 800)
  }
}
</script>

<style scoped>
#paymentContainer {
  display: flex;
  margin-left: 2em;
}
.payDetails {
  flex: 1;
}
#fieldRowContainer {
  display: flex;
}
#fieldRow {
  float: left;
}
.payDetails:first-child {
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
