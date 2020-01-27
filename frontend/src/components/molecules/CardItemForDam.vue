<template>
  <v-card class="mx-auto card" max-width="450" min-height="100%">
    <v-row class="card-inner" justify="space-between" no-gutters>
      <v-col>
        <common-card-img :url="item.cloudinary_url" :name="item.user.name" />

        <v-card-text>
          <v-row justify="space-between" class="mx-0">
            <div>
              <a href="javascript:void(0)" @click="goToUserPage">
                {{ item.user.name }}
              </a>
            </div>
            <div>
              <date :card-id="item.id" :date="item.published_date" />
            </div>
          </v-row>
        </v-card-text>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import CommonCardImg from './CommonCardImg';
import Date from '../atoms/Date';

export default {
  props: ['item'],
  components: {
    CommonCardImg,
    Date,
  },
  methods: {
    goToUserPage: function() {
      this.$router
        .push({ name: 'user', params: { userName: this.item.user.name } })
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
</style>
