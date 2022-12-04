<template>
  <form>
    <div class="flex-wrapper">
      <Header></Header>
      <div id="app">
        <div class="body">
          <div class="d-flex flex-row">
            <div class="p-2" style="margin-left:50px">
              <img class="mx-auto rounded-circle" src="@/assets/avatar.png" style="width:200px">
            </div>
            <div class="p-2" style="margin-right:200px">
              <div class="info-containter" ><h2>{{username}}</h2>
                <div class="reviewButton">
                  <fa :icon="['fas', 'star']"/>
                  <fa :icon="['fas', 'star']"/>
                  <fa :icon="['fas', 'star']"/>
                  <fa :icon="['fas', 'star']"/>
                  <fa :icon="['fas', 'star-half']"/>
                </div>
                <div class="about-me"><h7>About me:</h7></div>
                <div class="row">
                  <div class="col"><fa :icon="['fas', 'star']"/>      34 reviews</div>
                  <div class="w-100"></div>
                  <div class="col"><fa :icon="['fas', 'envelope']"/>          {{email}}</div>
                  <div class="w-100"></div>
                  <div class="col"><fa :icon="['fas', 'house']"/>       4</div>
                </div>
              </div>
            </div>
            <div class="profile2Button-button" align-content="left">
              <button class="btn btn-lg btn-block" type="submit" @click="goToEditProfile" name="editProfile" aria-label="Left Align"><fa :icon="['fas', 'pen-to-square']"/><h6>Edit Profile</h6></button>
              <button class="btn btn-lg btn-block" type="submit" style="color:#8dd0ff" @click="logOut" name="editProfile" aria-label="Left Align"><fa :icon="['fas', 'right-from-bracket']"/><h6>Log out</h6></button>
            </div>
            <br>
          </div>
          <hr>
        </div>
      </div>
      <Footer></Footer>
    </div>
  </form>
</template>

<script>
import Header from './Header'
import Footer from './Footer'

export default {
  components: {
    Header,
    Footer
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
    logOut () {
      this.logged = false
      // eslint-disable-next-line standard/object-curly-even-spacing
      this.$router.push({path: '/'})
    },
    goToEditProfile () {
      this.$router.push({ path: '/editProfile', query: { username: this.username, logged: this.logged, token: this.token, email: this.email, user_id: this.user_id } })
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
    console.log((this.username))
    console.log(this.email)
    console.log(this.logged)
    console.log(this.user_id)
    console.log(this.token)
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
.profileButton-button > :first-child {
  margin-top: 0.5em;
  align-content: center;
  background-color: white;
  border-color: white;
  outline-style: none;
  border: none;
  color: black;
}

.profile2Button-button > :first-child {
  margin-top: 0;
  align-content: center;
  background-color: #8dd0ff;
  border-color: #2a323d;
  outline-style: none;
  border: none;
  color: #2a323d;
}

.info-containter{
  text-align: left;
  padding-left: 40px;
  font-size: 16px;
  color: white;
}

.about-me{
  margin-top: 15px;
  color: white;
}

.row{
  padding-left: 50px;
  color: white;
}

</style>
