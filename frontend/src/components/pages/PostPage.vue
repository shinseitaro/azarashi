<template>
  <base-layout>
    <post-form />
  </base-layout>
</template>

<script>
import BaseLayout from '../organisms/BaseLayout';
import PostForm from '../organisms/PostForm';

export default {
  props: ['damId'],
  components: {
    BaseLayout,
    PostForm,
  },
};
</script>
