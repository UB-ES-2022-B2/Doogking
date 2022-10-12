<template>
  <div v-if="logged">
    <h4>"Hello World</h4>
  </div>
</template>

<script>
export default {
  data () {
    return {
      logged: false,
      username: null,
      token: null
    }
  },
  methods: {
    go_to_login () {
      // eslint-disable-next-line standard/object-curly-even-spacing
      this.$router.push({ path: '/login'})
    },
    login () {
      // eslint-disable-next-line standard/object-curly-even-spacing
      this.logged = true
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
}
</script>

<style scoped>
</style>
