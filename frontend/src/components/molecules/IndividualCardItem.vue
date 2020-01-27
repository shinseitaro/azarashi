<template>
  <v-card class="mx-auto card" max-width="450" width="100%" min-height="100%">
    <v-row class="card-inner" justify="space-between" no-gutters>
      <v-col>
        <common-card-img
          v-if="item.dam"
          :url="item.cloudinary_url"
          :name="item.dam.name"
        />

        <common-card-title v-if="item.dam" :item="item.dam" />

        <v-card-text>
          <div>{{ item.comment }}</div>
        </v-card-text>

        <v-card-text>
          <div>
            <date :date="item.published_date" />
          </div>
        </v-card-text>
      </v-col>

      <v-col class="card-footer">
        <v-card-actions v-if="this.$route.name === 'mycard'">
          <common-card-edit-btn :item="item" />
        </v-card-actions>
        <common-card-footer v-if="item.dam" :dam-id="item.dam.dam_code" />
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
  props: ['item'],
  components: {
    CommonCardImg,
    CommonCardTitle,
    CommonCardEditBtn,
    CommonCardFooter,
    Date,
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
