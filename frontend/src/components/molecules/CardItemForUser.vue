<template>
  <v-card class="mx-auto card" max-width="450" min-height="100%">
    <v-row class="card-inner" justify="space-between" no-gutters>
      <v-col>
        <common-card-img :url="item.cloudinary_url" :name="item.dam.name" />

        <common-card-title :item="item.dam" />

        <v-card-text>
          <div>{{ item.comment }}</div>
        </v-card-text>

        <v-card-text>
          <div>
            <date :card-id="item.id" :date="item.published_date" />
          </div>
        </v-card-text>
      </v-col>

      <v-col class="card-footer">
        <v-card-actions v-if="this.$route.name === 'mypage'">
          <common-card-edit-btn :card-id="item.id" />
        </v-card-actions>
        <common-card-footer :dam-id="item.dam.dam_code" />
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import CommonCardImg from './CommonCardImg';
import CommonCardTitle from './CommonCardTitle';
import CommonCardEditBtn from './CommonCardEditBtn';
import CommonCardFooter from './CommonCardFooter';
import Date from '../atoms/Date';

export default {
  props: ['item', 'userName'],
  components: {
    CommonCardImg,
    CommonCardTitle,
    CommonCardEditBtn,
    CommonCardFooter,
    Date,
  },
  mounted() {
    if (
      this.$store.state.auth.isLoggedIn &&
      this.userName === this.$store.state.auth.username
    ) {
      this.$router
        .push({ name: 'mypage', params: { userName: this.userName } })
        .catch(error => {
          return { error };
        });
    }
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
