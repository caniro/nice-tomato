<script>
import { Line } from "vue-chartjs";

export default {
  extends: Line,
  mounted() {

    this.renderChart(
      {
        labels: [
          "",
        ],
        datasets: [
          {
            label: "온도",
            borderColor: "#FC2525",
            pointBackgroundColor: "white",
            borderWidth: 1,
            pointBorderColor: "red",
            backgroundColor: "transparent",
            data: [40, 39, 10, 40, 39, 80, 40, 30, 50, 90, 
                  40, 39, 10, 40, 39, 80, 40, 30, 50, 90, ]
          },
          {
            label: "습도",
            borderColor: "#05CBE1",
            pointBackgroundColor: "white",
            pointBorderColor: "skyblue",
            borderWidth: 1,
            backgroundColor: "transparent",
            data: [60, 55, 32, 10, 2, 12, 53]
          },
          {
            label: "조도",
            borderColor: "yellow",
            pointBackgroundColor: "white",
            pointBorderColor: "yellow",
            borderWidth: 1,
            backgroundColor: "transparent",
            data: [30, 25, 30, 20, 10, 15, 30]
          ,}
        ]
      },
      {
        responsive: true,
        maintainAspectRatio: false,
        title: {
          display: true,
          text: "온•습•조도 통계"
        }
      }
    );
  }
};
</script>

<style>

</style>