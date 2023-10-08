<template>

<div class="video">
</div>

<div>
    name : {{ user.username }} <br>
    email: {{ user.email }} <br>
    role: {{ user.role }} <br>
    created at: {{ formatDateTime(user.created_at) }} <br>
    <div v-if="user.role == 'admin'">
        You are an admin
    </div>
    <div v-else>
        You are a user
    </div>
</div>

<div></div>

</template>

<script>

import axios from 'axios';


export default {
    name: 'DashboardView',
    // components: {
    //   HelloWorld
    // }
    data() {
        return {
            token: localStorage.getItem('token'),
            user: {}
        }
    },
    methods: {
        getProfile() {

            const config = {
                headers: {
                    Authorization: `Bearer ${this.token}`
                }
            };

            axios.get('http://localhost:7000/auth/user/profile', config)
            .then(response => {
                // console.log(response.data)
                this.user = response.data
            }).then(error => {
                console.log(error)
            });
        },
        formatDateTime(dateString) {
            const mydate = new Date(dateString);
            return `${mydate.toLocaleDateString()} ${mydate.toLocaleTimeString()}`;        
        }
    },
    mounted() {
        this.getProfile()
        this.formatDateTime()
    }
}

</script>

<style scoped>

.video:empty {
  width: 315px;
  height: 250px; 
  cursor: progress; 
  background: 
    linear-gradient(0.25turn, transparent, #fff, transparent),
    linear-gradient(#eee, #eee),
    radial-gradient(38px circle at 19px 19px, #eee 50%, transparent 51%),
    linear-gradient(#eee, #eee);  
  background-repeat: no-repeat;
  background-size: 315px 250px, 315px 180px, 100px 100px, 225px 30px; 
  background-position: -315px 0, 0 0, 0px 190px, 50px 195px; 
  animation: loading 1.5s infinite;
}


@keyframes loading {  
  to {
    background-position: 315px 0, 0 0, 0 190px, 50px 195px;
  }
}



</style>