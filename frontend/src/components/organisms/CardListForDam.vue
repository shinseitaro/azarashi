<template>
  <v-container>
    <v-row>
      <v-col
        v-for="(item, index) in cardList"
        :key="index"
        cols="12"
        lg="4"
        md="6"
        xs="12"
      >
        <card-item-for-dam :item="item" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import CardItemForDam from '../molecules/CardItemForDam';
import { mapState } from 'vuex';

export default {
  components: {
    CardItemForDam,
  },
  computed: {
    ...mapState({
      cardList: state => state.card.cardList,
    }),
  },
};
</script>
