<template>
  <base-layout>
    <post-form :dam-id="damId" :card-id="cardId" />
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
  created() {
    document.title = 'カード投稿・編集';
  },
};
</script>
