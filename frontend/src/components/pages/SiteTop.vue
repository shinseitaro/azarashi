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
import DamSearchField from '../molecules/DamSearchField';
import Map from '../molecules/Map.vue';
import Header from '../organisms/Header.vue';
import CardList from '../organisms/CardList.vue';

export default {
  components: {
    DamSearchField,
    Header,
    Map,
    CardList,
  },
  mounted() {
    this.$store.dispatch('map/getDamData');
  },
};
</script>
