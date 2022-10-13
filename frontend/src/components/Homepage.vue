<template>
  <div>
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
</style>
