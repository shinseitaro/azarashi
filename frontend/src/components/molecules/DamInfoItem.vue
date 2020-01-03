<template>
  <div>
    <v-list-item>
      <v-list-item-icon>
        <v-icon color="indigo">mdi-map-marker</v-icon>
      </v-list-item-icon>

      <v-list-item-content>
        <v-list-item-subtitle>{{ title[name] }}</v-list-item-subtitle>
        <div>
          {{
            name === 'purpose_code' || name === 'institution_in_charge'
              ? Object.keys(value)
                  .reduce((acc, val) => acc.concat(value[val].name), [])
                  .join('：')
              : value
          }}
        </div>
      </v-list-item-content>
    </v-list-item>

    <v-divider></v-divider>
  </div>
</template>

<script>
export default {
  props: ['title', 'value', 'name'],
};
</script>
