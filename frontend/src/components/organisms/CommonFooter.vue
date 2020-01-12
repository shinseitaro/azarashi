<template>
  <v-footer class="font-weight-medium white--text mt-4 footer">
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

<style lang="scss">
.footer {
  background-color: #5b5b51 !important;
}
</style>
