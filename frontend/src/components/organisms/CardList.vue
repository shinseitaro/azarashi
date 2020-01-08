<template>
  <v-container>
    <v-row>
      <v-col
        v-for="(item, index) in damList"
        :key="index"
        cols="12"
        lg="4"
        md="6"
        xs="12"
      >
        <card-item v-if="isEmptySearchField" :item="item" />
        <card-item
          v-if="!isEmptySearchField && item.properties"
          :item="item.properties"
        />
      </v-col>
    </v-row>
    <pagination></pagination>
    <v-row align="center" justify="center">
      <div class="text-xs-center">
        <v-btn small @click="loadMore">もっと見る</v-btn>
      </div>
    </v-row>
  </v-container>
</template>

<script>
import { mapState } from 'vuex';
import CardItem from '../molecules/CardItem';
import Pagination from '../atoms/Pagination';

export default {
  components: {
    Pagination,
    CardItem,
  },
  computed: {
    ...mapState({
      damList: state => state.map.damList,
      isEmptySearchField: state => state.map.isEmptySearchField,
    }),
  },
  methods: {
    async loadMore() {
      await this.$store.dispatch('map/pageUp');
      await this.$store.dispatch('map/getDamList');
    },
  },
};
</script>
