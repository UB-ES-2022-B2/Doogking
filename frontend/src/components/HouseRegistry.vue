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
                      <InputText id="street" type="text" v-model="value" placeholder="Street" />
                    </span>
                    <h1></h1>
                    <span class="p-float-label" style="margin-right:145px">
                      <InputText id="street number" type="text" v-model="value" style="width:130px" placeholder="Street Number"/>
                      <InputText id="floor" type="text" v-model="value" style="width:100px" placeholder="Floor"/>
                      <InputText id="door" type="text" v-model="value" style="width:100px" placeholder="Door"/>
                    </span>
                    <h1></h1>
                  <div class="p-float-label">
                    <InputText id="city" type="text" v-model="value" placeholder="City" />
                  </div>
                    <h1></h1>
                    <span class="p-float-label" style="margin-right:1px">
                      <InputText id="house_dimension" type="text" v-model="value" style="width:150px" placeholder="House Dimension"/>
                      <InputText id="house_owner" type="text" v-model="value" style="width:150px" placeholder="House Owner"/>
                      <InputText id="house_owner_name" type="text" v-model="value" style="width:174px" placeholder="House Owner Name"/>
                    </span>
                    <h1></h1>
                    <span class="p-float-label">
                <InputText id="price" type="number" v-model="value" placeholder="Price per day" />
              </span>
                    <h1></h1>
                    <span class="p-float-label">
                <InputText id="description" type="text" v-model="value" style="height:100px" placeholder="Description"/>
              </span>
                    <h1></h1>
                    <div class="btn-group">
                      <div class="field">
                        <Button id="submitButton" type="submit" label="Submit" class="mt-2" style="width:200px"/>
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
      token: null
    }
  },
  methods: {
    checkRegisterHouse () {
      const headers = {'Access-Control-Allow-Origin': '*'}
      const parameters = {
        city: this.city,
        street: this.street,
        description: this.description,
        price: this.price
      }
      const path = 'https://doogking.azurewebsites.net/api/housing/'
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
