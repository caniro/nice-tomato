<template>
  <div class="my-3">
    <div class="mb-4">방향 제어</div>

    <div>
      <v-btn icon @click="$emit('direction', 'tl')">
        <v-icon>mdi-arrow-top-left</v-icon></v-btn>
      <v-btn icon @click="$emit('direction', 'u')">
        <v-icon>mdi-arrow-up</v-icon></v-btn>
      <v-btn icon @click="$emit('direction', 'tr')">
        <v-icon>mdi-arrow-top-right</v-icon></v-btn>
    </div>
    <div>
      <v-btn icon @click="$emit('direction', 'l')">
        <v-icon>mdi-arrow-left</v-icon></v-btn>
      <v-btn icon @click="$emit('direction', 's')">
        <v-icon>mdi-stop</v-icon></v-btn>
      <v-btn icon @click="$emit('direction', 'r')">
        <v-icon>mdi-arrow-right</v-icon></v-btn>
    </div>
    <div>
      <v-btn icon @click="$emit('direction', 'bl')">
        <v-icon>mdi-arrow-bottom-left</v-icon></v-btn>
      <v-btn icon @click="$emit('direction', 'd')">
        <v-icon>mdi-arrow-down</v-icon></v-btn>
      <v-btn icon @click="$emit('direction', 'br')">
        <v-icon>mdi-arrow-bottom-right</v-icon></v-btn>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DirectionPanel',
}
</script>

<style>

</style>
