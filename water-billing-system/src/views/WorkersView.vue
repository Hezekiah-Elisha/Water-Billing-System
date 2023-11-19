<template>
<div class="row">
    <div class="col-md-2">
        <SideNav/>
    </div>
    <div class="col-md-10">
        <div class="container">
            <h2>Available workers</h2>
            <hr>
            <div class="row">
                <div v-for="worker in workers" :key="worker.id" class="col-md-4 tiles">
                    <WorkerTileComponent :user="worker">
                        <div class="row">
                            <RouterLink :to="{ name: 'worker', params: { id: worker.id } }" class="btn btn-info">View</RouterLink>
                        </div>
                    </WorkerTileComponent>
                </div>
            </div>

        </div>
    </div>
</div>
</template>

<script>

import WorkerTileComponent from '@/components/WorkerTileComponent.vue'
import axios from 'axios'
import SideNav from '@/components/SideNav.vue'

export default {
    name: 'SupervisorView',
    components: {
        WorkerTileComponent,
        SideNav
    },
    data() {
        return {
            workers: [],
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

            axios.post('worker', {
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
                .get('auth/users/role/worker')
                .then(response => {
                this.workers = response.data;
                })
                .catch(error => {
                console.log(error);
                });
        },
        getSupervisors() {
            axios.get('auth/users/role/worker')
                .then(response => {
                    console.log(response.data['username'])
                    return response.data['username']
                })
                .catch(error => {
                    console.log(error)
                })
        },
        completeSupervisor(user_id) {
            axios.post('workers/'+user_id,{
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

.tiles{
    padding: 20px;
}
</style>