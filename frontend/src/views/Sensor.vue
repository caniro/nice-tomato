<template>
  <div class="pa-3">
    <div class="my-3">
      <div v-if="Object.keys(sensors).length === 0">데이터 수신 중...</div>

      <div v-for="(sections, place) in sensors" :key="place" class="pa-1 pb-3">
        <m-title icon="fas fa-seedling"> {{ place }}</m-title>
        <hr color="lightgray">
        <div v-for="(devices, section) in sections" :key="section"
            class="border pa-1 pb-3 text-center">
          <h3 class="indigo--text mb-3">{{ section }}</h3>
          <v-row>
            <v-col class="px-3 py-1" cols="12" sm="4"
                  v-for="(value, device) in devices" :key="device">
              <temperature v-if="device==='temp'" :value="value"></temperature>
              <humidity v-if="device==='humi'" :value="value"></humidity>
              <illumination v-if="device==='illu'" :value="value"></illumination>
            </v-col>
          </v-row>
        </div>
      </div>

      <!-- <hr class="my-3 blue-grey darken-1"> -->
      <!-- <m-title class="mt-10" icon="mdi-devices"> 장치 제어</m-title>
      <hr class="my-3">
      <v-row>
        <v-col cols="6" sm="4" v-for="(led, ix) in leds" :key="ix">
          <led :led="led" :topic="topic"></led>
        </v-col>
      </v-row> -->
    </div>
  </div>
</template>

<script>
export default {
  name: 'Sensor',
  data() {
    return {
      sensors: {
        // [place]: {
        //   [section]: {
        //     [device]: value,
        //   }
        // }
        //
        // 예시
        // farm: {
        //   section1: {
        //     temp: 1,
        //     humi: 2,
        //     illu: 3
        //   }
        // }
      },
      topic: 'iot/hong/control',
      leds: [
        { place: 'livingroom', placeTitle: '거실', color: 'red', state: false },
        { place: 'kitchen', placeTitle: '부엌', color: 'green', state: true },
        { place: 'bedroom', placeTitle: '침실', color: 'blue', state: false },
      ]
    };
  },
  mqtt: {
    'iot/sensor/#': function(value, topic) {
      const [,,place, section, device] = topic.split('/');

      const temp_section = this.sensors[place] ? {...this.sensors[place][section]} : null

      this.$set(this.sensors, place, {
        ...this.sensors[place],
        [section]: {
          ...temp_section,
          [device]: value
        }
      });
    }
  },
  mounted() {
    this.$mqtt.subscribe('iot/sensor/#');
  },
  unmounted() {
    this.$mqtt.unsubscribe('iot/sensor/#');
  },
}
</script>

<style>
.border {
  border: 1px solid gray;
  border-radius: 5px;
}
</style>
