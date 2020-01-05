<template>
  <v-card class="mx-auto card" max-width="450" min-height="100%">
    <v-row class="card-inner" justify="space-between" no-gutters>
      <v-col>
        <v-img
          :aspect-ratio="88 / 63"
          src="/img/no_cards_posted.jpg"
          :alt="`${item.username}が投稿したカード`"
        ></v-img>

        <v-card-text>
          <v-row justify="space-between" class="mx-0">
            <div>
              <a :href="`/user/${item.userId}`">
                {{ item.username }}
              </a>
            </div>
            <div>{{ item.published_date }}</div>
          </v-row>
        </v-card-text>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
export default {
  props: ['item'],
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
