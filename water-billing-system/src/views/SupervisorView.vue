<template>
    <div class="container">
        <h1>Supervisor View</h1>
        <h2>Create Supervisor</h2>

        <div class="supervisor container">
            <form @submit.prevent="submit">
                <select v-model="user_id" name="" id="">
                    <option value="" selected>Select User</option>
                    <option v-for="user in users" :key="user.id" :value="user.id"> {{ user.id}}</option>
                </select>
                <input v-model="phone" type="number" placeholder="Phone Number" min="0" max="0800000000">
                <input v-model="location" type="text" placeholder="location">
                <button type="submit">Create</button>
                <p class="text-danger">{{ error }}</p>
                <p class="text-success">{{ success }}</p>
            </form>
        </div>
        <div>
            <h2>Available Supervisors</h2>
        </div>
    </div>
</template>

<script>

import axios from 'axios'

export default {
    name: 'SupervisorView',
    data() {
        return {
            users: [],
            user_id: '',
            phone: '',
            location: '',
            error: '',
            success: '',
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
        getUsername(id) {
            axios.get('http://localhost:7000/auth/users/' + id+'/username')
                .then(response => {
                    console.log(response.data['username'])
                    return response.data['username']
                })
                .catch(error => {
                    console.log(error)
                })
        },
    },
    mounted(){
        axios.get('http://localhost:7000/auth/users/role/supervisor')
                .then(response => {
                    this.users = response.data
                })
                .catch(error => {
                    console.log(error)
                })
    },


    // created() {
    //     this.getUsername()
    // }
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