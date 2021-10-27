<template>
  <div>
    <p><img :src="url_img" />{{ description }}</p>
    <span class="mx-1"><i class="fas fa-temperature-low"></i> : {{ weather_main.temp }} °C</span>
    <span class="mx-1"><i class="fas fa-tint"></i> : {{ weather_main.humidity }} %</span>
    <span class="mx-1"><i class="fas fa-wind"></i> : {{ wind.speed }} m/s</span>
    <span class="mx-1"><i class="fas fa-location-arrow"></i> : {{ wind.deg }} °</span>
  </div>
</template>

<script scoped>
import axios from 'axios';

/*
 * 프로젝트 root 디렉토리 (src 바깥 디렉토리)의 .env 파일에
 * VUE_APP_WEATHER_API_KEY=abc 이런식으로 저장
 */
const WEATHER_API_KEY = process.env.VUE_APP_WEATHER_API_KEY;

export default {
  name: 'Weather',
  data() {
    return {
      weather_main: {},
      url_img: '',
      description: '',
      wind: {},
    };
  },
  mounted() {
    this.setWeatherData();
  },
  methods: {
    saveWeatherData(data) {
      this.weather_main = data.main;
      this.url_img = `http://api.openweathermap.org/img/w/${data.weather[0].icon}.png`;
      this.description = data.weather[0].description;
      this.wind = data.wind;
    },
    async setWeatherData() {
      const url = 'http://api.openweathermap.org/data/2.5/weather';
      const city = 'Seoul';
      const lang = 'kr';
      const units = "metric";
      const params = { q: city, appid: WEATHER_API_KEY, lang, units };

      try {
        const res = await axios.get(url, { params });
        this.saveWeatherData(res.data);
      } catch(e) {
        console.log(e);
      }
    },
  }
}
</script>

<style>

</style>
