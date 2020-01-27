<template>
  <base-layout>
    <v-container>
      <v-row>
        <individual-card-item :item="item" />
      </v-row>
    </v-container>
  </base-layout>
</template>

<script>
import BaseLayout from '../organisms/BaseLayout';
import IndividualCardItem from '../molecules/IndividualCardItem';
import { mapState } from 'vuex';

export default {
  props: ['cardId'],
  components: {
    BaseLayout,
    IndividualCardItem,
  },
  computed: {
    ...mapState({
      item: state => state.card.cardItem,
    }),
  },
  created() {
    this.$store.dispatch('card/getCardItem', this.cardId).then(() => {
      const token = localStorage.getItem('token');
      if (token !== null) {
        this.$store.dispatch('auth/update').then(() => {
          if (
            this.$store.state.auth.isLoggedIn &&
            this.item.user.name === this.$store.state.auth.username
          ) {
            this.$router
              .push({
                name: 'mycard',
                params: { userName: this.item.user.name },
              })
              .catch(error => {
                return { error };
              });
          }
        });
      }
    });
  },
};
</script>
