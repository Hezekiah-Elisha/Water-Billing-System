<template>
    <div class="tile">
        <h3>{{ user.username }}</h3>
        <hr>
        <p>Email: {{ user.email }}</p>
        Role: {{ user.role }}

        <div class="row">
            <!-- <button class="btn btn-outline-primary col-10"> <i class="bi bi-pen-fill"></i> Edit Profile</button> -->
            <router-link
                :to="{ name: 'supervisor', params: { id: user.id } }"
                class="btn btn-outline-info col-10">
                <i class="bi bi-pen-fill"></i>
                Edit profile
            </router-link>
            <button @click="deleteSupervisor(supervisor.id)" class="btn btn-danger col-2"> <i class="bi bi-trash2-fill"></i> </button>
        </div>
    </div>
</template>

<script>

import axios from 'axios'

export default {
    name: 'TileComponent',
    props: ['user'],
    methods: {
        submit(){

            axios.post('http://localhost:7000/supervisors', {
                user_id: this.user_id,
                phone: this.phone,
                location: this.location
            })
            .then(response=>{
                console.log(response.data)
                if (response.status === 200) {
                    this.success = 'Supervisor created successfully!'
                }
                else if (response.status === 409) {
                    console.log('Note: Email or Password is incorrect')
                    this.error = 'Supervisor already exists'
                }
            })
            .catch(error=>{
                this.error = 'Error creating supervisor'+error
            })

        },
        loadUsers() {
            axios
                .get('http://localhost:7000/auth/users/role/supervisor')
                .then(response => {
                this.supervisors = response.data;
                })
                .catch(error => {
                console.log(error);
                });
        },
        getSupervisors() {
            axios.get('http://localhost:7000/auth/users/role/supervisor')
                .then(response => {
                    console.log(response.data['username'])
                    return response.data['username']
                })
                .catch(error => {
                    console.log(error)
                })
        },
        completeSupervisor(user_id) {
            axios.post('http://localhost:7000/supervisors/'+user_id,{
                username: this.username,
                email: this.email,
                password: this.password,
                role: 'supervisor'
            })
            .then(response => {
                this.users = response.data('users')
            })
            .catch(error => {
                console.log(error)
            })
        },
    },
}

</script>

<style scoped>
.tile{
    background-color: var(--primary-color);
    padding: 20px;
    border-radius: 20px;
    color: white;
}
.tile h3{
    margin-bottom: 10px;
    text-transform: capitalize;
}
</style>