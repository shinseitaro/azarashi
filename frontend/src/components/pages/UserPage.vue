<template>
  <base-layout>
    <card-list-for-user :user-name="userName" />
  </base-layout>
</template>

<script>
import BaseLayout from '../organisms/BaseLayout';
import CardListForUser from '../organisms/CardListForUser';

export default {
  props: ['userName'],
  components: {
    BaseLayout,
    CardListForUser,
  },
  created() {
    this.$store.dispatch('card/getCardList', this.userName);
    document.title = this.userName + 'さんのカード';
  },
};
</script>
