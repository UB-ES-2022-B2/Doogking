<template>
  <form>
    <div class="flex-wrapper">
      <Header></Header>
      <div id="app">
        <div class="body">
          <div class="d-flex flex-row">
            <div class="p-2" style="margin-left:50px">
              <img class="mx-auto rounded-circle" src="@/assets/avatar.png" style="width:200px">
              <div class="profileButton-button">
                <button class="btn btn-lg btn-block" @click="goToUploadPhoto" name="forgotPassword"><u>Uploado Photo</u></button>
              </div>
            </div>
            <div class="p-2" style="margin-right:300px">
              <div class="info-containter" ><h2>{{username}}</h2>
                <div class="reviewButton">
                  <fa :icon="['fas', 'star']"/>
                  <button class="btn btn-lg btn-block" @click="goToReviews" name="goToLogIn">num. Reviews</button>
                </div>
                <div class="about-me"><h7>About me:</h7></div>
                <div class="row">
                  <div class="col"><fa :icon="['fas', 'location-dot']"/>      Location</div>
                  <div class="w-100"></div>
                  <div class="col"><fa :icon="['fas', 'envelope']"/>          {{username}}</div>
                  <div class="w-100"></div>
                  <div class="col"><fa :icon="['fas', 'house']"/>Num houses</div>
                </div>
              </div>
            </div>
            <div class="profile2Button-button" align-content="left">
              <button class="btn btn-lg btn-block" type="submit" @click="goToEditProfile" name="editProfile" aria-label="Left Align"><fa :icon="['fas', 'pen-to-square']"/><h6>Edit Profile</h6></button>
              <button class="btn btn-lg btn-block" type="submit" @click="logOut" name="editProfile" aria-label="Left Align"><fa :icon="['fas', 'right-from-bracket']"/><h6>Log out</h6></button>
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
      email: null,
      username: null,
      password: null,
      token: null,
      logged: false
    }
  },
  methods: {
    logOut () {
      this.logged = false
      // eslint-disable-next-line standard/object-curly-even-spacing
      this.$router.push({path: '/'})
    },
    goToEditProfile () {
      this.$router.push({ path: '/editProfile', query: {username: this.username, logged: this.logged, token: this.token} })
    }
  },
  created () {
    this.logged = this.$route.query.logged === 'true'
    this.username = this.$route.query.username
    this.email = this.$route.query.email
    this.token = this.$route.query.token
    if (this.logged === undefined) {
      this.logged = false
    }
  }
}
</script>

<style scoped>
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
  background-color: #6c757d;
  border-color: black;
  outline-style: none;
  border: none;
  color: white;
}

.info-containter{
  text-align: left;
  padding-left: 40px;
  font-size: 16px;
}

.about-me{
  margin-top: 15px;
}

.row{
  padding-left: 50px;
}

</style>
