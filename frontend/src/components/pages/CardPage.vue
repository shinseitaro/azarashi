<template>
  <base-layout>
    <v-container>
      <v-row>
        <individual-card-item :item="item" />
      </v-row>
    </v-container>
  </base-layout>
</template>

<script>
import BaseLayout from '../organisms/BaseLayout';
import IndividualCardItem from '../molecules/IndividualCardItem';

export default {
  props: ['cardId'],
  components: {
    BaseLayout,
    IndividualCardItem,
  },
  data() {
    return {
      item: {
        name: 'あいうえお',
        address: '北海道稚内市大字声問村字上声問',
        water_system_name: '声問川',
        river_name: 'タツニウシュナイ川',
        dam_code: 1,
        userId: 2,
      },
    };
  },
  mounted() {
    const token = localStorage.getItem('token');
    if (token !== null) {
      this.$store.dispatch('auth/update').then(() => {
        if (
          this.$store.state.auth.isLoggedIn &&
          this.item.userId === this.$store.state.auth.userId
        ) {
          this.$router
            .push({ name: 'mycard', params: { userId: this.item.userId } })
            .catch(error => {
              return { error };
            });
        }
      });
    }
  },
};
</script>
