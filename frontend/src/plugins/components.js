import Vue from 'vue';
import VueKnob from '@websanova/vue-knob'

import Weather from '../components/Weather.vue'

// controller
import RemoteCamera from '../components/controllers/RemoteCamera.vue'

// sensor
import Temperature from '../components/sensors/Temperature'
import Humidity from '../components/sensors/Humidity'
import Illumination from '../components/sensors/Illumination'

// ui
import MTitle from '../components/ui/MTitle'

Vue.component('knob', VueKnob)

Vue.component('Weather', Weather)
Vue.component('RemoteCamera', RemoteCamera)

Vue.component('Temperature', Temperature)
Vue.component('Humidity', Humidity)
Vue.component('Illumination', Illumination)

Vue.component('MTitle', MTitle)
