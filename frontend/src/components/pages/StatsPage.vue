<template>
  <base-layout>
    <stats-list />
  </base-layout>
</template>

<script>
import StatsList from '../organisms/StatsList';
import BaseLayout from '../organisms/BaseLayout';

export default {
  name: 'StatsPage',
  components: { BaseLayout, StatsList },
  created() {
    document.title = 'ダム統計情報';
  },
};
</script>

<style scoped></style>
