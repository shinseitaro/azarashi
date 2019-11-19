<template>
  <v-container class="grey lighten-5">
    <v-row>
      <v-col v-for="n in 8" :key="n" cols="12" md="3">
        <Card />
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue';
import Card from '../molecules/Card.vue';

export default Vue.extend({
  name: 'Cards',

  components: {
    Card,
  },

  data: () => ({
    //
  }),
});
</script>
