<template>
  <v-card>
    <v-toolbar color="indigo" dark>
      <v-toolbar-title>{{ items.name }}</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn text @click="goToPostPage">
        <v-icon>mdi-pencil-plus</v-icon>投稿する
      </v-btn>
    </v-toolbar>
    <v-list>
      <template v-for="(value, name, index) in items">
        <dam-info-item
          :key="index"
          :title="title"
          :value="value"
          :name="name"
          :last="index === Object.keys(items).length - 1"
        />
      </template>
    </v-list>
  </v-card>
</template>

<script>
import DamInfoItem from '../molecules/DamInfoItem';

export default {
  props: ['damId'],
  components: {
    DamInfoItem,
  },
  data() {
    return {
      title: {
        name: 'ダム名',
        dam_code: 'ダムコード',
        water_system_name: '水系名',
        river_name: '河川名',
        type_code: '形式',
        purpose_code: '目的',
        scale_bank_height: '堤高',
        scale_bank_span: '堤頂長',
        bank_volume: '堤体積',
        total_pondage: '総貯水量',
        institution_in_charge: 'ダム事業者名',
        year_of_completion: '竣工年度',
        address: '所在地',
        positional_information_precision: '位置情報精度',
        prefecture: '都道府県',
        category_id: 'カテゴリー',
        coordinates: '緯度・経度',
      },
      items: {
        id: 1,
        name: '駒込',
        dam_code: 191,
        water_system_name: '堤川',
        river_name: '駒込川',
        type_code: '重力式コンクリートダム',
        purpose_code: [
          {
            name: '洪水調節，農地防災',
          },
          {
            name: '不特定用水，河川維持用水',
          },
          {
            name: '発電',
          },
        ],
        scale_bank_height: 84.5,
        scale_bank_span: 270.0,
        bank_volume: 320,
        total_pondage: 7800,
        institution_in_charge: [
          {
            name: '都道府県',
          },
        ],
        year_of_completion: '-',
        address: '青森県青森市大字駒込',
        positional_information_precision: 4,
        prefecture: '青森県',
        category_id: 1,
        coordinates: [140.8858935039343, 40.70977115787313],
      },
    };
  },
  methods: {
    goToPostPage: function() {
      this.$router
        .push({ name: 'post', params: { damId: this.damId } })
        .catch(error => {
          return { error };
        });
    },
  },
};
</script>
