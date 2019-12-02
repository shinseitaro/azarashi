<template>
  <v-app>
    <Header />
    <v-content>
      <Map />
      <CardList />
    </v-content>
  </v-app>
</template>

<script>
import Map from '../molecules/Map.vue';
import Header from '../organisms/Header.vue';
import CardList from '../organisms/CardList.vue';

export default {
  components: {
    Header,
    Map,
    CardList,
  },
  mounted() {
    this.$store.dispatch('map/getDamData');
  },
};
</script>
