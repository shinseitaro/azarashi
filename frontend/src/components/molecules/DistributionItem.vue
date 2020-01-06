<template>
  <div v-if="title[name]">
    <v-list-item>
      <v-list-item-content v-if="name === 'url' && value !== null" class="py-2">
        <div>
          <a :href="value" target="_blank">URL</a>
        </div>
      </v-list-item-content>
      <v-list-item-content v-else class="py-2">
        <v-list-item-subtitle>{{ title[name] }}</v-list-item-subtitle>
        <div>{{ value }}</div>
      </v-list-item-content>
    </v-list-item>
  </div>
</template>

<script>
export default {
  props: ['title', 'value', 'name'],
};
</script>
