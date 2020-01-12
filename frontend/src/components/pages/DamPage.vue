<template>
  <base-layout>
    <individual-dam-map />
    <v-container>
      <v-row>
        <v-col cols="12" md="5" xs="12">
          <dam-info :dam-id="damId" />
        </v-col>
        <v-col cols="12" md="7" xs="12">
          <distribution-list />
        </v-col>
      </v-row>
    </v-container>
    <card-list-for-dam />
  </base-layout>
</template>

<script>
import BaseLayout from '../organisms/BaseLayout';
import IndividualDamMap from '../molecules/IndividualDamMap';
import DamInfo from '../organisms/DamInfo';
import DistributionList from '../organisms/DistributionList';
import CardListForDam from '../organisms/CardListForDam';

export default {
  props: ['damId'],
  components: {
    BaseLayout,
    IndividualDamMap,
    DamInfo,
    DistributionList,
    CardListForDam,
  },
  mounted() {
    this.$store
      .dispatch('dam/getDam', this.damId)
      .then(() => {
        document.title = this.$store.state.dam.damName + 'ダム情報';
      })
      .catch(error => {
        return { error };
      });
  },
};
</script>
