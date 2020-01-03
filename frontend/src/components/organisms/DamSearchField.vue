<template>
  <div class="lime lighten-5">
    <v-container>
      <v-row>
        <v-col cols="12" md="6" sm="12">
          <search-text-field label="名称" search-action="searchName" />
        </v-col>
        <v-col cols="12" md="6" sm="12">
          <search-text-field label="住所" search-action="searchAddress" />
        </v-col>
        <v-col cols="12" md="4" sm="12">
          <search-text-field label="都道府県" search-action="searchPref" />
        </v-col>
        <v-col cols="12" md="4" sm="12">
          <search-text-field label="河川" search-action="searchRiver" />
        </v-col>
        <v-col cols="12" md="4" sm="12">
          <search-text-field label="水系" search-action="searchWaterSystem" />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import SearchTextField from '../atoms/SearchTextField';

export default {
  components: { SearchTextField },
};
</script>
