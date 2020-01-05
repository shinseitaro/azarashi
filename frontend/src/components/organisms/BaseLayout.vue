<template>
  <v-app>
    <common-header />
    <v-content class="grey lighten-5">
      <slot></slot>
    </v-content>
    <common-footer />
  </v-app>
</template>

<script>
import CommonHeader from './CommonHeader';
import CommonFooter from './CommonFooter';

export default {
  components: {
    CommonHeader,
    CommonFooter,
  },
};
</script>
