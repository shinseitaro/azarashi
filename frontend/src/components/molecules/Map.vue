<template>
  <div>
    <div id="map-wrap">
      <mapbox-map
        :access-token="accessToken"
        :map-style="mapStyle"
        :center="center"
        :zoom="zoom"
        :bounds="getBounds"
        :fitBoundsOptions="fitBoundsOptions"
      >
        <mapbox-cluster
          v-if="!isDisplayMarker"
          :data="geoJsonSource"
          :clustersPaint="clustersPaint"
        />
        <mapbox-marker v-if="isDisplayMarker" :lng-lat="markerPosition" />
      </mapbox-map>
    </div>
    <div>{{ getBounds }}</div>
  </div>
</template>

<script>
import 'mapbox-gl/dist/mapbox-gl.css';
import {
  MapboxMap,
  MapboxCluster,
  MapboxMarker,
} from '@studiometa/vue-mapbox-gl';
import axios from 'axios';
import { mapState, mapGetters } from 'vuex';

export default {
  components: {
    MapboxMap,
    MapboxCluster,
    MapboxMarker,
  },
  data() {
    return {
      accessToken: process.env.VUE_APP_MAPBOX_KEY,
      zoom: 6,
      mapStyle: 'mapbox://styles/mapbox/streets-v10',
      fitBoundsOptions: {
        linear: true,
        maxZoom: 8,
      },
      geoJsonSource: {},
      clustersPaint: {
        'circle-color': [
          'step',
          ['get', 'point_count'],
          '#51bbd6',
          100,
          '#f1ae4e',
          750,
          '#f24078',
        ],
        'circle-radius': ['step', ['get', 'point_count'], 20, 100, 30, 750, 40],
      },
    };
  },
  mounted() {
    axios.get('/geojson/dam.geojson').then(response => {
      this.geoJsonSource = response.data;
    });
  },
  computed: {
    ...mapState({
      center: state => state.map.center,
      isDisplayMarker: state => state.map.isDisplayMarker,
      markerPosition: state => state.map.markerPosition,
    }),
    ...mapGetters('map', ['getBounds']),
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
