<template>
  <v-row class="mx-0">
    <v-spacer></v-spacer>
    <v-btn @click="goToEditPostPage">
      <v-icon left>mdi-pencil-outline</v-icon>編集
    </v-btn>
    <v-btn @click.stop="dialog = true">
      <v-icon left>mdi-delete-forever</v-icon>削除
    </v-btn>
    <v-dialog v-model="dialog" max-width="290">
      <v-card>
        <v-card-title class="headline">本当に削除しますか？</v-card-title>

        <v-card-text>
          {{ item.dam.name }}ダムの
          <date :date="item.published_date" />
          投稿のカードを削除します。本当に削除しますか？
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn @click="dialog = false">
            キャンセル
          </v-btn>

          <v-btn color="primary" @click="deleteCard">
            削除
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import Date from '../atoms/Date';
import * as API from '../../apis/API';

export default {
  props: ['item'],
  components: {
    Date,
  },
  data() {
    return {
      dialog: false,
    };
  },
  methods: {
    goToEditPostPage: function() {
      this.$router
        .push({ name: 'edit_post', params: { cardId: this.item.id } })
        .catch(error => {
          return { error };
        });
    },
    deleteCard: function() {
      API.destroy('card', this.item.id).then(() => {
        if (this.$route.name === 'mycard') {
          this.$router
            .push({
              name: 'mypage',
              params: { userName: this.$store.state.auth.username },
            })
            .catch(error => {
              return { error };
            });
        } else {
          this.$store.dispatch(
            'card/getCardList',
            this.$store.state.auth.username
          );
        }
        this.dialog = false;
      });
    },
  },
};
</script>
