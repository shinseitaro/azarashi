<template>
  <v-container class="grey lighten-5">
    <p v-html="text" class="text"></p>
  </v-container>
</template>

<script>
export default {
  props: ['text'],
};
</script>

<style lang="scss"></style>
