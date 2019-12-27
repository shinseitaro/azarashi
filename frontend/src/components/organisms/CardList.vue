<template>
  <v-container class="grey lighten-5">
    <v-row>
      <v-col
        v-for="(item, index) in damList.slice(0, 8)"
        :key="index"
        cols="12"
        lg="4"
        md="6"
        xs="12"
      >
        <Card :item="item" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapState } from 'vuex';
import Card from '../molecules/Card';

export default {
  components: {
    Card,
  },
  computed: {
    ...mapState({
      damList: state => state.map.damList,
    }),
  },
};
</script>
