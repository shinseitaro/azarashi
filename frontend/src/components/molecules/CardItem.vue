<template>
  <v-card class="mx-auto card" max-width="450" min-height="100%">
    <v-row class="card-inner" justify="space-between" no-gutters>
      <v-col>
        <common-card-img :url="null" :name="item.name" />

        <common-card-title :item="item" />
      </v-col>

      <v-col class="card-footer">
        <common-card-footer :dam-id="item.dam_code" />
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import CommonCardImg from './CommonCardImg';
import CommonCardTitle from './CommonCardTitle';
import CommonCardFooter from './CommonCardFooter';

export default {
  props: ['item'],
  components: {
    CommonCardImg,
    CommonCardTitle,
    CommonCardFooter,
  },
};
</script>

<style lang="scss">
.card {
  display: flex !important;
}

.card-inner {
  flex-direction: column;
  flex: 1 0 100%;
}

.card-footer {
  flex-grow: 0;
}
</style>
