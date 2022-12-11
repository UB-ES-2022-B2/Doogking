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
import MultiSelect from 'primevue/multiselect'
import Calendar from 'primevue/calendar'
import Divider from 'primevue/divider'
import Toast from 'primevue/toast'
import ConfirmationService from 'primevue/confirmationservice'
import ToastService from 'primevue/toastservice'
import ConfirmPopup from 'primevue/confirmpopup'
import Galleria from 'primevue/galleria'
import Accordion from 'primevue/accordion'
import AccordionTab from 'primevue/accordiontab'
import ProgressSpinner from 'primevue/progressspinner'
import Password from 'primevue/password'
import InputText from 'primevue/inputtext'
import Checkbox from 'primevue/checkbox'
import SplitButton from 'primevue/splitbutton'
import Carousel from 'primevue/carousel'
import FileUpload from 'primevue/fileupload'
import Slider from 'primevue/slider'

library.add(fas, fab)
Vue.component('fa', FontAwesomeIcon)

Vue.use(BootstrapVue)
Vue.use(PrimeVue)
Vue.use(ConfirmationService)
Vue.use(ToastService)

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
Vue.component('MultiSelect', MultiSelect)
Vue.component('Calendar', Calendar)
Vue.component('Divider', Divider)
Vue.component('Dialog ', Dialog)
Vue.component('Toast', Toast)
Vue.component('ConfirmPopup', ConfirmPopup)
Vue.component('Galleria', Galleria)
Vue.component('Accordion', Accordion)
Vue.component('AccordionTab', AccordionTab)
Vue.component('ProgressSpinner', ProgressSpinner)
Vue.component('Password', Password)
Vue.component('InputText', InputText)
Vue.component('Checkbox', Checkbox)
Vue.component('SplitButton', SplitButton)
Vue.component('Carousel', Carousel)
Vue.component('FileUpload', FileUpload)
Vue.component('Slider', Slider)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
