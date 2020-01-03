<template>
  <v-card class="mx-auto card" max-width="374" min-height="100%">
    <v-row class="card-inner" justify="space-between" no-gutters>
      <v-col>
        <v-img :aspect-ratio="88 / 63" src="/img/no_cards_posted.jpg"></v-img>

        <v-card-title>
          <v-row align="center" justify="space-between" class="mx-0">
            <span>{{ item.name }}</span>
            <v-checkbox
              v-model="checkbox"
              off-icon="mdi-heart"
              on-icon="mdi-heart"
              color="red"
              hide-details
              class="mt-0"
            ></v-checkbox>
          </v-row>
        </v-card-title>

        <v-card-text>
          <v-row align="center" class="mx-0">
            <v-rating
              :value="4.5"
              color="amber"
              dense
              half-increments
              readonly
              size="14"
            ></v-rating>

            <div class="grey--text ml-4">4.5 (413)</div>
          </v-row>
          <v-row align="start" justify="space-between" class="mx-0 my-4">
            <div>
              <div class="subtitle-1 black--text">
                {{ item.address }}
              </div>
              <div>{{ item.water_system_name }}水系 {{ item.river_name }}</div>
            </div>
            <v-btn icon>
              <v-icon>mdi-map-marker</v-icon>
            </v-btn>
          </v-row>
        </v-card-text>
      </v-col>

      <v-col class="card-footer">
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn><v-icon left>mdi-map-legend</v-icon>配布所</v-btn>
          <v-btn><v-icon left>mdi-cards</v-icon>投稿一覧</v-btn>
          <v-btn><v-icon left>mdi-pencil-plus</v-icon>投稿する</v-btn>
        </v-card-actions>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
export default {
  props: ['item'],
  data() {
    return {
      checkbox: false,
    };
  },
  methods: {
    moveMarker: function(marker) {
      this.$store.dispatch('map/startMove', marker);
    },
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
