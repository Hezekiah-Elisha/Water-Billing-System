<template>
<!-- <div class="video">
</div> -->
<div class="row">
    <div class="col-md-2">
        <SideNav/>
    </div>
    <div class="col-md-10">
        <InfoComponent info="Dashboard" />
        <h2>
            Welcome to the dashboard
        </h2>
        <hr>
        <div>
            <img src="@/assets/male-profile-image-placeholder.png" alt="" class="profile-img">
                <p>name : {{ user.username }} </p>
                <p>email: {{ user.email }} </p>
                <p>role: {{ user.role }} </p>
                <p>created at: {{ formatDateTime(user.created_at) }} </p>
            <div v-if="user.role == 'supervisor'">
                You are a Supervisor
            </div>
            <div v-else>
                You are a user
            </div>


            <button @click="logout" class="btn btn-outline-danger"> <i class="bi bi-box-arrow-right"></i> Logout</button>
        </div>
    </div>

</div>

<hr>

</template>

<script>

import SideNav from '@/components/SideNav.vue';
import InfoComponent from '@/components/common/InfoComponent.vue';
import axios from 'axios';


export default {
    name: 'DashboardView',
    components: { 
        SideNav, 
        InfoComponent
    },
    data() {
        return {
            token: localStorage.getItem('token'),
            user: {},
        };
    },
    methods: {
        getProfile() {
            const config = {
                headers: {
                    Authorization: `Bearer ${this.token}`
                }
            };
            axios.get('http://localhost:7000/auth/users/profile', config)
                .then(response => {
                // console.log(response.data)
                this.user = response.data;
            }).catch(error => {
                console.log(error.code);
                this.$router.push('/login');
            });
        },
        formatDateTime(dateString) {
            const mydate = new Date(dateString);
            return `${mydate.toLocaleDateString()} ${mydate.toLocaleTimeString()}`;
        },
        logout() {
            const config = {
                headers: {
                    Authorization: `Bearer ${this.token}`
                }
            };
            axios.delete('http://localhost:7000/auth/logout', config)
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
        this.getProfile();
        this.formatDateTime();
    }
}

</script>

<style scoped>

.profile-img {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    /* margin: 0 auto; */
    display: block;
}

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