<template>
  <div v-if="title[name]">
    <v-divider v-if="!first"></v-divider>

    <v-list-item>
      <v-list-item-icon>
        <v-icon color="indigo">mdi-sign-direction</v-icon>
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
  </div>
</template>

<script>
export default {
  props: ['title', 'value', 'name', 'first'],
};
</script>
