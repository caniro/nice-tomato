<template>
  <div class="pa-3">
    <v-form @submit.prevent="login({ username, password })">
      <v-row class="login">
        <v-col cols="8" class="mx-auto">
          <!-- label이 placeholder 역할을 하다가 입력할 때 label 역할함 -->
          <v-text-field v-model="username" label="username"
              prepend-icon="mdi-account" required></v-text-field>
        </v-col>
        <v-col cols="8" class="mx-auto">
          <v-text-field type="password" v-model="password" label="password"
              prepend-icon="mdi-account-lock" required></v-text-field>
        </v-col>
        <v-col cols="8" class="mx-auto red--text" v-if="error">
          <v-icon color="red">mdi-information</v-icon> {{ error.message }}
        </v-col>
        <v-col cols="8" class="mx-auto">
          <v-btn type="submit" color="primary" block :disabled="!isValid">
            <v-icon class="mr-3">mdi-login</v-icon> 로그인
          </v-btn>
        </v-col>
        <v-col cols="8" class="mx-auto">
          <v-btn color="primary" block>
            <v-icon class="mr-3">mdi-account-plus</v-icon> 회원가입
          </v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
import { mapState, mapMutations, mapActions } from 'vuex';

export default {
  name: 'Login',

  data() {
    return {
      username: undefined,
      password: undefined,
    };
  },

  computed: {
    ...mapState(['error']),

    isValid() {
      return (!!this.username && !! this.password);
    }
  },

  methods: {
    ...mapMutations(['setError']),
    ...mapActions(['login']),
  },

  mounted() {
    this.setError()
  },

  unmounted() {
    this.setError()
  },
}
</script>

<style>

</style>
