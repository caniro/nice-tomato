import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import './plugins/components.js'
import VueMqtt from 'vue-mqtt';

Vue.config.productionTip = false

const MQTT_BROKER_IP = process.env.VUE_APP_MQTT_BROKER_IP;

Vue.use(require('vue-moment'))
Vue.use(VueMqtt, 'ws://' + MQTT_BROKER_IP + ':9001/ws', 
    { clientID: "clientID-" + parseInt(Math.random() * 1000) });

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
