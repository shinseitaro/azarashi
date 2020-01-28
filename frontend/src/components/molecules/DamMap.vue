<template>
  <div>
    <div id="map-wrap">
      <mapbox-map
        :access-token="accessToken"
        :map-style="mapStyle"
        :center="center"
        :zoom="zoom"
        :scrollZoom="scrollZoom"
        :touchZoomRotate="touchZoomRotate"
        @mb-created="mapboxInstance => (map = mapboxInstance)"
        @mb-zoom="zoomMap"
      >
        <mapbox-navigation-control />
        <mapbox-cluster
          v-if="!isDisplayZoomLayer && !isDisplayPlotLayer"
          :data="damGeoData"
          :clustersPaint="clustersPaint"
          :unclusteredPointPaint="unclusteredPointPaint"
        />
        <mapbox-marker v-if="isDisplayPopup" :lng-lat="coordinates">
          <template>
            <div class="mapboxgl-popup">
              {{ name }}<br />{{ yearOfCompletion }}
            </div>
          </template>
        </mapbox-marker>
        <mapbox-source id="plot" :options="plotSource" />
        <mapbox-layer
          v-if="isDisplayZoomLayer && !isDisplayPlotLayer"
          :id="zoomUpLayer.id"
          :options="zoomUpLayer"
          @mb-mouseover="displayPopup"
          @mb-mouseenter="setCursor"
          @mb-mouseleave="clearCursor"
        />
        <mapbox-layer
          :id="plotLayer.id"
          :options="plotLayer"
          @mb-mouseover="displayPopup"
          @mb-mouseenter="setCursor"
          @mb-mouseleave="clearCursor"
        />
        <div class="slider">
          <v-slider
            v-model="slider"
            thumb-label="always"
            :min="min"
            :max="max"
            @end="filterBy"
            @click="displayPlotLayer(true)"
          />
          <div>
            <v-btn fab small class="ml-2" @click="animateSlide">
              <v-icon dark>mdi-play</v-icon>
            </v-btn>
            <v-btn fab small class="ml-2" @click="stopSlide">
              <v-icon dark>mdi-stop</v-icon>
            </v-btn>
            <v-btn fab small class="ml-2" @click="displayPlotLayer(false)">
              <v-icon dark>mdi-close</v-icon>
            </v-btn>
          </div>
        </div>
      </mapbox-map>
    </div>
    <v-container>
      <p class="ma-0">
        スライダーの数字はダムの竣工年度です（はっきりわからないものについては1790年度として集約しています）。
      </p>
    </v-container>
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
      touchZoomRotate: false,
      zoom: 4,
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
      isDisplayPlotLayer: false,
      zoomUpLayer: {
        id: 'zoomUpLayer',
        type: 'circle',
        source: 'plot',
        paint: {
          'circle-radius': [
            '/',
            ['+', ['log2', ['number', ['get', 'total_pondage']]], 1],
            2.5,
          ],
          'circle-color': '#3794b3',
          'circle-opacity': 0.7,
        },
      },
      plotLayer: {
        id: 'plotLayer',
        type: 'circle',
        source: 'plot',
        layout: {
          visibility: 'none',
        },
        paint: {
          'circle-radius': [
            '/',
            ['+', ['log2', ['number', ['get', 'total_pondage']]], 1],
            2.5,
          ],
          'circle-opacity': 0.7,
          'circle-color': [
            'interpolate',
            ['linear'],
            ['to-number', ['get', 'year_of_completion'], 1790],
            1790,
            '#df9ee2',
            1800,
            '#9233d0',
            2030,
            '#ec3823',
          ],
        },
      },
      coordinates: [null, null],
      name: '',
      yearOfCompletion: '',
      slider: 1800,
      min: 1790,
      max: 2022,
    };
  },
  computed: {
    ...mapState({
      damGeoData: state => state.map.damGeoData,
      isDisplayPopup: state => state.map.isDisplayPopup,
    }),
    plotSource: function() {
      return {
        type: 'geojson',
        cluster: false,
        data: this.$store.state.map.damGeoData,
      };
    },
  },
  methods: {
    filterBy: function(e) {
      const filters = [
        '==',
        ['to-number', ['get', 'year_of_completion'], 1790],
        e,
      ];
      this.map.setFilter('plotLayer', filters);
    },
    displayPlotLayer: function(boolean) {
      if (this.map.getLayer('plotLayer')) {
        if (boolean) {
          this.map.setLayoutProperty('plotLayer', 'visibility', 'visible');
        } else {
          this.map.setLayoutProperty('plotLayer', 'visibility', 'none');
          this.stopSlide();
        }
        this.isDisplayPlotLayer = boolean;
      }
    },
    animateSlide: function() {
      this.displayPlotLayer(true);
      const countUp = () => {
        this.filterBy(this.slider);
        this.slider++;
      };
      this.timer = setInterval(countUp, 400);
    },
    stopSlide: function() {
      clearInterval(this.timer);
    },
    zoomMap: function() {
      this.isDisplayZoomLayer = this.map.getZoom() > this.zoomThreshold;
    },
    displayPopup: function(e) {
      this.coordinates = e.features[0].geometry.coordinates.slice();
      this.name = e.features[0].properties.name;
      this.yearOfCompletion = e.features[0].properties.year_of_completion;
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

.mapboxgl-popup {
  background-color: #ffffff;
  white-space: nowrap;
  padding: 0.3em;
  transform: translate(-50%, -55px);
}

.slider {
  display: flex;
  position: absolute;
  bottom: 1em;
  left: 2em;
  right: 2em;
  z-index: 2;
}
</style>
