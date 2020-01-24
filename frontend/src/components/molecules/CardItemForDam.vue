<template>
  <v-card class="mx-auto card" max-width="450" min-height="100%">
    <v-row class="card-inner" justify="space-between" no-gutters>
      <v-col>
        <common-card-img :url="null" :name="item.username" />

        <v-card-text>
          <v-row justify="space-between" class="mx-0">
            <div>
              <a :href="`/user/${item.username}`">
                {{ item.username }}
              </a>
            </div>
            <div>
              <a :href="`/card/${item.cardId}`">
                {{ item.published_date }}
              </a>
            </div>
          </v-row>
        </v-card-text>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import CommonCardImg from './CommonCardImg';

export default {
  props: ['item'],
  components: {
    CommonCardImg,
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
</style>
