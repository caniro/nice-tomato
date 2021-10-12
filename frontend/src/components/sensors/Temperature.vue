<template>
  <div>
    <v-icon class="ml-1 mr-5" :color="color">{{ icon }}</v-icon>
    <span class="font-weight-bold">온도 : </span>
    <span>{{ value }} °C</span>
  </div>
</template>

<script>
export default {
  name: 'Temperature',
  props: ['value'],
  data() {
    return {
      icons: [
        'fa-thermometer-empty',
        'fa-thermometer-quarter',
        'fa-thermometer-half',
        'fa-thermometer-three-quarters',
      ],
      colors: [ 'gray', 'yellow', 'orange', 'red'],
    }
  },
  computed: {
    color() {
      return this.colors[this.index];
    },
    icon() {
      return this.icons[this.index];
    },
    index() {
      if (this.value < 0) return 0;
      else if (this.value < 15) return 1;
      else if (this.value < 30) return 2;
      else return 3;
    }
  },
}
</script>

<style>

</style>
