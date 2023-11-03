<template class="container-fluid">

  <RouterView/>


    <!-- <div v-if="info == true">
      <main class="row">
        <aside class="col-md-2">
        </aside>
        <article class="col-md-10">
          <RouterView/>
        </article>
      </main>
    </div>
    <div v-else>
          <RouterView/>
    </div> -->

</template>

<script>


// import SideNav from './components/SideNav.vue';
// import LoginView from './views/LoginView.vue';
import axios from 'axios';

    // Function to check if the token is still valid
    async function isTokenValid() {
      const token = localStorage.getItem('token'); // Retrieve the JWT token from local storage
      if (!token) {
        return false; // Token is not available, so it's not valid
      }

      try {
        // Send a request to a Flask endpoint to validate the token
        const response = await axios.get('/auth/check-token', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        if (response.status === 200) {
          return true; // Token is valid
        } else {
          return false;
        }
      } catch (error) {
        console.error('Token validation failed:', error);
        return false
      }

      // return false; // Token is invalid
    }

        // Example usage
    async function checkTokenValidity() {
      const isValid = await isTokenValid();
      if (isValid) {
        // Token is still valid
        return true;
      } else {
        // Token is invalid, handle the re-authentication or redirect the user to login
        return false;
      }
    }
    const info = await checkTokenValidity();
    console.log(info);


    // const info = await checkTokenValidity();
    // console.log(await checkTokenValidity());

export default {
  components : {
    // SideNav,
    // LoginView
  },
  setup(){
    // async function isTokenValid() {
    //   const token = localStorage.getItem('token'); // Retrieve the JWT token from local storage
    //   if (!token) {
    //     return false; // Token is not available, so it's not valid
    //   }

    //   try {
    //     // Send a request to a Flask endpoint to validate the token
    //     const response = await axios.get('/auth/check-token', {
    //       headers: {
    //         Authorization: `Bearer ${token}`,
    //       },
    //     });

    //     if (response.status === 200) {
    //       return true; // Token is valid
    //     }
    //   } catch (error) {
    //     console.error('Token validation failed:', error);
    //   }

    //   return false; // Token is invalid
    // }

    //     // Example usage
    // async function checkTokenValidity() {
    //   const isValid = await isTokenValid();
    //   if (isValid) {
    //     // Token is still valid
    //     return true;
    //   } else {
    //     // Token is invalid, handle the re-authentication or redirect the user to login
    //     return false;
    //   }
    // }



    // const token = localStorage.getItem('token');
    // console.log(token);
    return {
      info,
    }
  },
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