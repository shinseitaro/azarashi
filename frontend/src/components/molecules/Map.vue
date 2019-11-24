<template>
  <div id="map-wrap">
    <mapbox-map
      :access-token="accessToken"
      :map-style="mapStyle"
      :center="center"
      :zoom="zoom"
    >
      <mapbox-cluster :data="geoJsonSource" :clustersPaint="clustersPaint" />
    </mapbox-map>
  </div>
</template>

<script>
import 'mapbox-gl/dist/mapbox-gl.css';
import { MapboxMap, MapboxCluster } from '@studiometa/vue-mapbox-gl';
import axios from 'axios';

export default {
  components: {
    MapboxMap,
    MapboxCluster,
  },
  data() {
    return {
      accessToken: process.env.VUE_APP_MAPBOX_KEY,
      zoom: 6,
      mapStyle: 'mapbox://styles/mapbox/streets-v10',
      center: { lon: 139.7009177, lat: 35.6580971 },
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
