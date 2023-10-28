<template>
    <div class="container">
        <h2>Available Supervisors</h2>


        <table class="table table-hover">
            <thead>
                <tr>
                    <th>Username</th>
                    <th>Email</th>
                    <th>role</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="supervisor in supervisors" :key="supervisor.id">
                    <td>{{ supervisor.username }}</td>
                    <td>{{ supervisor.email }}</td>
                    <td>{{ supervisor.role }}</td>
                    <td>
                        <router-link
                            :to="{ name: 'supervisor', params: { id: supervisor.id } }"
                            class="btn btn-outline-primary">
                            Edit profile
                        </router-link>

                        <button @click="deleteSupervisor(supervisor.id)"
                            class="btn btn-outline-danger">
                            <i class="bi bi-trash2"></i>Delete
                        </button>
                    </td>
                </tr>
            </tbody>
        </table>


        <div class="supervisor container">
            <form @submit.prevent="submit">
                <select v-model="user_id" name="" id="">
                    <option value="" selected>Select User</option>
                </select>
                <input v-model="phone" type="number" placeholder="Phone Number" min="0" max="0800000000">
                <input v-model="location" type="text" placeholder="location">
                <button type="submit">Create</button>
                <p class="text-danger">{{ error }}</p>
                <p class="text-success">{{ success }}</p>
            </form>
        </div>
        <div>
        </div>
    </div>
</template>

<script>

import axios from 'axios'

export default {
    name: 'SupervisorView',

    data() {
        return {
            supervisors: [],
            user_id: '',
            phone: '',
            location: '',
            error: '',
            success: '',
            isThere: false,
            supervisorModal: false,
        }
    },
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
    mounted(){
        this.loadUsers()

    },

}

</script>

<style scoped>
.supervisor {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

form {
  width: 400px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
}

form h2 {
  font-size: 2rem;
  color: #333;
}

form input {
  width: 100%;
  height: 40px;
  border: 1px solid #001f3f;
  padding: 0 20px;
  font-size: 1rem;
  margin: 10px;

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

form select{
    width: 100%;
    height: 40px;
    border: 1px solid #001f3f;
    padding: 0 20px;
    font-size: 1rem;
}

</style>