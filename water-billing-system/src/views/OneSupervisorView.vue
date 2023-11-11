<template>
<div class="row">
    <div class="col-md-2">
        <SideNav/>
    </div>
    <div class="col-md-10">
        <!-- Supervisor {{ $route.params.id }} -->
        <h2>Supervisor <span>{{ user.username }}</span></h2>
        <hr>
        <p>Email: {{ user.email }}</p>

        <div v-if="isThere">
            <p>Phone: {{ phone }}</p>
            <p>Location: {{ location }}</p>

            <h3>Assign Workers</h3>
            <hr>
            <div class="row tiles workers">
                <div v-for="worker in workers" :key="worker.id" class="col-md-4">
                    <h4>{{ worker.username }}</h4>
                    <hr>
                    <p>{{ worker.email }}</p>
                    <p>{{ worker.role }}</p>
                    <button @click="deleteWorker(worker.id)"
                                    class="btn btn-outline-warning">
                        <i class="bi bi-person-fill-add"></i> Self Assign
                    </button>

                </div>
            </div>


            <h3>Workers</h3>
            <hr>
            <div class="row">
                <WorkerTileComponent v-for="worker in workers" :key="worker.id" :user="worker" class="col-md-4"/>
            </div>
        </div>

        <div v-else>
            <h3>Complete Supervisor Registration</h3>
            <button class="btn action" @click="supervisorModal = true" > <i class="bi bi-pencil-fill"></i>Complete Supervisor Registration</button>
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
    </div>
</div>
</template>

<script>
import axios from 'axios'
import WorkerComponent from '@/components/WorkerComponent.vue'
import WorkerTileComponent from '@/components/WorkerTileComponent.vue'
import SideNav from '@/components/SideNav.vue'

export default {
    name : 'OneSupervisorView',
    components: {
        WorkerComponent,
        WorkerTileComponent,
        SideNav
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

.tiles{
    padding: 20px;
}
.workers div{
    /* margin: 5px; */
    padding: 10px;
    border: 1px solid #001f3f;
    border-radius: 5px;
    background-color: #001f3f;
    color: #fff;
}

.workers div h4{
    text-transform: capitalize;
}
</style>