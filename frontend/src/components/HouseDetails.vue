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
            <p>{{house.street}},{{house.street_number}},{{house.floor}},{{house.door}},{{house.house_dimension}}</p>
          </template>
        </Galleria>
      </div>
      <div id="detailsContainer" class="houseDetails">
        <div class="form-demo">
          <div class="flex justify-content-center">
            <div class="card">
              <label class="text-center" style="margin-top: 1em; font-weight: 600; font-size: 20px;">{{ house.city}} <a style="text-decoration: none; font-size: 15px; color: #a0a0a0;">{{house.street}}, {{house.street_number}}, {{house.floor}}, {{house.door}}, {{house.house_dimension}}</a></label>
              <form @submit.prevent="handleSubmit(!v$.$invalid)" class="p-fluid">
                <div class="field" style="margin-top: -1em">
                  <Button id="submitButton" type="submit" label="Reserve" class="mt-2"/>
                </div>
                <div class="field" style="margin-top: -1em">
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
      house: null,
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
  validations () {
    return {
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
      if (isFormValid) {
      }
    },
    goToLogin () {
      // eslint-disable-next-line standard/object-curly-even-spacing
      this.$router.push({ path: '/login'})
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
}

.houseDetails {
  flex: 1;
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
  height: 25em;
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
  margin-top: 1.5rem;
  border-radius: 1rem;
  min-width: 35rem;
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
</style>
