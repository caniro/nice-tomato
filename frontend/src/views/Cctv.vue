<template>
  <div class="pa-3">
    <m-title icon="fas fa-video"> CCTV 현황</m-title>
    <div class="cctv">
      <remote-camera :url="url"
        max-width="50%"></remote-camera>
      <remote-camera :url="url"
        max-width="50%"></remote-camera>
      <remote-camera :url="url"
        max-width="50%"></remote-camera>
      <remote-camera :url="url"
        max-width="50%"></remote-camera>
      <remote-camera :url="url"
        max-width="50%"></remote-camera>
      <remote-camera :url="url"
        max-width="50%"></remote-camera>
      <remote-camera :url="url"
        max-width="50%"></remote-camera>
      <remote-camera :url="url"
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
      url: 'https://picsum.photos/640/480'
    }
  }
}
</script>

<style scoped>
.cctv {
  line-height: 0px;
}
</style>
