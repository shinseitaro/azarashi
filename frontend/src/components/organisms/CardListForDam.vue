<template>
  <v-container>
    <v-row>
      <v-col
        v-for="(item, index) in cards"
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

export default {
  components: {
    CardItemForDam,
  },
  data() {
    return {
      cards: [
        {
          cardId: 1,
          imageUrl: 'http://****',
          userId: 1,
          username: 'aiueo',
          published_date: '2020-01-01',
        },
        {
          cardId: 2,
          imageUrl: 'http://****',
          userId: 2,
          username: 'kaizumaki',
          published_date: '2020-01-01',
        },
        {
          cardId: 3,
          imageUrl: 'http://****',
          userId: 2,
          username: 'kaizumaki',
          published_date: '2020-01-01',
        },
      ],
    };
  },
};
</script>
