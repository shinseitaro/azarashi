<template>
  <div>
    <v-card-title>
      <v-row align="center" justify="space-between" class="mx-0">
        <span>{{ item.name }}</span>
        <!--        <v-checkbox-->
        <!--          v-model="checkbox"-->
        <!--          off-icon="mdi-heart"-->
        <!--          on-icon="mdi-heart"-->
        <!--          color="red"-->
        <!--          hide-details-->
        <!--          class="mt-0"-->
        <!--        ></v-checkbox>-->
      </v-row>
    </v-card-title>

    <v-card-text>
      <!--      <v-row align="center" class="mx-0">-->
      <!--        <v-rating-->
      <!--          :value="4.5"-->
      <!--          color="amber"-->
      <!--          dense-->
      <!--          half-increments-->
      <!--          readonly-->
      <!--          size="14"-->
      <!--        ></v-rating>-->

      <!--        <div class="grey&#45;&#45;text ml-4">4.5 (413)</div>-->
      <!--      </v-row>-->
      <div class="subtitle-1">{{ item.address }}</div>
      <div>{{ item.water_system_name }}水系 {{ item.river_name }}</div>
    </v-card-text>
  </div>
</template>

<script>
export default {
  props: ['item'],
  data() {
    return {
      checkbox: false,
    };
  },
};
</script>
