<template>
  <div id="map-wrap">
    <mapbox-map
      :access-token="accessToken"
      :map-style="mapStyle"
      :center="getBounds[1]"
      :zoom="zoom"
      @mb-created="mapboxInstance => (map = mapboxInstance)"
      @mb-move="move"
      @mb-moveend="endMove"
      @mb-zoom="zoomMap"
    >
      <mapbox-navigation-control />
      <mapbox-cluster
        v-if="!isDisplayZoomLayer"
        :data="damGeoData"
        :clustersPaint="clustersPaint"
        :unclusteredPointPaint="unclusteredPointPaint"
      />
      <mapbox-marker
        v-if="isDisplayZoomLayer"
        :lng-lat="coordinates"
        :offset="popupOffsets"
      >
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
import { mapState, mapGetters } from 'vuex';

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
      accessToken: process.env.VUE_APP_MAPBOX_KEY,
      mapStyle: 'mapbox://styles/mapbox/light-v10',
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
      map: null,
      isDisplayZoomLayer: false,
      coordinates: [0, 0],
      name: '',
      popupOffsets: [0, 0],
    };
  },
  computed: {
    ...mapState({
      damGeoData: state => state.map.damGeoData,
      isDisplayMarker: state => state.map.isDisplayMarker,
      markerPosition: state => state.map.markerPosition,
    }),
    ...mapGetters('map', ['getBounds']),
    zoomUpSource: function() {
      return {
        type: 'geojson',
        cluster: false,
        data: this.$store.state.map.damGeoData,
      };
    },
    zoomUpLayer: function() {
      return {
        id: 'zoomUpLayer',
        type: 'circle',
        source: 'zoomUp',
        paint: {
          'circle-radius': [
            'interpolate',
            ['linear'],
            ['zoom'],
            10,
            ['/', ['number', ['get', 'bank_volume']], 700],
            13,
            ['/', ['number', ['get', 'bank_volume']], 400],
          ],
          'circle-color': '#3794b3',
        },
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
      this.map.getCanvas().style.cursor = 'pointer';
    },
    clearCursor: function() {
      this.map.getCanvas().style.cursor = '';
    },
    move: function() {
      if (this.$store.state.map.isMoving) {
        this.map.fitBounds(this.$store.state.map.bounds, {
          linear: true,
          easing: function(t) {
            return t;
          },
          padding: 100,
          maxZoom: 6,
        });
      }
    },
    endMove: function() {
      this.$store.dispatch('map/stopMove');
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
  transform: translate(-50%, -25px);
}
</style>
