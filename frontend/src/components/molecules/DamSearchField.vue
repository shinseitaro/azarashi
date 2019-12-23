<template>
  <v-row>
    <v-col cols="12" md="6" sm="12">
      <v-text-field
        placeholder="名称"
        prepend-icon="mdi-magnify"
        @change="searchName"
      ></v-text-field>
    </v-col>
    <v-col cols="12" md="6" sm="12">
      <v-text-field
        placeholder="住所"
        prepend-icon="mdi-magnify"
        @change="searchAddress"
      ></v-text-field>
    </v-col>
    <v-col cols="12" md="4" sm="12">
      <v-text-field
        placeholder="都道府県"
        prepend-icon="mdi-magnify"
        @change="searchPref"
      ></v-text-field>
    </v-col>
    <v-col cols="12" md="4" sm="12">
      <v-text-field
        placeholder="河川"
        prepend-icon="mdi-magnify"
        @change="searchRiver"
      ></v-text-field>
    </v-col>
    <v-col cols="12" md="4" sm="12">
      <v-text-field
        placeholder="水系"
        prepend-icon="mdi-magnify"
        @change="searchWaterSystem"
      ></v-text-field>
    </v-col>
  </v-row>
</template>

<script>
export default {
  methods: {
    searchName: function(e) {
      if (e !== undefined) {
        this.$store
          .dispatch('map/searchName', e)
          .then(() => {
            this.$store.dispatch('map/emptySearchField');
          })
          .then(() => {
            this.$store.dispatch('map/searchResult');
          });
      }
    },
    searchAddress: function(e) {
      if (e !== undefined) {
        this.$store
          .dispatch('map/searchAddress', e)
          .then(() => {
            this.$store.dispatch('map/emptySearchField');
          })
          .then(() => {
            this.$store.dispatch('map/searchResult');
          });
      }
    },
    searchPref: function(e) {
      if (e !== undefined) {
        this.$store
          .dispatch('map/searchPref', e)
          .then(() => {
            this.$store.dispatch('map/emptySearchField');
          })
          .then(() => {
            this.$store.dispatch('map/searchResult');
          });
      }
    },
    searchRiver: function(e) {
      if (e !== undefined) {
        this.$store
          .dispatch('map/searchRiver', e)
          .then(() => {
            this.$store.dispatch('map/emptySearchField');
          })
          .then(() => {
            this.$store.dispatch('map/searchResult');
          });
      }
    },
    searchWaterSystem: function(e) {
      if (e !== undefined) {
        this.$store
          .dispatch('map/searchWaterSystem', e)
          .then(() => {
            this.$store.dispatch('map/emptySearchField');
          })
          .then(() => {
            this.$store.dispatch('map/searchResult');
          });
      }
    },
  },
};
</script>
