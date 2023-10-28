<template class="container-fluid">
  <!-- <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> |
    <router-link to="/test">Test</router-link>
  </nav> -->

  <!-- <div v-if="token == null"> -->
    <!-- <LoginView/> -->
    <!-- hhaha -->
  <!-- </div> -->
  <!-- <div v-else> -->
    <main class="row">
      <aside class="col-md-2">
        <SideNav/>
      </aside>
      <article class="col-md-10">
        <RouterView/>
      </article>
    </main>
  <!-- </div> -->


  

  <!-- <router-view/> -->
  <!-- <div v-if="token != null">
      <router-view/>
  </div>
  <div v-else>
     haha
  </div> -->
</template>

<script>

import SideNav from './components/SideNav.vue';

export default {
  components : {
    SideNav
  }
}

</script>



<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
}

:root{
  --primary-color: #001f3f;
  --secondary-color: #00bfff;
  --tertiary-color: #f0f0f0;
  --neutral-color: #ffffff;
}

/* nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
} */
</style>