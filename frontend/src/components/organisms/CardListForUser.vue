<template>
  <v-container>
    <v-toolbar color="primary" dark>
      <v-toolbar-title>{{ cardUser }}さんのカード</v-toolbar-title>
    </v-toolbar>
    <v-row>
      <v-col
        v-for="(item, index) in cardList"
        :key="index"
        cols="12"
        lg="4"
        md="6"
        xs="12"
      >
        <card-item-for-user :item="item" :user-id="userId" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapState } from 'vuex';
import CardItemForUser from '../molecules/CardItemForUser';

export default {
  props: ['userId'],
  components: {
    CardItemForUser,
  },
  computed: {
    ...mapState({
      cardList: state => state.card.cardList,
      cardUser: state => state.card.cardUser,
    }),
  },
};
</script>
