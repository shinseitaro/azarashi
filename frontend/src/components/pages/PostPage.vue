<template>
  <base-layout>
    <post-form />
  </base-layout>
</template>

<script>
import BaseLayout from '../organisms/BaseLayout';
import PostForm from '../organisms/PostForm';

export default {
  props: ['damId', 'cardId'],
  components: {
    BaseLayout,
    PostForm,
  },
  mounted() {
    document.title = 'カード投稿';
  },
};
</script>
