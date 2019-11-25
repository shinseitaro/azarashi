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
import axios from 'axios';
import Card from '../molecules/Card.vue';

export default {
  name: 'Cards',
  components: {
    Card,
  },
  data() {
    return {
      markers: [],
    };
  },
  mounted() {
    axios.get('/geojson/dam.geojson').then(response => {
      response.data.features.map(value => {
        this.markers.push(value.geometry.coordinates);
      });
    });
  },
};
</script>
