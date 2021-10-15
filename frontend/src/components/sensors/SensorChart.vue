<script>
import { Line } from "vue-chartjs";
// import { Line, mixins } from "vue-chartjs";
// const { reactiveProp } = mixins;

export default {
  extends: Line,
  // mixins: [reactiveProp],
  props: ['data', 'options'],
  computed: {
    chartData: function() {
      return this.data;
    },
  },
  mounted() {
    this.renderLineChart();
  },
  methods: {
    renderLineChart: function() {
      this.renderChart(this.chartData, this.options);
    },
  },
  watch: {
    data: function() {
      this.renderLineChart();
    }
  },
};
// 차트 동적 업데이트 참고할 것 : https://stackoverflow.com/questions/43728332/vue-chart-js-chart-is-not-updating-when-data-is-changing
</script>

<style>

</style>
