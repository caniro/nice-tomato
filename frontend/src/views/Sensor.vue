<template>
  <div class="pa-3">
    <div class="my-3">
      <div v-if="Object.keys(sensors).length === 0">데이터 수신 대기 중...</div>
      <sensor-chart></sensor-chart>
      <div v-for="(sections, place) in sensors" :key="place" class="pa-1 pb-3">
        <m-title icon="fas fa-seedling"> {{ place }}</m-title>
        <hr color="lightgray">
        <div v-for="(devices, section) in sections" :key="section"
            class="border pa-1 pb-3 text-center" @click="onClickSection(place, section)">
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
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Sensor',
  data() {
    return {
      sensors: {
        /*
          객체 구조
          [place]: {
            [section]: {
              [device]: value,
            }
          }
          
          예시
          farm: {
            section1: {
              temp: 1,
              humi: 2,
              illu: 3
            }
          }
        */
      },
      chart_data: {
        
      },
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
  methods: {
    onClickSection(place, section) {
      axios.get(`/api/sensor?place=${place}&section=${section}`).then(res => {
          console.log(res);
      });
    }
  },
}
</script>

<style>
.border {
  border: 1px solid gray;
  border-radius: 5px;
}
</style>
