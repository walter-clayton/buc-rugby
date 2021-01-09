<template>
  <div id="app">
    <NavBarTop />
    <Tabs />
    <router-view />
  </div>
</template>

<script>
import NavBarTop from "@/components/NavBarTop.vue";
import Tabs from "@/components/Tabs.vue";
export default {
  name: "App",
  components: {
    NavBarTop,
    Tabs
  }
};
</script>
<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
