<template>
  <div class="pa-3">
    <m-title icon="fas fa-video"> CCTV 현황</m-title>
    <div class="cctv">
      <remote-camera :url="url1"
        max-width="50%"></remote-camera>
      <remote-camera :url="url2"
        max-width="50%"></remote-camera>
      <remote-camera :url="url3"
        max-width="50%"></remote-camera>
      <remote-camera :url="url4"
        max-width="50%"></remote-camera>
      <remote-camera :url="url5"
        max-width="50%"></remote-camera>
      <remote-camera :url="url6"
        max-width="50%"></remote-camera>
      <remote-camera :url="url7"
        max-width="50%"></remote-camera>
      <remote-camera :url="url8"
        max-width="50%"></remote-camera>
    </div>
  </div>
</template>

<script>
const RPI_CAMERA_IP_1 = process.env.VUE_APP_RPI_CAMERA_IP_1;
const RPI_CAMERA_IP_2 = process.env.VUE_APP_RPI_CAMERA_IP_2;

export default {
  name: 'Cctv',
  data() {
    return {
      url1: 'http://' + RPI_CAMERA_IP_1 + ':8000/mjpeg/stream/',
      url2: 'http://' + RPI_CAMERA_IP_2 + ':8000/mjpeg/stream/',
      url3: 'http://' + RPI_CAMERA_IP_1 + ':8000/mjpeg/stream/',
      url4: 'http://' + RPI_CAMERA_IP_2 + ':8000/mjpeg/stream/',
      url5: 'http://' + RPI_CAMERA_IP_1 + ':8000/mjpeg/stream/',
      url6: 'http://' + RPI_CAMERA_IP_2 + ':8000/mjpeg/stream/',
      url7: 'http://' + RPI_CAMERA_IP_1 + ':8000/mjpeg/stream/',
      url8: 'http://' + RPI_CAMERA_IP_2 + ':8000/mjpeg/stream/',

      // motion 사용 : 8081 포트
      // url1: 'http://192.168.219.101:8081',
      // url2: 'http://192.168.219.102:8081',
      // url3: 'http://192.168.219.101:8081',
      // url4: 'http://192.168.219.102:8081',
      // url5: 'http://192.168.219.101:8081',
      // url6: 'http://192.168.219.102:8081',
      // url7: 'http://192.168.219.101:8081',
      // url8: 'http://192.168.219.102:8081',
    }
  }
}
</script>

<style scoped>
.cctv {
  line-height: 0px;
}
</style>
