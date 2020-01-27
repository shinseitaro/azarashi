<template>
  <v-row justify="center">
    <v-pagination
      v-model="page"
      :length="pageLength"
      total-visible="7"
      @input="getNumber"
    ></v-pagination>
  </v-row>
</template>

<script>
export default {
  name: 'Pagination',
  props: ['pageLength', 'isEmptySearchField'],
  data() {
    return {
      page: 1,
    };
  },
  methods: {
    getNumber(number) {
      this.$store.dispatch('map/setPageNum', { page: number }).then(() => {
        if (!this.$props.isEmptySearchField) {
          this.$store.dispatch('map/searchResult');
        } else {
          this.$store.dispatch('map/getDamList');
        }
      });
    },
  },
};
</script>
