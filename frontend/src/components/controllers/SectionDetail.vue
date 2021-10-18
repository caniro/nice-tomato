<template>
  <div class="pa-3">
      <remote-camera url="https://picsum.photos/640/480?random=1"
        max-width="100%"></remote-camera>
      <div v-if="Object.keys(sensors).length === 0">
        <v-text-field
          color="success"
          loading
          disabled
        ></v-text-field>
      </div>
      <div v-for="(sections, place) in sensors" :key="place" class="pa-1 pb-3">
        <m-title icon="fas fa-seedling"> {{ place }}</m-title>
        <hr color="lightgray">
        <div v-for="(devices, section) in sections" :key="section"
            class="border pa-1 pb-3 text-center">
          <div>
            <h3 class="indigo--text mb-3">{{ section }}</h3>
            <v-row justify="space-between">
              <div class="px-3 py-1" cols="9" sm="3">
                <v-col v-for="(value, device) in devices" :key="device">
                  <temperature v-if="device==='temp'" :value="value"></temperature>
                  <humidity v-if="device==='humi'" :value="value"></humidity>
                  <illumination v-if="device==='illu'" :value="value"></illumination>
                </v-col>
              </div>
            </v-row>
          </div>
        </div>
      </div>
      <div>
        <m-title icon="fas fa-cog"> 수동 제어</m-title>
        <hr color="lightgray">
        <v-row>
          <v-col cols="9">
            <v-text-field
              label="온도 설정 값"
              hide-details="auto"
              outlined
              class="pa-1"
              prepend-inner-icon="mdi-thermometer"
              :rules="[rules.number, rules.temp_limit]"
              v-model="desired_temperature"
            ></v-text-field>
            <v-text-field
              label="습도 설정 값"
              hide-details="auto"
              outlined
              class="pa-1"
              prepend-inner-icon="mdi-water-percent"
              :rules="[rules.number, rules.humi_limit]"
              v-model="desired_humidity"
            ></v-text-field>
            <v-text-field
              label="조도 설정 값"
              hide-details="auto"
              outlined
              class="pa-1"
              prepend-inner-icon="mdi-white-balance-sunny"
              :rules="[rules.number, rules.illu_limit]"
              v-model="desired_illuminance"
            ></v-text-field>
          </v-col>
          <v-btn elevation="2" cols="3" class="align-self-center border"
            @click="onClickSet">설정</v-btn>
        </v-row>
      </div>
  </div>
</template>

<script>

export default {
  name: 'SectionDetail',
  props: ['target_place', 'target_section'],
  data() {
    return {
      sensors: {},
      desired_temperature: '',
      desired_humidity: '',
      desired_illuminance: '',
      rules: {
        number: value => !isNaN(value) || 'Input must be a number',
        temp_limit: value => (value >= -50 && value <= 100) || 'limit',
        humi_limit: value => (value >= 0 && value <= 100) || 'limit',
        illu_limit: value => (value >= 0 && value <= 100) || 'limit',
      },
    }
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
    const mqtt_topic = 'iot/sensor/' + this.target_place + '/' + this.target_section + '/#';
    this.$mqtt.subscribe(mqtt_topic);
    // TODO : 마지막 측정값 불러와서 sensors에 저장
    console.log(mqtt_topic);
  },
  unmounted() {
    const mqtt_topic = 'iot/sensor/' + this.target_place + '/' + this.target_section + '/#';
    this.$mqtt.unsubscribe(mqtt_topic);
  },
  methods: {
    onClickSet() {
      if (isNaN(this.desired_temperature) || isNaN(this.desired_humidity)
            || isNaN(this.desired_illuminance))
        return ;
      console.log(this.desired_temperature, this.desired_humidity, this.desired_illuminance);
      const mqtt_control_topic = `iot/control/${this.target_place}/${this.target_section}/`;
      this.$mqtt.publish(mqtt_control_topic + `temp`, this.desired_temperature);
      this.$mqtt.publish(mqtt_control_topic + `humi`, this.desired_humidity);
      this.$mqtt.publish(mqtt_control_topic + `illu`, this.desired_illuminance);
    },
  },
}
</script>

<style>

</style>
