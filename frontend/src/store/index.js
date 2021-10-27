import Vue from 'vue'
import Vuex from 'vuex'
import axios from '@/util/api';
import jwt_decode from 'jwt-decode';
import router from '../router';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: undefined,
    error: undefined
  },
  getters: {    // 상태에 대한 getter. 컴포넌트의 computed에 해당
    isLogin(state) {
      return !!state.user // Boolean 야매 변환
    }
  },
  mutations: {  // 여기서만 state를 수정할 수 있음. 즉 setter 함수
                // 동기 함수만 가능
    restore(state, user) {
      state.user = user;
    },
    
    login(state, user) {
      state.user = user;
      // localStorage의 key:value에서 value는 문자열만 가능 -> 직렬화
      // API에서는 쿠키보다 localStorage가 편하다 (별도로 처리해야 하는 게 적어서)
      localStorage.setItem('user', JSON.stringify(user));
      router.push({ name: 'Home' }); // 상태를 유지하며 페이지 이동
    },

    logout(state) {
      state.user = {}
      localStorage.setItem('user', '');
      router.go({ name: 'Home' }); // 상태를 유지하지 않고 페이지 이동
    },

    setError(state, e) {
      state.error = e;
    }
  },
  actions: {    // 비동기 처리 후 mutation 함수를 호출해서 상태 변경
    async login(context, userInfo) {
      context.commit('setError'); // 2번째 인자가 없으므로 undefined 전달
      console.log('login', userInfo);
      try {
        const { data } = await axios.post('/api/login', userInfo);
        const token = data.token; // base64 포맷
        const user = jwt_decode(token);
        user.jwt = token;
        console.log(user);

        const now = parseInt(Date.now() / 1000);
        const remain = (user.exp - now) / 3600; // 남은 만기 hour
        console.log('현재 시간[ms] :', now, '만료 시간[ms] :', user.exp,
            '남은 시간[hour] :', remain);
        context.commit('login', user);
      } catch(e) {
        console.log('로그인 실패 :', e);
        context.commit('setError', 
                  { message: '사용자 ID 또는 비밀번호가 맞지 않습니다.' });
      }
    },

    async verify(context, token) {
      const { data } = await axios.post('/api/login/verify', { token });
      return data.token;
    }
  },
  modules: {
  }
})
