<template>
  <v-footer class="primary lighten-2 font-weight-medium white--text mt-4">
    <v-col class="text-center" cols="12">
      {{ new Date().getFullYear() }} — <strong>みんなのダムカード</strong>
    </v-col>
  </v-footer>
</template>

<script>
export default {
  name: 'CommonFooter',
};
</script>

<style scoped></style>
