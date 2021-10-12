<template>
  <div>
    <v-icon class="mr-3" :color="color">mdi-brightness-7</v-icon>
    <span class="font-weight-bold">조도 : </span>
    <span>{{ value }} %</span>
  </div>
</template>

<script>
export default {
  name: 'Illumination',
  props: ['value'],
  data() {
    return {
      colors: [ 
        'grey darken-4',
        'grey darken-2',
        'yellow accent-4',
        'yellow accent-7',
        'yellow accent-1',
        'yellow accent-2',
        ],
    }
  },
  computed: {
    color() {
      return this.colors[this.index];
    },
    index() {
      return parseInt(this.value / 20);
    }
  },
}
</script>

<style>

</style>
