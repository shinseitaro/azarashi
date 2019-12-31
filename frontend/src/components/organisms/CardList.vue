<template>
  <v-container>
    <v-row>
      <v-col
        v-for="(item, index) in damList.slice(0, 8)"
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
  </v-container>
</template>

<script>
import { mapState } from 'vuex';
import CardItem from '../molecules/CardItem';

export default {
  components: {
    CardItem,
  },
  computed: {
    ...mapState({
      damList: state => state.map.damList,
      isEmptySearchField: state => state.map.isEmptySearchField,
    }),
  },
};
</script>
