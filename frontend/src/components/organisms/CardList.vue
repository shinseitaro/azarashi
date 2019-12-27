<template>
  <v-container class="grey lighten-5">
    <v-row>
      <v-col
        v-for="(marker, index) in markers.slice(0, 8)"
        :key="index"
        cols="12"
        md="3"
      >
        <Card :marker="marker" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapState } from 'vuex';
import Card from '../molecules/Card.vue';

export default {
  components: {
    Card,
  },
  computed: {
    ...mapState({
      markers: state => state.map.markers,
    }),
  },
};
</script>
