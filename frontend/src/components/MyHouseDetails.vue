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
                <div class="field" style="margin-top:-0.2em;">
                  <Accordion :multiple="true" :activeIndex="[0]">
                    <AccordionTab header="Description">
                      <p>{{house.description}}</p>
                    </AccordionTab>
                  </Accordion>
                </div>
                <div class="field" style="margin-top: 3.2em" v-if="this.logged===true"></div>
                <div class="field" style="margin-top: -0.5em" v-else></div>
                <div class="field">
                  <hr style="margin-top: -1em;" class="solid"/>
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
      dates2: null,
      totalPrice: 0,
      validInDate: true,
      validOutDate: true,
      loaderActive: false,
      userId: null,
      showSuccessMessage: false,
      showErrorMessage: false,
      showLoginMessage: false,
      showHouseMessage: false,
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
  methods: {
    getHouse () {
      const headers = {'Access-Control-Allow-Origin': '*'}
      const pathHouses = 'https://doogking.azurewebsites.net/api/housing/' + this.house_id + '/'
      axios.get(pathHouses, headers)
        .then(response => (this.house = response.data))
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
    goToLogin () {
      // eslint-disable-next-line standard/object-curly-even-spacing
      this.$router.push({ path: '/login'})
    },
    goToHomepage () {
      this.$router.push({path: '/'})
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
    toggleDialogError () {
      this.showErrorMessage = !this.showErrorMessage
      if (!this.showErrorMessage) {
        this.resetForm()
      }
    },
    toggleDialogHouse () {
      this.showHouseMessage = !this.showHouseMessage
      if (!this.showHouseMessage) {
        this.resetForm()
        this.goToHomepage()
      }
    }
  },
  mounted () {
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
  },
  created () {
    this.house_id = this.$route.query.house_id
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
