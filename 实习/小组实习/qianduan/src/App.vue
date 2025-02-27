<template>
  <div id="app">
    <nav>
      <router-link to="/">退出登录</router-link>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {

  }
}
</script>

<style>
#app {
    height: 100%;
}
</style>
