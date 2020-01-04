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
      <mapbox-marker :lng-lat="damCoord" />
    </mapbox-map>
  </div>
</template>

<script>
import 'mapbox-gl/dist/mapbox-gl.css';
import {
  MapboxMap,
  MapboxMarker,
  MapboxNavigationControl,
} from '@studiometa/vue-mapbox-gl';
import { mapState } from 'vuex';

export default {
  components: {
    MapboxMap,
    MapboxMarker,
    MapboxNavigationControl,
  },
  data() {
    return {
      map: null,
      accessToken: process.env.VUE_APP_MAPBOX_KEY,
      mapStyle: 'mapbox://styles/mapbox/light-v10',
      zoom: 6,
      scrollZoom: false,
    };
  },
  computed: {
    ...mapState({
      damCoord: state => state.dam.damCoord,
    }),
  },
};
</script>

<style lang="scss">
#map-wrap {
  position: relative;
  height: 80vh;
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
