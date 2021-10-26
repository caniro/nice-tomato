<template>
  <div class="pa-3">
    <m-title icon="mdi-car"> 탐사 차량</m-title>

    <v-row>
      <v-col cols="12" :sm="6">
        <v-img :src="img_src"
          max-width="640" contain></v-img>
      </v-col>
      <v-col cols="12" :sm="6" class="text-center align-self-center">
        <direction-panel @direction="onDirection"></direction-panel>
      </v-col>
    </v-row>
  </div>
</template>

<script>
const RPI_CAR_IP = process.env.VUE_APP_RPI_CAR_IP;

export default {
  name: 'MonitoringCar',
  data() {
    return {
      img_src: "http://" + RPI_CAR_IP + ":8000/mjpeg/stream/"
    };
  },
  mounted() {
    console.log(this.img_src);
  },
  methods: {
    onDirection(dir) {
      console.log('direction:', dir);
      this.$mqtt.publish('iot/control/car', dir);
    }
  },
}
</script>

<style>

</style>
