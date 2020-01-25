<template>
  <span>
    <a v-if="cardId" :href="`/card/${cardId}`">
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
};
</script>
s
