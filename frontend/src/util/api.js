import axios from 'axios';
import store from '@/store/index.js'; // vuex에서 jwt 사용

let instance = axios.create({}); // 매개변수 - timeout 등의 값 넣기 가능

function setInterceptors(instance) {
  instance.interceptors.request.use( // login API 요청 후
    function(config) { // config에는 http 구성
      if (store.state.user) {
        config.headers.Authorization = `jwt ${store.state.user.jwt}`
      }
      return config;
    },
    function(error) {
      return Promise.reject(error);
    }
  );

  instance.interceptors.response.use(
    function(response) {
      // jwt 기간 만료가 가까워지면 refresh하는거 여기서 처리
      return response;
    },
    function(error) {
      return Promise.reject(error);
    }
  );
}

setInterceptors(instance);

export default instance;
