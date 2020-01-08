<template>
  <div class="text-center">
    <v-pagination
      v-model="page"
      :length="pageLength"
      @input="getNumber"
    ></v-pagination>
  </div>
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
      console.log(number);
      this.$store.dispatch('map/setPageNum', { page: number });

      if (!this.$props.isEmptySearchField) {
        this.$store.dispatch('map/searchResult');
      } else {
        this.$store.dispatch('map/getDamList');
      }
    },
  },
};
</script>

<style scoped></style>
