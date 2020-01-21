<template>
  <v-card class="mx-auto card" max-width="450" min-height="100%">
    <v-row class="card-inner" justify="space-between" no-gutters>
      <v-col>
        <v-img
          :aspect-ratio="88 / 63"
          src="/img/no_cards_posted.jpg"
          :alt="`${item.name}のカード`"
        ></v-img>

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
          <div class="subtitle-1">{{ item.address }}</div>
          <div>{{ item.water_system_name }}水系 {{ item.river_name }}</div>
        </v-card-text>

        <v-card-text>
          <div>
            コメントです。コメントです。コメントです。コメントです。コメントです。
          </div>
        </v-card-text>
      </v-col>

      <v-col class="card-footer">
        <v-card-actions v-if="this.$route.name === 'mypage'">
          <v-spacer></v-spacer>
          <v-btn @click="goToEditPostPage">
            <v-icon left>mdi-pencil-outline</v-icon>編集
          </v-btn>
          <v-btn><v-icon left>mdi-delete-forever</v-icon>削除</v-btn>
        </v-card-actions>
        <common-card-footer :dam-id="item.dam_code" />
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import CommonCardFooter from './CommonCardFooter';

export default {
  props: ['item', 'userId'],
  components: {
    CommonCardFooter,
  },
  data() {
    return {
      checkbox: false,
    };
  },
  mounted() {
    if (
      this.$store.state.auth.isLoggedIn &&
      parseInt(this.userId) === this.$store.state.auth.userId
    ) {
      this.$router
        .push({ name: 'mypage', params: { userId: this.userId } })
        .catch(error => {
          return { error };
        });
    }
  },
  methods: {
    goToEditPostPage: function() {
      this.$router
        .push({ name: 'edit_post', params: { cardId: 1 } })
        .catch(error => {
          return { error };
        });
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
