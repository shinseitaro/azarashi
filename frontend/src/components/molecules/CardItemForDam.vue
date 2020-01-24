<template>
  <v-card class="mx-auto card" max-width="450" min-height="100%">
    <v-row class="card-inner" justify="space-between" no-gutters>
      <v-col>
        <common-card-img :url="item.cloudinary_url" :name="item.user.name" />

        <v-card-text>
          <v-row justify="space-between" class="mx-0">
            <div>
              <a :href="`/user/${item.user.name}`">
                {{ item.user.name }}
              </a>
            </div>
            <div>
              <a :href="`/card/${item.id}`">
                {{ publishedDate }}
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
import * as moment from 'moment';

export default {
  props: ['item'],
  components: {
    CommonCardImg,
  },
  computed: {
    publishedDate: function() {
      return moment(this.item.published_date).format('YYYY.MM.DD HH:mm');
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
