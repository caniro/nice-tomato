<template>
  <div class="pa-3">
    <!-- <div>
      <span>현재시간
        <v-icon>mdi-clock</v-icon>
        {{ new Date()|moment("YYYY-MM-DD hh:mm:ss") }}
      </span>
    </div>
  
    <div>
      <weather />
    </div> -->
    <v-img src="cover.png"></v-img>
    <div v-if="!isLogin" class="mt-5">
      <v-btn block color="primary" :to="{ name: 'Login' }">로그인</v-btn>
    </div>
    <div v-if="isLogin" class="mt-5">
      <v-btn block :to="{ name: 'Cctv' }">CCTV 현황</v-btn>
      <v-btn block :to="{ name: 'Sensor' }" class="mt-5">센서 통계</v-btn>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'Home',
  computed: {
    ...mapGetters(['isLogin']),
  },
}
</script>
