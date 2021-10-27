<template>
  <div class="small">
    <chart-test :chart-data="dataCollection"></chart-test>
    <v-btn @click="fillData()">Randomize</v-btn>
  </div>
</template>

<script>
import ChartTest from '@/components/ChartTest';

export default {
  components: {
    ChartTest,
  },
  data() {
    return {
      dataCollection: null,
    };
  },
  created() {
    this.fillData();
  },
  methods: {
    fillData() {
      this.dataCollection = {
        labels: [this.getRandomInt(), this.getRandomInt()],
        datasets: [
          {
            label: 'Main One',
            backgroundColor: '#f87979',
            data: [this.getRandomInt(), this.getRandomInt()],
          }, {
            label: 'Main One',
            backgroundColor: '#f87979',
            data: [this.getRandomInt(), this.getRandomInt()],
          },
        ],
      };
      console.log('ChartTestMain', this.dataCollection);
    },
    getRandomInt() {
      return Math.floor(Math.random() * (50 - 4)) + 5;
    },
  },
};
</script>

<style>
  .small {
    max-width: 600px;
    margin:  150px auto;
  }
</style>