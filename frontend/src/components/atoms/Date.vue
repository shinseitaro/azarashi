<template>
  <span>
    <a v-if="cardId" href="javascript:void(0)" @click="goToCardPage">
      {{ formattedDate }}
    </a>
    <template v-else>
      {{ formattedDate }}
    </template>
  </span>
</template>

<script>
import * as moment from 'moment';

export default {
  props: ['cardId', 'date'],
  computed: {
    formattedDate: function() {
      return moment(this.date).format('YYYY.MM.DD HH:mm');
    },
  },
  methods: {
    goToCardPage: function() {
      this.$router
        .push({ name: 'card', params: { cardId: this.cardId } })
        .catch(error => {
          return { error };
        });
    },
  },
};
</script>
s
