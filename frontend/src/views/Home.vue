<template>
  <div class="pa-3">
    <div>
      <span>현재시간
        <v-icon>mdi-clock</v-icon>
        {{ new Date()|moment("YYYY-MM-DD hh:mm:ss") }}
      </span>
    </div>
  
    <div>
      <weather />
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
}
</script>
