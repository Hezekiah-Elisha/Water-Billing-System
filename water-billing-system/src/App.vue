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
    <!-- <div v-if="token == null">
      <LoginView/>
    </div>

    <div v-else>
      Vijana
    </div> -->

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
// import LoginView from './views/LoginView.vue';

export default {
  components : {
    SideNav,
    // LoginView
  },
  setup() {
    const token = localStorage.getItem('token');
    console.log(token);
    return {
      token
    }
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
form input {
    width: 100%;
    height: 40px;
    border: 1px solid #001f3f;
    padding: 0 20px;
    font-size: 1rem;
  }
form input:focus {
  outline: none;
}
  
form button {
    width: 100%;
    height: 40px;
    border: 1px solid #001f3f;
    background-color: #001f3f;
    color: #fff;
    font-size: 1rem;
    cursor: pointer;
}
form button:hover {
  background-color: #00bfff;
  border: 1px solid #00bfff;
  color: #fff;
}

form select {
    width: 100%;
    height: 40px;
    border: 1px solid #001f3f;
    padding: 0 20px;
    font-size: 1rem;
  }
  
</style>