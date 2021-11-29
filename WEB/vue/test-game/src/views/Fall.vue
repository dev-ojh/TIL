<template>
  <div id="app">
    <nav>
      <router-link :to="{name: 'page1'}">Slide Page</router-link>
      <router-link :to="{name: 'page4'}">New Page 1</router-link>
      <router-link :to="{name: 'page5'}">New Page 2</router-link>
    </nav>
    <main>
      <transition :name="transitionName">
        <router-view />
      </transition>
    </main>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      transitionName: ""
    };
  },
  watch: {
    $route(to, from) {
      if(to.meta.page == null || from.meta.page == null){
        this.transitionName = "fade";
      }else{
        this.transitionName = to.meta.page > from.meta.page ? "next" : "prev";
      }
      console.log(this.transitionName);
    }
  }
};
</script>

<style>
* { box-sizing: border-box; }
html, body { height: 100%; margin:0; padding:0; }
#app { display: grid; grid-template-rows: min-content; min-height: 100%; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
  -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; color: #FAFAFA; }
nav { display: flex; align-items: center; justify-content: space-around; background-color: #424242; position: sticky; bottom: 0; z-index: 1; }
a { color: white; text-decoration: none; text-transform: uppercase; font-weight: bold; padding: 1em 0; margin: 0 1em; border-bottom: 2px solid transparent; }
a.router-link-exact-active { border-color: inherit; }
main h1{ color:black; }
main { min-height: 100%; display: grid; grid-template: "main"; flex: 1; background-color: white; position: relative; z-index: 0; overflow-x: hidden; }
main > * { grid-area: main; background-color: white; position: relative; }
main > :first-child { z-index: 1; }

/* 전환효과 (Slide) */
.next-leave-to { animation: leaveToLeft 500ms both cubic-bezier(0.165, 0.84, 0.44, 1); z-index: 0; }
.next-enter-to { animation: enterFromRight 500ms both cubic-bezier(0.165, 0.84, 0.44, 1); z-index: 1; }
.prev-leave-to { animation: leaveToRight 500ms both cubic-bezier(0.165, 0.84, 0.44, 1); z-index: 1; }
.prev-enter-to { animation: enterFromLeft 500ms both cubic-bezier(0.165, 0.84, 0.44, 1); z-index: 0; }
@keyframes leaveToLeft { from { transform: translateX(0); } to { transform: translateX(-25%); filter: brightness(0.5); } }
@keyframes enterFromLeft { from { transform: translateX(-25%); filter: brightness(0.5); } to { transform: translateX(0); } }
@keyframes leaveToRight { from { transform: translateX(0); } to { transform: translateX(100%); } }
@keyframes enterFromRight { from { transform: translateX(100%); } to { transform: translateX(0); } }

/* 전환효과 (Fade) */
.fade-enter-active, .fade-leave-active { transition: opacity .8s; }
.fade-enter, .fade-leave-to { opacity: 0; }
</style>
