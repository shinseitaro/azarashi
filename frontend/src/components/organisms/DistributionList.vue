<template>
  <v-card outlined>
    <v-toolbar color="primary" dark>
      <v-toolbar-title>カード配布所</v-toolbar-title>
    </v-toolbar>
    <v-list :key="key" v-for="(item, key) in items">
      <v-divider inset v-if="key !== 0"></v-divider>

      <v-list-item>
        <v-list-item-icon class="pt-3">
          <v-icon color="info">mdi-hand-pointing-right</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <template v-for="(value, name, index) in item">
            <distribution-item
              :key="index"
              :title="title"
              :value="value"
              :name="name"
            />
          </template>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-card>
</template>

<script>
import DistributionItem from '../molecules/DistributionItem';
import { mapState } from 'vuex';

export default {
  components: {
    DistributionItem,
  },
  data() {
    return {
      title: {
        name: '配布所名',
        url: 'URL',
        address: '所在地',
        operation_hour: '配布日時',
      },
    };
  },
  computed: {
    ...mapState({
      items: state => state.dam.distributionList,
    }),
  },
};
</script>
