<template>
  <v-card>
    <v-toolbar color="indigo" dark>
      <v-toolbar-title>{{ damInfo.name }}</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn text @click="goToPostPage">
        <v-icon>mdi-pencil-plus</v-icon>投稿する
      </v-btn>
    </v-toolbar>
    <v-list>
      <template v-for="(value, name, index) in damInfo">
        <dam-info-item
          :key="index"
          :title="title"
          :value="value"
          :name="name"
          :first="name === 'name'"
        />
      </template>
    </v-list>
  </v-card>
</template>

<script>
import DamInfoItem from '../molecules/DamInfoItem';
import { mapState } from 'vuex';

export default {
  props: ['damId'],
  components: {
    DamInfoItem,
  },
  data() {
    return {
      title: {
        name: 'ダム名',
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
      },
    };
  },
  computed: {
    ...mapState({
      damInfo: state => state.dam.damInfo,
    }),
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
