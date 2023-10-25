<template>
    <h1>Users</h1>
    <div v-if="users.length != 0">
        <table class="table table-hover">
            <thead>
                <tr>
                    <th>Username</th>
                    <th>Email</th>
                    <th>Role</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr
                    v-for="user in users"
                    :key="user.id">
                    <td>{{ user.username }}</td>
                    <td>{{ user.email }}</td>
                    <td>{{ user.role }}</td>
                    <td>
                        <!-- <router-link
                            :to="{ name: 'UserEdit', params: { id: user.id } }"
                            class="btn btn-outline-primary">
                            Edit
                        </router-link> -->
                        <button
                            @click="deleteUser(user.id)"
                            class="btn btn-outline-danger">
                            <i class="bi bi-trash2"></i>Delete
                        </button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    <h1 v-else>
        None Yet
    </h1>
    <button @click="deleteUsers" class="btn btn-outline-danger">
        <i class="bi bi-trash"></i>Delete all
    </button>
    
</template>

<script>
import axios from 'axios'

export default {
    name: 'UsersView',
    data() {
        return {
            users: []
        }
    },
    methods: {
        deleteUsers(){
            axios.delete('http://localhost:7000/auth/users')
            .then(response => {
                this.users = response.data
            })
            .catch(error => {
                console.log(error)
            })
        },
        deleteUser(id) {
            axios.delete(`http://localhost:7000/auth/users/${id}`)
            .then(response => {
                this.users = response.data
            })
            .catch(error => {
                console.log(error)
            })
        }
    },
    // created() {
    //     this.getUsers()
    // },
    mounted() {
        axios.get('http://localhost:7000/auth/users')
            .then(response => {
                this.users = response.data
            })
            .catch(error => {
                console.log(error)
            })
    }
}

</script>

<style scoped>


</style>