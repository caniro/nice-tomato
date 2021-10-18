<template>
  <v-app>
    <v-app-bar app color="red accent-1" dark>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>멋쟁이 토마토</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon @click="$router.push({ name: 'Home' }).catch(() => {})">
        <v-icon>mdi-home</v-icon>
      </v-btn>
      <v-btn icon v-if="isLogin" @click="logout">
        <v-icon>mdi-logout</v-icon>
      </v-btn>
      <v-btn icon v-else :to="{ name: 'Login' }">
        <v-icon>mdi-login</v-icon>
      </v-btn>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" temporary app>
      <v-list-item two-line>
        <v-list-item-avatar v-if="isLogin">
          <v-img src="https://randomuser.me/api/portraits/men/85.jpg"></v-img>
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title class="text-h6">
            {{ isLogin ? user.username : '스마트 팜' }}
          </v-list-item-title>
          <v-list-item-subtitle>
            {{ isLogin ? user.email : '' }}
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list dense nav v-if="isLogin">
        <v-list-item v-for="page in pages" :key="page.name"
             :to="{ name: page.name }" exact>

          <v-list-item-icon>
            <v-icon>{{ page.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ page.title }}</v-list-item-title>
          </v-list-item-content>

        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <v-slide-x-transition mode="out-in">
        <router-view />
      </v-slide-x-transition>
    </v-main>
  </v-app>
</template>

<script>
import { mapState, mapGetters, mapMutations, mapActions } from 'vuex';

export default {
  name: 'App',

  data: () => ({
    drawer: false,
    pages: [
      { title: 'Home', name: 'Home', icon: 'mdi-home' },
      { title: 'CCTV', name: 'Cctv', icon: 'mdi-video' },
      { title: '센서 통계', name: 'Sensor', icon: 'mdi-access-point-network' },
    ],
  }),
  computed: {
    ...mapState(['user']),
    /*
     * 아래와 같이 전개된다.
     * 즉 this.$store.state.user 대신 this.user로 접근 가능
     * computed: {
     *   user () {
     *     return this.$store.state.user;
     *   }
     * }
     */
    ...mapGetters(['isLogin']),
  },
  methods: {
    // this.$store.commit('logout') -> this.logout() 단축
    ...mapMutations(['logout', 'restore']),
    // this.$store.dispatch('verify', token) -> this.verify(token) 단축
    ...mapActions(['verify']),
  },

  async mounted() {
    let user = localStorage.getItem('user');

    if (user) {
      // 객체 -> 문자열 : stringify / 문자열 -> 객체 : parse
      user = JSON.parse(user);
      try {
        await this.verify(user.jwt);
        this.restore(user);
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>
