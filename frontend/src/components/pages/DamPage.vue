<template>
  <base-layout>
    <individual-dam-map />
    <v-container>
      <dam-info />
    </v-container>
    <card-list-for-dam />
  </base-layout>
</template>

<script>
import BaseLayout from '../organisms/BaseLayout';
import IndividualDamMap from '../molecules/IndividualDamMap';
import DamInfo from '../organisms/DamInfo';
import CardListForDam from '../organisms/CardListForDam';

export default {
  props: ['damId'],
  components: {
    BaseLayout,
    IndividualDamMap,
    DamInfo,
    CardListForDam,
  },
};
</script>
