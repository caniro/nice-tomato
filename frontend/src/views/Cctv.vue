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
// const RPI_CAMERA_IP = process.env.VUE_APP_RPI_CAMERA_IP;

export default {
  name: 'Cctv',
  data() {
    return {
      // url: 'http://' + RPI_CAMERA_IP + ':8000/mjpeg/stream/'
      url1: 'https://picsum.photos/640/480?random=1',
      url2: 'https://picsum.photos/640/480?random=2',
      url3: 'https://picsum.photos/640/480?random=3',
      url4: 'https://picsum.photos/640/480?random=4',
      url5: 'https://picsum.photos/640/480?random=5',
      url6: 'https://picsum.photos/640/480?random=6',
      url7: 'https://picsum.photos/640/480?random=7',
      url8: 'https://picsum.photos/640/480?random=8',
    }
  }
}
</script>

<style scoped>
.cctv {
  line-height: 0px;
}
</style>
