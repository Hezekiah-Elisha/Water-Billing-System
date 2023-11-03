<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">{{ info }}</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#"></a>
        </li>
      </ul>
      <div class="nav">
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Welcome {{ username }}
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Profile</a></li>
            <li><hr class="dropdown-divider"></li>
            <li @click="logout" class="dropdown-item text-danger">
                <!-- <button @click="logout" class="btn btn-outline-danger"> <i class="bi bi-box-arrow-right"></i> Logout</button> -->
                logout

            </li>
          </ul>
        </li>
      </div>
    </div>
  </div>
</nav>
</template>

<script>
import axios from 'axios';

export default{
    name: 'InfoComponent',
    props: {
        info: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            username: null
        }
    },
    methods: {
        getUsername(){
            axios.get('auth/users/username')
            .then(response => {
                this.username = response.data["username"];
            })
            .catch(error => {
                console.log(error);
            })
        },
        logout() {
            // const config = {
            //     headers: {
            //         Authorization: `Bearer ${this.token}`
            //     }
            // };
            axios.delete('/auth/logout')
                .then(response => {
                // console.log(response.data)
                if (response.status === 200) {
                    // console.log('success')
                    localStorage.removeItem('token');
                    localStorage.removeItem('user');
                    this.$router.push('/login');
                }
            }).catch(error => {
                console.log(error.code);
            });
        }
    },
    mounted() {
        this.getUsername();
    }
}

</script>