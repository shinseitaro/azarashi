<template>
  <base-layout>
    <individual-dam-map />
    <v-container>
      <dam-info />
    </v-container>
  </base-layout>
</template>

<script>
import BaseLayout from '../organisms/BaseLayout';
import IndividualDamMap from '../molecules/IndividualDamMap';
import DamInfo from '../organisms/DamInfo';

export default {
  props: ['id'],
  components: {
    BaseLayout,
    IndividualDamMap,
    DamInfo,
  },
};
</script>
