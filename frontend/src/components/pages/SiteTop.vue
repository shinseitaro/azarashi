<template>
  <v-app>
    <Header />
    <v-content>
      <Map />
      <DamSearchField />
      <CardList />
    </v-content>
  </v-app>
</template>

<script>
import DamSearchField from '../organisms/DamSearchField';
import Map from '../molecules/Map';
import Header from '../organisms/Header';
import CardList from '../organisms/CardList';

export default {
  components: {
    DamSearchField,
    Header,
    Map,
    CardList,
  },
  mounted() {
    this.$store.dispatch('map/getDamGeoData');
    this.$store.dispatch('map/getDamList');
  },
};
</script>
