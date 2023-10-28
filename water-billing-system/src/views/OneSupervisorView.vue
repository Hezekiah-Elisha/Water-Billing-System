<template>
    <!-- Supervisor {{ $route.params.id }} -->
    <h2>Supervisor <span>{{ user.username }}</span></h2>
    <hr>
    <p>Email: {{ user.email }}</p>

    <div v-if="isThere">
        <p>Phone: {{ phone }}</p>
        <p>Location: {{ location }}</p>

        <h3>Assign Workers</h3>
        <hr>
        <table>
            <thead>
                <tr>
                    <th>Username</th>
                    <th>Email</th>
                    <th>Role</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="worker in workers" :key="worker.id">
                    <td>{{ worker.username }}</td>
                    <td>{{ worker.email }}</td>
                    <td>{{ worker.role }}</td>
                    <td>
                        
                        <button @click="deleteWorker(worker.id)"
                            class="btn btn-outline-danger">
                            <i class="bi bi-trash2"></i>Delete
                        </button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>

    <div v-else>
        <h3>Complete Supervisor Registration</h3>
        <button class="btn action" @click="supervisorModal = true" > <i class="bi bi-pencil-fill"></i> Create Supervisor</button>
        <WorkerComponent v-if="supervisorModal" @close="supervisorModal = false">
            <h2>Create Supervisor</h2>
            <hr>
            <form @submit.prevent="submit">
                <!-- <label for="">Username</label> -->
                <input v-model="phone" type="number" placeholder="Phone Number" min="0">
                <!-- <label for="">Email</label> -->
                <input v-model="location" type="text" placeholder="Location">
                <!-- <label for="">Password</label> -->
                <button class="btn action">Complete registration</button>
            </form>

        </WorkerComponent>
    </div>
</template>

<script>
import axios from 'axios'
import WorkerComponent from '@/components/WorkerComponent.vue'

export default {
    name : 'OneSupervisorView',
    components: {
        WorkerComponent
    },
    data() {
        return {
            user : {},
            phone: '',
            location: '',
            isThere: false,
            supervisorModal: false,
            workers: {}
        }
    },
    methods: {
        loadUser() {
            axios
                .get('http://localhost:7000/auth/users/'+this.$route.params.id)
                .then(response => {
                this.user = response.data;
                // console.log(response.data)
                })
                .catch(error => {
                console.log(error);
                });
        },
        submit() {
            axios.post('http://localhost:7000/supervisors', {
                user_id: this.$route.params.id,
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
        checkSupervisor() {
            axios.get('http://localhost:7000/supervisors/'+this.$route.params.id)
                .then(response => {
                    // console.log(response.data)
                    if (response.data['message'] === 'Supervisor does not exist') {
                        this.isThere = false
                    }
                    else {
                        this.isThere = true
                        this.phone = response.data['supervisor']['phone']
                        this.location = response.data['supervisor']['location']
                    }
                })
                .catch(error => {
                    console.log(error)
                })
        },
        getWorkers() {
            axios.get('http://localhost:7000/auth/users/role/worker')
                .then(response => {
                    console.log(response.data)
                    this.workers = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        },

    },
    created() {
        this.loadUser()
        this.checkSupervisor()
        this.getWorkers()
    }
}


</script>

<style scoped>
h2, span{
    text-transform: capitalize;
}
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