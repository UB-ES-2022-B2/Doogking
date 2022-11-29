<template>
  <div class="flex-wrapper">
    <Header></Header>
    <Toast />
    <div class="flex justify-content-center">
      <div class="container">
        <h2 class="text-center" style="color:white; margin-bottom: -2rem; padding-top: 1rem;">House Registry</h2>
        <form @submit.prevent="handleSubmit(!v$.$invalid)" class="p-fluid">
          <div class="field">
            <hr style="margin-bottom: 1.5rem;" class="solid"/>
            <div class="p-float-label">
                  <span class="p-float-label">
                    <InputText id="city" type="text" v-model="value" />
                    <label for="city">What's the city? Ex: Barcelona</label>
                  </span>
              <h1></h1>
              <span class="p-float-label">
                <InputText id="street" type="text" v-model="value" />
                <label for="street">What's the Street? Ex: Gran Via de les Corts Catalanes, 585, Planta Baixa</label>
              </span>
              <h1></h1>
                <FileUpload name="demo[]" :customUpload="true" @uploader="myUploader($event)" :multiple="true" accept="image/*" :maxFileSize="1000000">
                  <template #empty>
                    <div class="flex align-items-center justify-content-center flex-column">
                      <i class="pi pi-cloud-upload border-2 border-circle p-5 text-8xl text-400 border-400" />
                      <p class="mt-4 mb-0">Drag and drop files here to upload.</p>
                    </div>
                  </template>
                </FileUpload>
              <h1></h1>
              <span class="p-float-label">
                <InputText id="price" type="number" v-model="value" />
                <label for="price">Price per day</label>
              </span>
              <h1></h1>
              <span class="p-float-label">
                <InputText id="description" type="text" v-model="value" />
                <label for="description">Add a description</label>
              </span>
              <h1></h1>
              <span class="p-float-label">
                <InputText id="email" type="text" v-model="value" />
                <label for="email">Write your mail</label>
              </span>
              <h1></h1>
              <div class="btn-group">
                <div class="flex align-items-center">
                  <Button label="Post" icon="pi pi-check" class="btnpost" />
                  <Button label="Delete" icon="pi pi-trash" class="btndelete"/>
                </div>
              </div>
            </div>
            </div>
        </form>
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
      const path = 'https://doogking.azurewebsites.net/api/houses/'
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
