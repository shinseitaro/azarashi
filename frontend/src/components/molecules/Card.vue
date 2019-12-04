<template>
  <v-card class="mx-auto" max-width="400">
    <v-img
      class="white--text align-end"
      height="200px"
      src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
    >
      <v-card-title>{{ dam.name }}</v-card-title>
    </v-img>

    <v-card-subtitle class="pb-0">{{ dam.river_name }}</v-card-subtitle>

    <v-card-text class="text--primary">
      <div>{{ dam.address }}</div>

      <div>{{ dam.year_of_completion }}</div>
    </v-card-text>

    <v-card-actions>
      <v-spacer></v-spacer>

      <v-btn icon @click="moveMarker(dam.coordinates)">
        <v-icon>mdi-map-marker</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-share-variant</v-icon>
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: ['dam'],
  methods: {
    moveMarker: function(coordinates) {
      this.$store.dispatch('map/startMove', coordinates);
    },
  },
};
</script>
