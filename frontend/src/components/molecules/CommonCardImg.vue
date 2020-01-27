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
      return this.url
        ? `http://res.cloudinary.com/${process.env.VUE_APP_CLOUDINARY_CLOUD_NAME}/image/upload/${process.env.VUE_APP_CLOUDINARY_IMAGE_PARAMS}/${this.url}`
        : '/img/no_cards_posted.jpg';
    },
  },
};
</script>
