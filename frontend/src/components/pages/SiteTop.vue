<template>
  <base-layout>
    <dam-map />
    <dam-search-field />
    <card-list />
  </base-layout>
</template>

<script>
import BaseLayout from '../organisms/BaseLayout';
import DamSearchField from '../organisms/DamSearchField';
import DamMap from '../molecules/DamMap';
import CardList from '../organisms/CardList';

export default {
  components: {
    BaseLayout,
    DamMap,
    DamSearchField,
    CardList,
  },
  mounted() {
    document.title = 'みんなのダムカード';
    this.$store.dispatch('map/getDamGeoData');
    this.$store.dispatch('map/getDamList');
  },
};
</script>
