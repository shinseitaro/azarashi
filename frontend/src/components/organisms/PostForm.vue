<template>
  <div>
    <v-textarea
      name="comment"
      label="コメント"
      :value="comment"
      @change="inputComment"
    ></v-textarea>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  computed: {
    ...mapState({
      comment: state => state.form.comment,
    }),
  },
  methods: {
    inputComment: function(e) {
      this.$store.dispatch('form/inputComment', e.target.value);
    },
  },
};
</script>
