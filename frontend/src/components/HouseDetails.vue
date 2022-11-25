<template>
  <div class="flex-wrapper">
    <Header></Header>
    <div id="houseContainer">
      <div id="galleriaContainer" class="houseDetails">
        <Galleria id="galleriaHouse" :value="images" :responsiveOptions="responsiveOptions" :numVisible="3"
                  :showItemNavigators="true" :showItemNavigatorsOnHover="true"
                  :circular="true" :autoPlay="true" :transitionInterval="3000"
                  style="max-width: 39em; margin:1em;">
          <template #item="{item}">
            <img id="imageHouse" :src="item.itemImageSrc" :alt="item.alt" style="width: 100%; display: block;" />
          </template>
          <template #thumbnail="{item}">
            <div class="grid grid-nogutter justify-content-center">
              <img id="thumbnailImage" :src="item.thumbnailImageSrc" :alt="item.alt" style="display: block;" />
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
          <div class="flex justify-content-center">
            <div class="card">
              <h5 class="text-center" style="margin-top: 1.5em;">{{ house.city}}</h5>
              <a class="text-center" style="text-decoration: none; font-size: 15px; color: #a0a0a0;">{{house.street}}, {{house.street_number}}, {{house.floor}}, {{house.door}}, {{house.house_dimension}}</a>
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
                    <Calendar id="checkInDate" :showIcon="true" v-model="v$.checkInDate.$model" :class="{'p-invalid':v$.checkInDate.$invalid && submitted}"/>
                    <label for="checkOutDate" :class="{'p-error':v$.checkInDate.$invalid && submitted}">Check-in*</label>
                  </div>
                  <small v-if="(v$.checkInDate.$invalid && submitted) || v$.checkInDate.$pending.$response" class="p-error">{{v$.checkInDate.required.$message.replace('Value', 'Check-in')}}</small>
                </div>
                <div class="field">
                  <div class="p-float-label">
                    <Calendar id="checkOutDate" :showIcon="true" v-model="v$.checkOutDate.$model" :class="{'p-invalid':v$.checkOutDate.$invalid && submitted || (checkOutDate !== null && checkInDate >= checkOutDate)}"/>
                    <label for="checkOutDate" :class="{'p-error':v$.checkOutDate.$invalid && submitted}">Check-out*</label>
                  </div>
                  <small v-if="(v$.checkOutDate.$invalid && submitted) || v$.checkOutDate.$pending.$response" class="p-error">{{v$.checkOutDate.required.$message.replace('Value', 'Check-out')}}</small>
                  <small v-if="checkOutDate !== null && checkInDate >= checkOutDate" class="p-error">Check-out date should be greater than check-in date</small>
                </div>
                <div class="field" style="margin-top: -1em;">
                  <Accordion :multiple="true" :activeIndex="[]">
                    <AccordionTab header="Description">
                      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
                        ut labore et dolore magna aliqua. Ut enim ad minim veniam.</p>
                    </AccordionTab>
                  </Accordion>
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
                  <Button id="submitButton" type="submit" label="Reserve" class="mt-2"/>
                </div>
                <div class="field" style="margin-top: -1em" v-if="this.logged===false">
                  <label>Want to reserve? <a class="link" @click="goToLogin" style="cursor: pointer; color: #8DD0FF; text-decoration: none; margin-top: -1em">Login now!</a></label>
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
import axios from 'axios'
import { useVuelidate } from '@vuelidate/core'
import { required } from '@vuelidate/validators'

export default {
  name: 'HouseDetails',
  components: {
    Header,
    Footer
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
      house: {
        'city': 'City',
        'street': 'street',
        'street_number': 'street_number',
        'floor': 'floor',
        'door': 'door',
        'house_dimension': 'house_dimension'
      },
      submitted: false,
      images: [
        {
          'itemImageSrc': 'https://doogkingteststorage.blob.core.windows.net/media/01niu-refugi_NoQaX10.jpg',
          'thumbnailImageSrc': 'https://doogkingteststorage.blob.core.windows.net/media/01niu-refugi_NoQaX10.jpg',
          'alt': 'Description for Image 1',
          'title': 'Title 1'
        },
        {
          'itemImageSrc': 'https://doogkingteststorage.blob.core.windows.net/media/L_015738_hotel-rural-catalunya.jpg',
          'thumbnailImageSrc': 'https://doogkingteststorage.blob.core.windows.net/media/L_015738_hotel-rural-catalunya.jpg',
          'alt': 'Description for Image 1',
          'title': 'Title 1'
        },
        {
          'itemImageSrc': 'https://doogkingteststorage.blob.core.windows.net/media/15206073607515_9DjC83v.jpg',
          'thumbnailImageSrc': 'https://doogkingteststorage.blob.core.windows.net/media/15206073607515_9DjC83v.jpg',
          'alt': 'Description for Image 2',
          'title': 'Title 2'
        }
      ],
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
    // whenever checkInDate or checkOutDateChenge, these functions will run
    checkInDate () {
      if (this.checkOutDate != null) {
        this.getTotalPrice()
      }
    },
    checkOutDate () {
      if (this.checkInDate != null) {
        this.getTotalPrice()
      }
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
    handleSubmit (isFormValid) {
      this.submitted = true
      if (isFormValid && this.checkOutDate !== null && this.checkInDate < this.checkOutDate) {
      }
    },
    goToLogin () {
      // eslint-disable-next-line standard/object-curly-even-spacing
      this.$router.push({ path: '/login'})
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
    }
  },
  created () {
    this.logged = this.$route.query.logged === 'true'
    this.username = this.$route.query.username
    this.token = this.$route.query.token
    this.house_id = this.$route.query.house_id
    if (this.logged === undefined) {
      this.logged = false
    }
    this.getHouse()
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
