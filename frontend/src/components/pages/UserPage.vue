<template>
  <base-layout>
    <card-list-for-user :user-id="userId" />
  </base-layout>
</template>

<script>
import BaseLayout from '../organisms/BaseLayout';
import CardListForUser from '../organisms/CardListForUser';

export default {
  props: ['userId'],
  components: {
    BaseLayout,
    CardListForUser,
  },
  mounted() {
    this.$store.dispatch('map/getDamList');
  },
};
</script>
