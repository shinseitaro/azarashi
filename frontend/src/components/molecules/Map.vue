<template>
  <div id="map-wrap">
    <MglMap
      :accessToken="accessToken"
      :mapStyle="mapStyle"
      :zoom.sync="zoom"
      :center="center"
    >
      <MglNavigationControl />
      <MglMarker
        v-for="(marker, index) in markers"
        :key="index"
        :coordinates="marker"
      >
        <v-icon slot="marker" color="blue">mdi-map-marker</v-icon>
      </MglMarker>
      <MglGeojsonLayer
        type="fill"
        :sourceId="sourceId"
        :layerId="layerId"
        :source="geoJsonSource"
      />
    </MglMap>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import 'mapbox-gl/dist/mapbox-gl.css';
import * as vueMapbox from 'vue-mapbox';
import axios, { AxiosResponse } from 'axios';

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
      zoom: 6,
      mapStyle: 'mapbox://styles/mapbox/streets-v10',
      center: { lon: 139.7009177, lat: 35.6580971 },
      geoJsonSource: {},
      layerId: 'firstLayer',
      sourceId: 'firstSource',
      markers: [] as any,
    };
  },
  mounted() {
    axios.get('/geojson/dam.geojson').then((response: AxiosResponse) => {
      this.geoJsonSource = response.data;
      response.data.features.map((value: any) => {
        this.markers.push(value.geometry.coordinates);
      });
    });
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
