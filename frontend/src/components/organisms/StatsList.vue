<template>
  <v-container>
    <v-toolbar color="primary" dark>
      <v-toolbar-title>貯水量トップ10</v-toolbar-title>
    </v-toolbar>
    <v-row>
      <v-col>
        <v-simple-table>
          <template v-slot:default>
            <thead>
              <tr>
                <th class="text-left">ダム名</th>
                <th class="text-left">総貯水量(千m&sup3;)</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in top_totalpontage_items" :key="item.name">
                <td>{{ item.name }}</td>
                <td>{{ item.total_pondage }}</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-col>
    </v-row>
    <v-toolbar color="primary" dark>
      <v-toolbar-title>貯水量ボトム10</v-toolbar-title>
    </v-toolbar>
    <v-row>
      <v-col>
        <v-simple-table>
          <template v-slot:default>
            <thead>
              <tr>
                <th class="text-left">ダム名</th>
                <th class="text-left">総貯水量(千m&sup3;)</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in bottom_totalpontage_items" :key="item.name">
                <td>{{ item.name }}</td>
                <td>{{ item.total_pondage }}</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-col>
    </v-row>
    <v-toolbar color="primary" dark>
      <v-toolbar-title>ダムが多い都道府県トップ10</v-toolbar-title>
    </v-toolbar>
    <v-row>
      <v-col>
        <v-simple-table>
          <template v-slot:default>
            <thead>
              <tr>
                <th class="text-left">都道府県</th>
                <th class="text-left">ダム数</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in top_by_pref_items" :key="item.name">
                <td>{{ item.prefecture }}</td>
                <td>{{ item.count }}</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import * as API from '../../apis/API';
export default {
  name: 'StatsList',
  data() {
    return {
      top_totalpontage_items: [],
      bottom_totalpontage_items: [],
      top_by_pref_items: [],
    };
  },
  mounted() {
    API.access('dam/top_totalpontage', 'GET').then(response => {
      console.log(response.payload);
      this.top_totalpontage_items = response.payload;
    });
    API.access('dam/bottom_totalpontage', 'GET').then(response => {
      console.log(response.payload);
      this.bottom_totalpontage_items = response.payload;
    });
    API.access('dam/top_by_pref', 'GET').then(response => {
      console.log(response.payload);
      this.top_by_pref_items = response.payload;
    });
  },
};
</script>

<style scoped></style>
