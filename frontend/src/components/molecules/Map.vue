<template>
  <div id="map-wrap">
    <MglMap
      :accessToken="accessToken"
      :mapStyle="mapStyle"
      :zoom.sync="zoom"
      :center="center"
    >
      <MglNavigationControl />
      <MglMarker :coordinates.sync="markerCoordinates" color="green" />
      <MglGeojsonLayer
        type="fill"
        :sourceId="sourceId"
        :layerId="layerId"
        :source="geojson"
      />
    </MglMap>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import 'mapbox-gl/dist/mapbox-gl.css';
import * as vueMapbox from 'vue-mapbox';

export default Vue.extend({
  components: {
    MglMap: vueMapbox.MglMap,
    MglNavigationControl: vueMapbox.MglNavigationControl,
    MglMarker: vueMapbox.MglMarker,
    MglGeojsonLayer: vueMapbox.MglGeojsonLayer,
  },
  data() {
    return {
      accessToken: process.env.VUE_APP_MAPBOX_KEY,
      zoom: 17,
      mapStyle: 'mapbox://styles/mapbox/streets-v10',
      center: { lon: 139.7009177, lat: 35.6580971 },
      geojson: '../../assets/geojson/dam.geojson',
      layerId: 'firstLayer',
      sourceId: 'firstSource',
      markerCoordinates: '[50, 50]',
    };
  },
});
</script>

<style lang="scss">
#map-wrap {
  position: relative;
  height: 80vh;
  overflow: hidden;
}

.mgl-map-wrapper {
  position: absolute;
  height: 100%;
  top: 0;
  left: 0;
  width: 100%;
}

.mapboxgl-canvas {
  outline: transparent;
  left: 0;
}

.mapboxgl-ctrl-attrib-inner {
  display: none;
}
</style>
