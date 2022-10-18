<template>
  <div class="flex-wrapper">
  <Header></Header>
  <Footer></Footer>
  </div>
</template>
<script>
import Header from './Header'
import Footer from './Footer'

export default {
  name: 'Homepage',
  components: {
    Header,
    Footer
  },
  data () {
    return {
      logged: null,
      username: null,
      token: null
    }
  },
  created () {
    this.logged = this.$route.query.logged === 'true'
    this.username = this.$route.query.username
    this.token = this.$route.query.token
    if (this.logged === undefined) {
      this.logged = false
    }
  }
}
</script>

<style scoped>
.flex-wrapper {
  display: flex;
  min-height: 100vh;
  flex-direction: column;
  justify-content: flex-start;
}
</style>
