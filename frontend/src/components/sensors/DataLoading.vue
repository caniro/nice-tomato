<template>
  <div v-if="Object.keys(obj).length === 0">
    <v-text-field
      color="success"
      loading
      disabled
    ></v-text-field>
    <div class="text-center grey--text">데이터 수신 중...</div>
  </div>
</template>

<script>
export default {
  name: 'DataLoading',
  props: ['obj'],
}
</script>

<style>

</style>
