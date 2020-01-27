<template>
  <v-container>
    <v-toolbar color="primary" dark>
      <v-toolbar-title>貯水量トップ10</v-toolbar-title>
    </v-toolbar>
    <v-row>
      <v-col>
        <v-simple-table height="300px">
          <template v-slot:default>
            <thead>
              <tr>
                <th class="text-left">Name</th>
                <th class="text-left">Calories</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in items" :key="item.name">
                <td>{{ item.name }}</td>
                <td>{{ item.calories }}</td>
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
        <v-simple-table height="300px">
          <template v-slot:default>
            <thead>
              <tr>
                <th class="text-left">Name</th>
                <th class="text-left">Calories</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in items" :key="item.name">
                <td>{{ item.name }}</td>
                <td>{{ item.calories }}</td>
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
        <v-simple-table height="300px">
          <template v-slot:default>
            <thead>
              <tr>
                <th class="text-left">Name</th>
                <th class="text-left">Calories</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in items" :key="item.name">
                <td>{{ item.name }}</td>
                <td>{{ item.calories }}</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'StatsList',
  data() {
    return {
      items: [],
    };
  },
};
</script>

<style scoped></style>
