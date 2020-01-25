<template>
  <div id="map-wrap">
    <mapbox-map
      :access-token="accessToken"
      :map-style="mapStyle"
      :center="damCoord"
      :zoom="zoom"
      :scrollZoom="scrollZoom"
      @mb-created="mapboxInstance => (map = mapboxInstance)"
    >
      <mapbox-navigation-control />
      <mapbox-source id="dam" :options="damSource" />
      <mapbox-layer :id="damLayer.id" :options="damLayer" />
    </mapbox-map>
  </div>
</template>

<script>
import 'mapbox-gl/dist/mapbox-gl.css';
import {
  MapboxMap,
  // MapboxMarker,
  MapboxSource,
  MapboxLayer,
  MapboxNavigationControl,
} from '@studiometa/vue-mapbox-gl';
import { mapState } from 'vuex';

export default {
  components: {
    MapboxMap,
    // MapboxMarker,
    MapboxSource,
    MapboxLayer,
    MapboxNavigationControl,
  },
  data() {
    return {
      map: null,
      accessToken: process.env.VUE_APP_MAPBOX_KEY,
      mapStyle: 'mapbox://styles/mapbox/light-v10',
      zoom: 10,
      scrollZoom: false,
      damLayer: {
        id: 'damLayer',
        type: 'circle',
        source: 'dam',
        paint: {
          'circle-radius': 10,
          'circle-color': '#3794b3',
        },
      },
    };
  },
  computed: {
    ...mapState({
      damCoord: state => state.dam.damCoord,
    }),
    damSource: function() {
      return {
        type: 'geojson',
        cluster: false,
        data: this.$store.state.dam.damGeoData,
      };
    },
  },
};
</script>

<style lang="scss">
#map-wrap {
  position: relative;
  height: calc(100vh - 56px);
  overflow: hidden;
}

.mapboxgl-map {
  position: absolute;
  height: 100%;
  top: 0;
  left: 0;
  width: 100%;
}
</style>
