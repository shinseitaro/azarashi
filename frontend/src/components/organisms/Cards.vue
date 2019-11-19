<template>
  <v-container class="grey lighten-5">
    <v-row v-for="n in 2" :key="n" :class="n === 1 ? 'mb-6' : ''">
      <v-col v-for="k in n + 1" :key="k">
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
