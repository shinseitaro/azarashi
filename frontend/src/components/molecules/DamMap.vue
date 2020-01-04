<template>
  <div id="map-wrap">
    <mapbox-map
      :access-token="accessToken"
      :map-style="mapStyle"
      :center="center"
      :zoom="zoom"
      :scrollZoom="scrollZoom"
      @mb-created="mapboxInstance => (map = mapboxInstance)"
      @mb-zoom="zoomMap"
    >
      <mapbox-navigation-control />
      <mapbox-cluster
        v-if="!isDisplayZoomLayer"
        :data="damGeoData"
        :clustersPaint="clustersPaint"
        :unclusteredPointPaint="unclusteredPointPaint"
      />
      <mapbox-marker v-if="isDisplayPopup" :lng-lat="coordinates">
        <template>
          <div class="mapboxgl-popup">{{ name }}</div>
        </template>
      </mapbox-marker>
      <mapbox-source id="zoomUp" :options="zoomUpSource" />
      <mapbox-layer
        v-if="isDisplayZoomLayer"
        :id="zoomUpLayer.id"
        :options="zoomUpLayer"
        @mb-click="displayPopup"
        @mb-mouseenter="setCursor"
        @mb-mouseleave="clearCursor"
      />
    </mapbox-map>
  </div>
</template>

<script>
import 'mapbox-gl/dist/mapbox-gl.css';
import {
  MapboxMap,
  MapboxCluster,
  MapboxMarker,
  MapboxSource,
  MapboxLayer,
  MapboxNavigationControl,
} from '@studiometa/vue-mapbox-gl';
import { mapState } from 'vuex';

export default {
  components: {
    MapboxMap,
    MapboxCluster,
    MapboxMarker,
    MapboxSource,
    MapboxLayer,
    MapboxNavigationControl,
  },
  data() {
    return {
      map: null,
      accessToken: process.env.VUE_APP_MAPBOX_KEY,
      mapStyle: 'mapbox://styles/mapbox/light-v10',
      center: [139.7009177, 35.6580971],
      scrollZoom: false,
      zoom: 6,
      zoomThreshold: 7,
      clustersPaint: {
        'circle-color': [
          'step',
          ['get', 'point_count'],
          '#51bbd6',
          50,
          '#78d6bc',
          100,
          '#f1ae4e',
          300,
          '#f24078',
        ],
        'circle-radius': ['step', ['get', 'point_count'], 20, 100, 30, 750, 40],
      },
      unclusteredPointPaint: {
        'circle-color': '#51bbd6',
        'circle-radius': 4,
      },
      isDisplayZoomLayer: false,
      zoomUpLayer: {
        id: 'zoomUpLayer',
        type: 'circle',
        source: 'zoomUp',
        paint: {
          'circle-radius': [
            '+',
            ['ln', ['number', ['get', 'total_pondage']]],
            1,
          ],
          'circle-color': '#3794b3',
        },
      },
      coordinates: [null, null],
      name: '',
    };
  },
  computed: {
    ...mapState({
      damGeoData: state => state.map.damGeoData,
      isDisplayPopup: state => state.map.isDisplayPopup,
    }),
    zoomUpSource: function() {
      return {
        type: 'geojson',
        cluster: false,
        data: this.$store.state.map.damGeoData,
      };
    },
  },
  methods: {
    zoomMap: function() {
      this.isDisplayZoomLayer = this.map.getZoom() > this.zoomThreshold;
    },
    displayPopup: function(e) {
      this.coordinates = e.features[0].geometry.coordinates.slice();
      this.name = e.features[0].properties.name;
    },
    setCursor: function() {
      this.$store.dispatch('map/setPopup', true);
      this.map.getCanvas().style.cursor = 'pointer';
    },
    clearCursor: function() {
      this.$store.dispatch('map/setPopup', false);
      this.map.getCanvas().style.cursor = '';
      this.coordinates = [null, null];
      this.name = '';
    },
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

.mapboxgl-popup {
  background-color: #ffffff;
  white-space: nowrap;
  padding: 0.5em;
  transform: translate(-50%, -40px);
}
</style>
