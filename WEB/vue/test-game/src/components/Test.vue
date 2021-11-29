<template>
  <div>
    <div id="app">

    <h1>안녕하세요</h1>

    <hr>

    <div class="quest" v-for="(q, index) in questions" :key="index">
      <h3>번{{ index + 1 }}호: {{ q.quest }}</h3>
      <label v-for="(answer, index) in q.options" :key="index">
        <input type="radio" :value="answer.value" v-model="q.selected">
        {{ index + 1 }}. {{ answer.ans }}
      </label>

    </div>

    <button @click="settlement">엥</button>
    <button @click="reset">초기화</button>
  </div>
  </div>
</template>

<script>
export default {
    el: '#app',
    data: function () {
      return{
        questions: [
        {
          quest: '如果你是童話故事中，想吃掉三隻小豬的大野狼，你認為使用哪一種方法可以容易吃掉他們？',
          options: [
            { ans: '用煙把小豬燻到昏倒',         value: 1 },
            { ans: '從煙囪或其他入口偷偷爬進屋',  value: 2 },
            { ans: '用槌子把門破壞闖入屋內',      value: 3 },
            { ans: '模仿豬媽媽的聲音騙小豬開門',  value: 4 },
          ],
          selected: null,
        },
        {
          quest: '剪刀、石頭、布，你第一直覺會出哪一個？',
          options: [
            { ans: '剪刀', value: 3 },
            { ans: '石頭', value: 2 },
            { ans: '布',   value: 1 },
          ],
          selected: null
        },
        {
          quest: '下列四項運動項目中，假設你要開始嘗試的話，你最想要做哪一項？',
          options: [
            { ans: '潛水',   value: 3 },
            { ans: '滑翔翼', value: 4 },
            { ans: '滑水',   value: 2 },
            { ans: '長途徒步旅行', value: 1 },
          ],
          selected: null,
        }
      ]}
    },
    computed: {
      total: function(){
        var sum = 0;
        this.questions.forEach(function(v){
          sum += Number(v.selected);
        });
        return sum;
      }
    },
    methods: {
      settlement: function(){
        alert('總分: ' + this.total);
      },
      reset: function(){
        this.questions.forEach(function(v){
          v.selected = null;
        });
      }
    },
  };
</script>

<style>
#app {
      font-size: 1.25em;
}
button{
  font-size: 1.5em;
}
label{
  display: block;
}
.quest{
  margin-bottom: 1em;
  padding-bottom: 1em;
  border-bottom: 1px solid #ccc;
}
</style>