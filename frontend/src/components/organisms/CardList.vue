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
    <pagination
      :page-length="pageLength"
      :is-empty-search-field="isEmptySearchField"
    ></pagination>
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
      pageLength: state => state.map.pageLength,
    }),
  },
};
</script>
