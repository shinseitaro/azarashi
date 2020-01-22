<template>
  <v-img
    :aspect-ratio="88 / 63"
    :src="imageUrl"
    :alt="`${name}のカード`"
  ></v-img>
</template>

<script>
export default {
  props: ['url', 'name'],
  computed: {
    imageUrl: function() {
      return this.url ? this.url : '/img/no_cards_posted.jpg';
    },
  },
};
</script>
