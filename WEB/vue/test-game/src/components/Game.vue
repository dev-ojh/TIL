<template>
  <div>
    <b-container class="container">
      <transition name="fade">
        <section v-if="show" class="mx-auto my-5 py-5 px-3 {}">
          <h1>십이간지로 알아보는 연애유형</h1>
          <div class="col-lg-6 col-md-8 col-sm-10 col-12 mx-auto">
            <img src="../assets/logo.png" alt="mainImage" class="img-fluid">
          </div>
          <p>
            나만의 MBTI 사이트입니다! <br>
            아래 시작하기 버튼을 눌러 시작해 주십시오.
          </p>
          <button type="button" class="btn btn-outline-danger mt-3" v-on:click="show = !show">시작하기</button>
            
        </section>
      </transition>
      <transition name="fade">
        <section v-show="!show">
          <div class="status mx-auto mt-5">
            <div class="statusBar">
            </div>
          </div>
          <div class="qBox my-5 py-3 mx-auto">
          </div>

          <div class="row row-cols-1 row-cols-md-2 g-2 answerBox mx-auto">
            <div class="col">
              <div class="card">
                <!-- <img src="./img/main.png" class="card-img-top leftImage" alt="..."> -->
              </div>
            </div>
            <div class="col">
              <div class="card">
                <!-- <img src="./img/main.png" class="card-img-top rightImage" alt="..."> -->
              </div>
            </div>
          </div>
        </section>
      </transition>
      

      <section id="result" class="mx-auto my-5 py-5 px-3">
        <h1>당신의 결과는?!</h1>
        <div class="resultname">

        </div>
        <div id="resultImg" class="my-3 col-lg-6 col-md-8 col-sm-10 col-12 mx-auto">

        </div>
        <div class="resultDesc">

        </div>
        <!-- <button type="button" class="kakao mt-3 py-2 px-3" onclick="js:setShare()">공유하기</button> -->
      </section>
  <!-- 
      <script src="./js/data.js" charset="utf-8"></script>
      <script src="./js/start.js" charset="utf-8"></script>
      <script src="./js/share.js" charset="utf-8"></script> -->
    </b-container>
  </div>
</template>

<script>

export default {
  name: 'Game',
  data: function () {
    return {
      show: true
    }
  },
  methods:{
    begin: function() {
      const main = this.$refs.main;
      const qna = this.$refs.qna;
      main.style.WebkitAnimation = "fadeOut 1s";
      main.style.animation = "fadeOut 1s";
      setTimeout(() => {
        qna.style.WebkitAnimation = "fadeIn 1s";
        qna.style.animation = "fadeIn 1s";
        setTimeout(() => {
          main.style.display = "none";
          qna.style.display = "block"
        }, 450)
        // let qIdx = 0;
        // goNext(qIdx);
      }, 450);
    },
  }
}
</script>

<style scoped>
/* default css */
.container{
  font-family: 'DX시인과나'
}
/* main css */
#main{
  background-color: whitesmoke;
  width: 80%;
  text-align: center;
  border-radius: 20px;
}

p{
  font-size: 20px;
}
/* qna css */
#qna {
  display: none;
}

.qBox {
  background-color: whitesmoke;
  text-align: center;
  border-radius: 20px;
  font-size: 24px;
  width: 80%
}

.answerList {
  background-color: whitesmoke;
  border-radius: 20px;
  display: block;
  width: 80%;
  border: 0px;
  font-size: 20px;
}

.answerList:hover, .answerList:focus {
  background-color: pink;
  color: whitesmoke;
}

.status {
  height: 20px;
  width: 80%;
  background-color: white;
  border-radius: 20px;
}

.statusBar {
  height: 100%;
  border-radius: 20px;
  /* Permalink - use to edit and share this gradient: https://colorzilla.com/gradient-editor/#febbbb+0,fe9090+52,ff5c5c+100;Red+3D+%231 */
  background: #febbbb;
  /* Old browsers */
  background: -moz-linear-gradient(top, #febbbb 0%, #fe9090 52%, #ff5c5c 100%);
  /* FF3.6-15 */
  background: -webkit-linear-gradient(top, #febbbb 0%, #fe9090 52%, #ff5c5c 100%);
  /* Chrome10-25,Safari5.1-6 */
  background: linear-gradient(to bottom, #febbbb 0%, #fe9090 52%, #ff5c5c 100%);
  /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#febbbb', endColorstr='#ff5c5c', GradientType=0);
  /* IE6-9 */
}

.answerBox{
  width: 80%;
}
/* animation css */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes fadeOut {
  from { opacity: 1; }
  to { opacity: 0; }
}

@-webkit-keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@-webkit-keyframes fadeOut {
  from { opacity: 1; }
  to { opacity: 0; }
}

.fadeIn{
  animation: fadeIn;
  animation-duration: 1s;
}

.fadeOut{
  animation: fadeOut;
  animation-duration: 1s;
}

/* result.css */
#result{
  display: none;
  background-color: whitesmoke;
  width: 80%;
  text-align: center;
  border-radius: 20px;
}

#shareResult{
  background-color: whitesmoke;
  width: 80%;
  text-align: center;
  border-radius: 20px;
}

.resultname{
  font-size: 26px;
}

.resultDesc{
  font-size: 20px;
}

.kakao{
  color: white;
  background-color: #FEE500;
  font-size: 20px;
  border: 0px;
  border-radius: 20px;
}

.kakao:hover, .kakao:focus {
  background-color: whitesmoke;
  color: #FEE500;
}

.gohome{
  color: white;
  background-color: pink;
  font-size: 20px;
  border: 0px;
  border-radius: 20px;
}

.gohome:hover, .gohome:focus {
  background-color: whitesmoke;
  color: pink;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>