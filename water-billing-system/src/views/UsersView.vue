<template>
<div class="row">
    <div class="col-md-2">
        <SideNav/>
    </div>
    <div class="col-md-10">
        <h1>Users</h1>

    <button @click="workerModal = true" class="btn action"><i class="bi bi-person-fill-add"></i>Create worker</button>
        <WorkerComponent v-if="workerModal" @close="workerModal = false">
            <h2>Create Worker</h2>
            <hr>
            <form @submit.prevent="createWorker">
                <!-- <label for="">Username</label> -->
                <input v-model="username" type="text" placeholder="Username" required>
                <!-- <label for="">Email</label> -->
                <input v-model="email" type="email" placeholder="Email" required>
                <!-- <label for="">Password</label> -->
                <input v-model="password" type="password" placeholder="Password" required>
                <!-- <label for="">Location</label> -->
                            
                <button class="btn action">Add</button>
            </form>

        </WorkerComponent>

        <button class="btn action" @click="supervisorModal = true" > <i class="bi bi-person-plus-fill"></i> Create Supervisor</button>
        <WorkerComponent v-if="supervisorModal" @close="supervisorModal = false">
            <h2>Create Supervisor</h2>
            <hr>
            <form @submit.prevent="createSupervisor">
                <!-- <label for="">Username</label> -->
                <input v-model="username" type="text" placeholder="Username">
                <!-- <label for="">Email</label> -->
                <input v-model="email" type="text" placeholder="Email">
                <!-- <label for="">Password</label> -->
                <input v-model="password" type="password" placeholder="Password">
                <!-- <label for="">Location</label> -->
                <button class="btn action">Add</button>
            </form>

        </WorkerComponent>
        <button @click="deleteUsers" class="btn btn-outline-danger">
            <i class="bi bi-trash"></i>Delete all
        </button>


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
    </div>
</div>

    
</template>

<script>
import axios from 'axios'
import WorkerComponent from '@/components/WorkerComponent.vue'
import SideNav from '@/components/SideNav.vue'


export default {
    name: 'UsersView',
    components: {
        WorkerComponent,
        SideNav
    },
    data() {
        return {
            users: [],
            workerModal: false,
            supervisorModal: false,
            username: '',
            email: '',
            password: '',
            role: ''
        }
    },
    methods: {
        deleteUsers(){
            axios.delete('http://localhost:7000/users')
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
                this.users = response.data['users']
                console.log(response.data)
            })
            .catch(error => {
                console.log(error)
            })
        },
        loadUsers() {
            axios
                .get('http://localhost:7000/auth/users')
                .then(response => {
                this.users = response.data;
                })
                .catch(error => {
                console.log(error);
                });
        },
        createWorker() {
            axios.post('http://localhost:7000/auth',{
                username: this.username,
                email: this.email,
                password: this.password,
                role: 'worker'
            })
            .then(response => {
                this.users = response.data['users']
            })
            .catch(error => {
                console.log(error)
            })
        },
        createSupervisor() {
            axios.post('http://localhost:7000/auth',{
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
    // created() {
    //     this.getUsers()
    // },
    mounted() {
        this.loadUsers()
    }
}

</script>

<style scoped>

.action {
    padding: 5px 10px;
    background-color: var(--primary-color);
    color: var(--secondary-color);
    border: none;
    margin: 0 10px;
}

.action:hover {
    background-color: var(--secondary-color);
    color: var(--primary-color);
}


form button{
    width: 30%;
}

input, select{
    margin: 10px auto;
    display: block;
    width: 80%;
    border: 1px solid #001f3f;
    padding: 10px;
    /* border-bottom: 1px solid #001f3f; */
}

input:focus {
    outline: none;
}

/* center the placeholders */
input::placeholder {
  text-align: center;
}
</style>