<template>
  <div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      logged: false
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
    }
  }
}
</script>

<style scoped>
</style>
