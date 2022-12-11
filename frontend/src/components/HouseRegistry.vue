<template>
  <div class="flex-wrapper">
    <Header></Header>
    <Dialog :visible="showSuccessMessage" :breakpoints="{ '960px': '80vw' }" :style="{ width: '30vw' }" position="top">
      <div class="flex align-items-center flex-column pt-6 px-3">
        <i class="pi pi-info-circle" :style="{fontSize: '5rem', color: 'var(--green-500)' }"></i>
        <h5 style="margin-top: 1em">Posted House Successful!</h5>
        <p style="text-align: center">
          Your house has been posted. Now other users can rent it!
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
        <h5 style="margin-top: 1em">Posted House Error!</h5>
        <p style="text-align: center">
          Please enter a valid house/images.
        </p>
      </div>
      <template #footer>
        <div class="flex justify-content-center">
          <Button label="OK" @click="toggleDialogError" class="p-button-text" />
        </div>
      </template>
    </Dialog>
    <Dialog :visible="showImagesMessage" :breakpoints="{ '960px': '80vw' }" :style="{ width: '30vw' }" position="top">
      <div class="flex align-items-center flex-column pt-6 px-3">
        <i class="pi pi-info-circle" :style="{fontSize: '5rem', color: 'var(--red-500)' }"></i>
        <h5 style="margin-top: 1em">Missing images!</h5>
        <p style="text-align: center">
          You have to upload at least one image before submitting your new house.
        </p>
      </div>
      <template #footer>
        <div class="flex justify-content-center">
          <Button label="OK" @click="toggleDialogImages" class="p-button-text" />
        </div>
      </template>
    </Dialog>
    <div id="app">
      <h5 style="color:white; margin-left: 165px" class="d-flex justify-content-start">Hey {{username}}! Start listing your place</h5>
      <hr style="width:24.3vw; color: white; margin-bottom: 40px; margin-left: 165px" class="solid"/>
      <h6 class="font-italic" style="color:white; margin-bottom: 5px; margin-right: 135px">To post a house, please upload your chosen images, then click on the upload button and then fill the house details</h6>
      <div class="body">
        <div class="d-flex flex-row">
          <div class="p-2" style="margin-left:150px">
            <FileUpload name="demo[]" :customUpload="true" @uploader="myUploader($event)" :multiple="true" accept="image/*" :maxFileSize="1000000">
              <template #empty>
                <div class="flex align-items-center justify-content-center flex-column">
                  <i class="pi pi-cloud-upload border-2 border-circle p-5 text-8xl text-400 border-400" />
                  <p class="mt-4 mb-0">Drag and drop images here.</p>
                </div>
              </template>
            </FileUpload>
          </div>
          <div class="p-2" style="width:500px">
            <form class="p-fluid">
              <div class="field">
                <div class="p-float-label">
                    <span class="p-float-label">
                      <InputText id="street" type="text" class="form-control" v-model="addUserForm.street" aria-describedby="inputGroupPrepend2" placeholder="Street" />
                    </span>
                  <h1></h1>
                  <span class="p-float-label" style="margin-right:30px">
                      <InputText id="street_number" type="text" autofocus v-model="addUserForm.street_number" aria-describedby="inputGroupPrepend2" style="width:130px" placeholder="Street Number"/>
                      <InputText id="floor" type="text" v-model="addUserForm.floor" aria-describedby="inputGroupPrepend2" style="width:80px" placeholder="Floor"/>
                      <InputText id="door" type="text" v-model="addUserForm.door" aria-describedby="inputGroupPrepend2" style="width:80px" placeholder="Door"/>
                      <InputText id="house_dimension" type="text" v-model="addUserForm.house_dimension" aria-describedby="inputGroupPrepend2" style="width:150px" placeholder="House Dimension"/>
                    </span>
                  <h1></h1>
                  <div class="p-float-label">
                    <InputText id="city" type="text" class="form-control" v-model="addUserForm.city" aria-describedby="inputGroupPrepend2" placeholder="City" />
                  </div>
                  <h1></h1>
                  <span class="p-float-label">
                <InputText id="price" type="number" class="form-control" v-model="addUserForm.price_per_day" aria-describedby="inputGroupPrepend2" placeholder="Price per day" />
              </span>
                  <h1></h1>
                  <span class="p-float-label">
                <InputText id="description" type="text" class="form-control" v-model="addUserForm.desciption" aria-describedby="inputGroupPrepend2" style="height:100px" placeholder="Description"/>
              </span>
                  <h1></h1>
                  <div class="btn-group">
                    <div class="field">
                      <Button id="submitButton" type="button" label="Submit" @click='goPostHouse($event)' class="mt-2" style="width:200px"/>
                    </div>
                  </div>
                </div>
              </div>
            </form>
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
import HouseView from './HouseView'
import axios from 'axios'

export default {
  components: {
    Header,
    Footer,
    HouseView
  },
  data () {
    return {
      logged: null,
      username: null,
      email: null,
      userId: null,
      token: null,
      street: null,
      street_number: null,
      uploadedFiles: false,
      floor: null,
      door: null,
      house_dimension: null,
      house_owner: null,
      house_owner_name: null,
      price_per_day: null,
      desciption: null,
      numHouses: null,
      house_id: null,
      images: [],
      showSuccessMessage: false,
      showErrorMessage: false,
      showImagesMessage: false,
      addUserForm: {
        city: null,
        street: null,
        street_number: null,
        floor: null,
        door: null,
        house_dimension: null,
        price_per_day: null,
        desciption: null
      }
    }
  },
  methods: {
    goPostHouse () {
      if (this.uploadedFiles === false) {
        this.showImagesMessage = true
      } else {
        var data = JSON.stringify({
          'city': this.addUserForm.city,
          'street': this.addUserForm.street,
          'street_number': this.addUserForm.street_number,
          'floor': this.addUserForm.floor,
          'door': this.addUserForm.door,
          'house_dimension': this.addUserForm.house_dimension,
          'price': this.addUserForm.price_per_day,
          'description': this.addUserForm.desciption,
          'house_owner': 'https://doogking.azurewebsites.net/api/profiles/' + this.userId + '/'
        })
        var config = {
          method: 'post',
          url: 'https://doogking.azurewebsites.net/api/housing/',
          headers: {
            'Access-Control-Allow-Origin': '*',
            'Authorization': 'Token ' + this.token,
            'Content-Type': 'application/json'
          },
          data: data
        }
        console.log('Token ' + this.token)
        axios(config)
          .then((res) => {
            this.goPostHouseImage(res.data.house_id)
            this.showSuccessMessage = true
          })
          .catch((response) => {
            this.showErrorMessage = true
          })
      }
    },
    goPostHouseImage (houseId) {
      for (let i = 0; i < this.images.length; i++) {
        const formData = new FormData()
        formData.append('housing', 'https://doogking.azurewebsites.net/api/housing/' + houseId + '/')
        formData.append('index', i)
        formData.append('image', this.images[i])
        var config = {
          method: 'post',
          url: 'https://doogking.azurewebsites.net/api/housing_images/',
          headers: {
            'Access-Control-Allow-Origin': '*',
            'Authorization': 'Token ' + this.token,
            'Content-Type': 'multipart/form-data'
          },
          data: formData
        }
        console.log('Token ' + this.token)
        axios(config)
          .then((response) => {
            this.showSuccessMessage = true
          }).catch(function (response) {})
      }
    },
    myUploader (event) {
      this.uploadedFiles = true
      for (let i = 0; i < event.files.length; i++) {
        this.images.push(event.files[i])
      }
    },
    getNumHouses () {
      const headers = {'Access-Control-Allow-Origin': '*'}
      const pathHouses = 'https://doogking.azurewebsites.net/api/housing/'
      const promise = axios.get(pathHouses, headers)
      Promise.resolve(promise).then((value) => (this.numHouses = value.data.length))
    },
    toggleDialogSuccess () {
      this.showSuccessMessage = !this.showSuccessMessage
      if (!this.showSuccessMessage) {
        this.$router.push({ path: '/' })
        this.resetForm()
      }
    },
    toggleDialogError () {
      this.showErrorMessage = !this.showErrorMessage
      if (!this.showErrorMessage) {
        this.resetForm()
      }
    },
    toggleDialogImages () {
      this.showImagesMessage = !this.showImagesMessage
      if (!this.showImagesMessage) {
        this.resetForm()
      }
    },
    resetForm () {
      this.addUserForm.street = ''
      this.addUserForm.street_number = ''
      this.addUserForm.floor = ''
      this.addUserForm.door = ''
      this.addUserForm.house_dimension = ''
      this.addUserForm.city = ''
      this.addUserForm.price_per_day = ''
      this.addUserForm.desciption = ''
      this.submitted = false
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
    this.getNumHouses()
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

.btnpost {
  aligned: center;
  background-color: #61A803;
  border-color: #61A803;
}

.btndelete {
  aligned: center;
  background-color: #F03420;
  border-color: #F03420;
}

</style>
