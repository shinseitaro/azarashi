<template>
  <v-app>
    <common-header />
    <v-content class="grey lighten-5">
      <slot></slot>
    </v-content>
  </v-app>
</template>

<script>
import CommonHeader from './CommonHeader';

export default {
  components: {
    CommonHeader,
  },
};
</script>
