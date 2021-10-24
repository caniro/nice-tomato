<template>
  <div class="pa-3">
    <div class="my-3">
      <div v-if="!isSelected" class="text-center"><span class="indigo--text font-weight-bold">구역</span>을 선택하세요.</div>
      <sensor-chart :chart-data="chartdata" :options="options" v-if="isSelected"></sensor-chart>
      <data-loading :obj="sensors"></data-loading>
      <div v-for="(sections, place) in sensors" :key="place" class="pa-1 pb-3">
        <m-title icon="fas fa-seedling"> {{ place }}</m-title>
        <hr color="lightgray">
        <div v-for="(devices, section) in sections" :key="section"
            class="border pa-1 pb-3 text-center">
          <div @click="onClickSection(place, section)">
            <h3 class="indigo--text mb-3">{{ section }}</h3>
            <v-row justify="space-between">
              <div class="px-3 py-1" cols="9" sm="3">
                <v-col v-for="(value, device) in devices" :key="device">
                  <temperature v-if="device==='temp'" :value="value"></temperature>
                  <humidity v-if="device==='humi'" :value="value"></humidity>
                  <illumination v-if="device==='illu'" :value="value"></illumination>
                </v-col>
              </div>
              <v-btn elevation="2" color="primary" class="mr-3 align-self-center" cols="3" sm="3"
                @click.stop="onClickDetail(place, section)">
                상세보기
              </v-btn>
            </v-row>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

const mqtt_topic = 'iot/sensor/#'

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
      chartdata: {},
      options: {
        responsive: true,
        maintainAspectRatio: false,
        title: {
          display: true,
          text: "온•습•조도 통계"
        }
      }
    };
  },
  computed: {
    isSelected: function() {
      if (!this.chartdata.labels)
        return false;
      else if (this.chartdata.labels.length)
        return true;
      else
        return false;
    },
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
    this.$mqtt.subscribe(mqtt_topic);
    console.log('mqtt subscribe :', mqtt_topic);
    this.resetChartdata();
    this.getLastData();
  },
  destroyed() {
    this.$mqtt.unsubscribe(mqtt_topic);
    console.log('mqtt unsubscribe :', mqtt_topic);
  },
  methods: {
    getLastData() { // 마지막에 측정된 데이터를 sensors에 저장
      axios.get('/api/last')
          .then(res => {
            let new_sensors = {};
            for (let sensor of res.data.results) {
              const place = sensor.place;
              const section = sensor.section;
              const type = sensor.sensor;
              const value = sensor.value;
              if (!new_sensors[place])
                new_sensors[place] = {};
              if (!new_sensors[place][section])
                new_sensors[place][section] = {};
              if (new_sensors[place][section][type]) // 한바퀴 돌면 종료
                break ;
              new_sensors[place][section][type] = value;
            }

            let ordered = {};
            // 사전 순으로 객체 정렬
            Object.keys(new_sensors).sort().forEach(function(place) {
              ordered[place] = {};
              Object.keys(new_sensors[place]).sort().forEach(function(section) {
                ordered[place][section] = new_sensors[place][section];
              });
            });
            this.sensors = ordered;
          });
    },
    resetChartdata() {
      this.chartdata = {
        labels: [],
        datasets: [
          {
            label: "온도",
            borderColor: "#FC2525",
            pointBackgroundColor: "white",
            borderWidth: 1,
            pointBorderColor: "red",
            backgroundColor: "transparent",
            data: []
          },
          {
            label: "습도",
            borderColor: "#05CBE1",
            pointBackgroundColor: "white",
            pointBorderColor: "skyblue",
            borderWidth: 1,
            backgroundColor: "transparent",
            data: []
          },
          {
            label: "조도",
            borderColor: "#AAAA11",
            pointBackgroundColor: "white",
            pointBorderColor: "#AAAA11",
            borderWidth: 1,
            backgroundColor: "transparent",
            data: []
          },
        ]
      };
    },
    onClickSection(place, section) {
      axios.get(`/api/sensor?place=${place}&section=${section}`)
          .then(res => {
              let temp_data = [];
              let humi_data = [];
              let illu_data = [];
              let label = [];
              for (let data of res.data) {
                if (data.sensor === 'temp') {
                  const regdate_h = data.regdate_h.substring(11, 13);
                  label.push(regdate_h); // 차트 x축(시간축) 추가
                  temp_data.push(data.avg);
                }
                else if (data['sensor'] === 'humi') {
                  humi_data.push(data.avg);
                }
                else if (data['sensor'] === 'illu') {
                  illu_data.push(data.avg);
                }
              }
              this.chartdata = {
                labels: label,
                datasets: [
                  {
                    label: "온도",
                    borderColor: "#FC2525",
                    pointBackgroundColor: "white",
                    borderWidth: 1,
                    pointBorderColor: "red",
                    backgroundColor: "transparent",
                    data: temp_data
                  },
                  {
                    label: "습도",
                    borderColor: "#05CBE1",
                    pointBackgroundColor: "white",
                    pointBorderColor: "skyblue",
                    borderWidth: 1,
                    backgroundColor: "transparent",
                    data: humi_data
                  },
                  {
                    label: "조도",
                    borderColor: "#AAAA11",
                    pointBackgroundColor: "white",
                    pointBorderColor: "#AAAA11",
                    borderWidth: 1,
                    backgroundColor: "transparent",
                    data: illu_data
                  },
                ]
              };
          });
      this.$vuetify.goTo('#app'); // 맨 위로
    },
    onClickDetail(place, section) {
      console.log(place, section);
      this.$mqtt.unsubscribe('iot/sensor/#');
      this.$router.push(`detail?place=${place}&section=${section}`);
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
