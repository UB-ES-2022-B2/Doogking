// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import BootstrapVue from 'bootstrap-vue'
import '@/../bootstrap/css/bootstrap.css'
import Vue from 'vue'
import App from './App.vue'
import router from './router'

import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'

import PrimeVue from 'primevue/config'
import 'primevue/resources/themes/bootstrap4-dark-blue/theme.css'
import 'primevue/resources/primevue.min.css'
import 'primeicons/primeicons.css'
import 'primeflex/primeflex.css'

import Button from 'primevue/button'
import DataView from 'primevue/dataview'
import Dropdown from 'primevue/dropdown'
import DataViewLayoutOptions from 'primevue/dataviewlayoutoptions'
import Panel from 'primevue/panel'
import Dialog from 'primevue/dialog'
import Rating from 'primevue/rating'
import Tag from 'primevue/tag'
import Galleria from 'primevue/galleria'

library.add(fas, fab)
Vue.component('fa', FontAwesomeIcon)

Vue.use(BootstrapVue)
Vue.use(PrimeVue)
Vue.config.productionTip = false
Vue.component('Button', Button)
Vue.component('DataView', DataView)
Vue.component('DataViewLayoutOptions', DataViewLayoutOptions)
// eslint-disable-next-line vue/multi-word-component-names
Vue.component('Panel', Panel)
// eslint-disable-next-line vue/multi-word-component-names
Vue.component('Dropdown', Dropdown)
Vue.component('Dialog', Dialog)
Vue.component('Rating', Rating)
Vue.component('Tag', Tag)
Vue.component('Galleria', Galleria)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
