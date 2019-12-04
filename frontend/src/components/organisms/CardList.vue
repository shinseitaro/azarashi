<template>
  <v-container class="grey lighten-5">
    <v-row>
        <v-col
          v-for="(dam, index) in dams"
          :key="index"
          cols="12"
          md="3"
        >
          <Card :dam="dam"/>
        </v-col>
    </v-row>
    <v-btn small @click="loadMore">もっと見る</v-btn>
  </v-container>
</template>

<script>
    import {mapState} from 'vuex';
    import Card from '../molecules/Card.vue';

    export default {
        components: {
            Card,
        },
        data() {
            return {
                busy: false
            }
        },
        computed: {
            ...mapState({
                markers: state => state.map.markers,
                dams: state => state.map.damDataForCardList
            }),
        },
        methods: {
            async loadMore() {
                this.busy = true;
                console.log('page up')
                await this.$store.dispatch('map/pageUp');
                //read pages
                await this.$store.dispatch('map/getDamDataForCardList');
                this.busy = false;
            }
        },
        created() {
            this.$store.dispatch('map/getDamDataForCardList');
        }
    };
</script>
