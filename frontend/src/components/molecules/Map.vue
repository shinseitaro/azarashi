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
        v-for="(marker, index) in mapData.marker"
        :key="index"
        :coordinates.sync="mapData.marker"
        color="green"
      >
        <v-icon slot="marker">mdi-map-marker</v-icon>
      </MglMarker>
      <MglGeojsonLayer
        type="fill"
        :sourceId="sourceId"
        :layerId="layerId"
        :source="mapData.geojson"
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
      mapData: {},
      // geoJsonSource: mapData.geojson,
      layerId: 'firstLayer',
      sourceId: 'firstSource',
      // markerCoordinates: mapData.marker,
    };
  },
  mounted() {
    axios.get('/geojson/dam.geojson').then(
      (response: AxiosResponse) =>
        (this.mapData = {
          geojson: response.data,
          marker: response.data.features.map((value: any) => [
            value.geometory.coordinates,
          ]),
        })
    );
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
