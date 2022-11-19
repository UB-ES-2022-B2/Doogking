<template>
  <div class="flex-wrapper">
    <Header></Header>
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
    <Footer id="footer"></Footer>
  </div>
</template>

<script>
import Header from './Header'
import Footer from './Footer'
import axios from 'axios'

export default {
  name: 'HouseDetails',
  components: {
    Header,
    Footer
  },
  data () {
    return {
      logged: null,
      username: null,
      token: null,
      house_id: null,
      house: null,
      titleIm: 'holaaa',
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
  methods: {
    getHouse () {
      const headers = {'Access-Control-Allow-Origin': '*'}
      const pathHouses = 'https://doogking.azurewebsites.net/api/housing/' + this.house_id + '/'
      axios.get(pathHouses, headers).then(response => (this.house = response.data))
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
.flex-wrapper {
  background-color: #2A323D;
  display: flex;
  min-height: 100vh;
  flex-direction: column;
  justify-content: flex-start;
  overflow-x: hidden;
  align-content: center;
}

#footer{
  flex: 1;
}

#imageHouse{
  height: 25em;
  width: 1em;
  border-radius: 2em 2em 0 0;
  border: 5px solid #1c1b29;
}

#thumbnailImage{
  height: 5em;
  width: 7em;
  border-radius: 0.5em;
  border: 3px solid #1c1b29;
}
</style>
