<template>
  <v-card>
    <v-toolbar color="indigo" dark>
      <v-toolbar-title>カード配布所</v-toolbar-title>
    </v-toolbar>
    <v-list :key="key" v-for="(item, key) in items">
      <v-list-item>
        <v-list-item-icon class="pt-3">
          <v-icon color="indigo">mdi-hand-pointing-right</v-icon>
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
      <v-divider inset v-if="key !== items.length - 1"></v-divider>
    </v-list>
  </v-card>
</template>

<script>
import DistributionItem from '../molecules/DistributionItem';

export default {
  components: {
    DistributionItem,
  },
  data() {
    return {
      title: {
        name: 'ダム名',
        dam_code: 'ダムコード',
        address: '所在地',
        operation_hour: '配布日時',
        prefecture: '都道府県',
        coordinates: '緯度・経度',
      },
      items: [
        {
          id: 1,
          name: '駒込',
          dam_code: 191,
          url: 'http://web.pref.hyogo.lg.jp/wd16/wd16_000000067.html',
          address: '青森県青森市大字駒込',
          operation_hour:
            '9:00~17:00 (土・日・祝祭日・年末年始は配布しておりません)',
          prefecture: '青森県',
          coordinates: [140.8858935039343, 40.70977115787313],
        },
        {
          id: 1,
          name: '駒込',
          dam_code: 191,
          url: 'http://web.pref.hyogo.lg.jp/wd16/wd16_000000067.html',
          address: '青森県青森市大字駒込',
          operation_hour:
            '9:00~17:00 (土・日・祝祭日・年末年始は配布しておりません)',
          prefecture: '青森県',
          coordinates: [140.8858935039343, 40.70977115787313],
        },
        {
          id: 1,
          name: '駒込',
          dam_code: 191,
          url: 'http://web.pref.hyogo.lg.jp/wd16/wd16_000000067.html',
          address: '青森県青森市大字駒込',
          operation_hour:
            '9:00~17:00 (土・日・祝祭日・年末年始は配布しておりません)',
          prefecture: '青森県',
          coordinates: [140.8858935039343, 40.70977115787313],
        },
      ],
    };
  },
};
</script>
