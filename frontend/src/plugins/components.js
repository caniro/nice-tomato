import Vue from 'vue';
import VueKnob from '@websanova/vue-knob'

import Weather from '../components/Weather.vue'

// controller
import RemoteCamera from '../components/controllers/RemoteCamera.vue'
import DirectionPanel from '../components/controllers/DirectionPanel.vue'

// sensor
import Temperature from '../components/sensors/Temperature'
import Humidity from '../components/sensors/Humidity'
import Illumination from '../components/sensors/Illumination'
import SensorChart from '../components/sensors/SensorChart'
import DataLoading from '../components/sensors/DataLoading'

// ui
import MTitle from '../components/ui/MTitle'

Vue.component('knob', VueKnob)

Vue.component('Weather', Weather)

Vue.component('RemoteCamera', RemoteCamera)
Vue.component('DirectionPanel', DirectionPanel)

Vue.component('Temperature', Temperature)
Vue.component('Humidity', Humidity)
Vue.component('Illumination', Illumination)
Vue.component('SensorChart', SensorChart)
Vue.component('DataLoading', DataLoading)

Vue.component('MTitle', MTitle)
