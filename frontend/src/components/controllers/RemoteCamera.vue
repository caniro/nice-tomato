<template>
  <span>
      <v-img :src="url" :max-width="maxWidth" contain></v-img>
  </span>
</template>

<script scoped>
export default {
  name: 'RemoteCamera',
  props: ['url', 'maxWidth'],
  data() {
    return {
    };
  },
  mounted() {
  },
}
</script>

<style scoped>
.v-image {
  display: inline-block;
}
</style>
