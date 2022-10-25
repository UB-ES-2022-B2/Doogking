<template>
  <div class="flex-wrapper">
  <Header></Header>
    <HouseView></HouseView>
  <Footer></Footer>
  </div>
</template>
<script>
import Header from './Header'
import Footer from './Footer'
import HouseView from './HouseView'

export default {
  name: 'Homepage',
  components: {
    Header,
    Footer,
    HouseView
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

.dark-panel >>> .p-panel-header {
  background-color: var(--primary-color);
}

.flex-wrapper {
  display: flex;
  min-height: 100vh;
  flex-direction: column;
  justify-content: flex-start;
  overflow-x: hidden;
}
</style>
