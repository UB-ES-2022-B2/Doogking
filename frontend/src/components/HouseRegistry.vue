<template>
  <div class="flex-wrapper">
    <Header></Header>
    <Toast />
    <div>
        <b-form >
          <b-form-group
            location="b-form-group"
            label="Location"
            label-for="input-1"
          >
            <b-form-input
              id="input-1"
              v-model="location"
              type="location"
              placeholder="Introduce la ubicación"
              required
            ></b-form-input>
          </b-form-group>
        </b-form>
    </div>
    <FileUpload name="demo[]" :customUpload="true" @uploader="myUploader($event)" :multiple="true" accept="image/*" :maxFileSize="1000000">
      <template #empty>
        <div class="flex align-items-center justify-content-center flex-column">
          <i class="pi pi-cloud-upload border-2 border-circle p-5 text-8xl text-400 border-400" />
          <p class="mt-4 mb-0">Drag and drop files here to upload.</p>
        </div>
      </template>
    </FileUpload>
    </div>
      <b-button type="submit" variant="primary">Post</b-button>
      <b-button type="reset" variant="danger">Cancel</b-button>
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
</style>
