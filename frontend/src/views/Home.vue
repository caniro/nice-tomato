<template>
  <div class="pa-3">
    <v-img src="cover.png"></v-img>
    <div v-if="!isLogin" class="mt-5">
      <v-btn block color="primary" :to="{ name: 'Login' }">로그인</v-btn>
    </div>
    <div v-if="isLogin" class="mt-5">
      <v-btn v-for="page in pages" :key="page.name" :to="{ name: page.name }"
          block class="mb-5" color="success" outlined>
        <v-icon>{{ page.icon }}</v-icon> {{ page.title }}
      </v-btn>
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
  data: () => ({
    pages: [
      { title: 'CCTV', name: 'Cctv', icon: 'mdi-video' },
      { title: '센서 통계', name: 'Sensor', icon: 'mdi-access-point-network' },
    ]
  }),
}
</script>
