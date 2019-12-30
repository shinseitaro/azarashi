<template>
  <base-layout>
    <login-form />
  </base-layout>
</template>

<script>
import BaseLayout from '../organisms/BaseLayout';
import LoginForm from '../organisms/LoginForm';

export default {
  components: {
    BaseLayout,
    LoginForm,
  },
};
</script>
