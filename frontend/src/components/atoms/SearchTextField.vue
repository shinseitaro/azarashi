<template>
  <v-text-field
    outlined
    hide-details
    background-color="white"
    :label="label"
    prepend-inner-icon="mdi-magnify"
    @change="search"
  ></v-text-field>
</template>

<script>
export default {
  props: ['label', 'searchAction'],
  methods: {
    search: function(e) {
      if (e !== undefined) {
        this.$store
          .dispatch('map/setPageNum', { page: 1 })
          .then(() => {
            this.$store.dispatch('map/' + this.searchAction, e);
          })
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
