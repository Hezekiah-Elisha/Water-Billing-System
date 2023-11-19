<template>
  Welcome

</template>


<script>
import axios from 'axios';
// import { useAuthStore } from '@/stores/auth'

// const auth = new useAuthStore()

// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld'

export default {
  name: 'HomeView',
  // components: {
  //   HelloWorld
  // }
  data() {
    return {
      email: '',
      password: '',
      error: ''
    }
  },
  methods: {
    submit() {
      axios.post('auth/login', {
        email: this.email,
        password: this.password
      })
      .then(response => {
        // console.log(response.data)
        if (response.status === 200) {
          // console.log('success')
          localStorage.setItem('token', response.data['access_token'])
          // auth.setToken(response.data['access_token'])
          // auth.setUser(response.data['user'])
          this.$router.push('/dashboard')
        }
        else if (response.status === 400) {
          console.log('Note: Email or Password is incorrect')
          this.error = 'Email or Password is incorrect'
        }

      }).catch(error => {
        // console.log(error.code)
        this.error = 'Email or Password is incorrect, error code: ' + error.code
      });
    }
  }
}
</script>

<style scoped>
.home {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.home form {
  width: 400px;
  height: 400px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
}

.home form h2 {
  font-size: 2rem;
  color: #333;
}

.home form input {
  width: 100%;
  height: 40px;
  border: 1px solid #001f3f;
  padding: 0 20px;
  font-size: 1rem;
}

.home form input:focus {
  outline: none;
}

.home form button {
  width: 100%;
  height: 40px;
  border: 1px solid #001f3f;
  background-color: #001f3f;
  color: #fff;
  font-size: 1rem;
  cursor: pointer;
}

</style>
