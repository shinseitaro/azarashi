<template>
  <div class="text-center">
    <v-pagination v-model="page" :length="6" @input="getNumber"></v-pagination>
  </div>
</template>

<script>
export default {
  name: 'Pagination',
  props: [],
  data() {
    return {
      page: 1,
    };
  },
  methods: {
    getNumber(number) {
      console.log(number);
      this.$store.dispatch('map/setPageNum', { page: number });
      this.$store.dispatch('map/searchResult');
    },
  },
};
</script>

<style scoped></style>
