<template>
  <div class="flex-wrapper">
    <Header></Header>
    <div id="app">
      <h2 style="color:white; margin-bottom: 40px; margin-left: 165px" class="d-flex justify-content-start">Hey {{username}}! Start listing your place</h2>
      <div class="body">
        <div class="d-flex flex-row">
          <div class="p-2" style="margin-left:150px">
            <FileUpload name="demo[]" :customUpload="true" @uploader="myUploader($event)" :multiple="true" accept="image/*" :maxFileSize="1000000">
              <template #empty>
                <div class="flex align-items-center justify-content-center flex-column">
                  <i class="pi pi-cloud-upload border-2 border-circle p-5 text-8xl text-400 border-400" />
                  <p class="mt-4 mb-0">Drag and drop files here to upload.</p>
                </div>
              </template>
            </FileUpload>
          </div>
            <div class="p-2" style="width:500px">
              <form @submit.prevent="handleSubmit(!v$.$invalid)" class="p-fluid">
                <div class="field">
                  <div class="p-float-label">
                    <span class="p-float-label">
                      <InputText id="street" type="text" class="form-control" v-model="addUserForm.street" aria-describedby="inputGroupPrepend2" placeholder="Street" />
                    </span>
                    <h1></h1>
                    <span class="p-float-label" style="margin-right:30px">
                      <InputText id="street number" type="text" autofocus v-model="addUserForm.street_number" aria-describedby="inputGroupPrepend2" style="width:130px" placeholder="Street Number"/>
                      <InputText id="floor" type="text" v-model="addUserForm.floor" aria-describedby="inputGroupPrepend2" style="width:80px" placeholder="Floor"/>
                      <InputText id="door" type="text" v-model="addUserForm.door" aria-describedby="inputGroupPrepend2" style="width:80px" placeholder="Door"/>
                      <InputText id="house_dimension" type="text" v-model="addUserForm.house_dimension" aria-describedby="inputGroupPrepend2" style="width:150px" placeholder="House Dimension"/>
                    </span>
                    <h1></h1>
                  <div class="p-float-label">
                    <InputText id="city" type="text" v-model="value" placeholder="City" />
                  </div>
                    <h1></h1>
                    <span class="p-float-label">
                <InputText id="price" type="number" class="form-control" v-model="addUserForm.price" aria-describedby="inputGroupPrepend2" placeholder="Price per day" />
              </span>
                    <h1></h1>
                    <span class="p-float-label">
                <InputText id="description" type="text" class="form-control" v-model="addUserForm.desciption" aria-describedby="inputGroupPrepend2" style="height:100px" placeholder="Description"/>
              </span>
                    <h1></h1>
                    <div class="btn-group">
                      <div class="field">
                        <Button id="submitButton" type="submit" label="Submit" @click='goPostHouse' class="mt-2" style="width:200px"/>
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
      user_id: null,
      token: null,
      street: null,
      street_number: null,
      floor: null,
      door: null,
      house_dimension: null,
      house_owner: null,
      house_owner_name: null,
      price_per_day: null,
      desciption: null,
      addUserForm: {
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
      var data = JSON.stringify({
        'street': this.addUserForm.street,
        'street_number': this.addUserForm.street_number,
        'floor': this.addUserForm.floor,
        'door': this.addUserForm.door,
        'house_dimension': this.addUserForm.house_dimension,
        'house_owner': 'https://doogking.azurewebsites.net/api/profile/' + this.user_id + '/',
        'house_owner_name': this.username,
        'price_per_day': this.addUserForm.price_per_day,
        'desciption': this.addUserForm.desciption
      })
      var config = {
        method: 'post',
        url: 'https://doogking.azurewebsites.net/api/housing/' + this.user_id + '/',
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Authorization': 'Token ' + this.token,
          'Content-Type': 'application/json'
        },
        data: data
      }
      console.log('Token ' + this.token)
      axios(config)
        .then(function (response) {
        }).catch(function (response) {})
    },
    myUploader (event) {
      alert(event.files[0].objectURL)
      const formData = new FormData()
      formData.append('file', event.files[0])
      axios
        .post('http://localhost:8000/api/upload/', formData)
        .then(() => {
          console.log('SUCCESS')
        })
      this.$toast.add({ severity: 'info', summary: 'Success', detail: 'File Uploaded', life: 3000 })
    }
  },
  created () {
    this.logged = this.$route.query.logged === 'true'
    this.username = this.$route.query.username
    this.email = this.$route.query.email
    this.user_id = this.$route.query.user_id
    this.token = this.$route.query.token
    if (this.logged === undefined) {
      this.logged = false
    }
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
