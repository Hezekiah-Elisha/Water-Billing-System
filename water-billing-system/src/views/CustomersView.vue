<template>
<div class="row">
    <div class="col-md-2">
        <SideNav/>
    </div>
    <div class="col-md-10">
        <h1>Customers Page</h1>
        <button @click="customerModal = true">Create Customer</button>
        <WorkerComponent v-if="customerModal" @close="customerModal = false">
            <h2>Create Customer</h2>
            <hr>
            <form @submit.prevent="submit">
                <input type="text" v-model="name" placeholder="Customer name">
                <input type="text" v-model="phone" placeholder="Customer phone">
                <input type="text" v-model="email" placeholder="Customer email">
                <input type="text" v-model="location" placeholder="Customer location">
                <button class="btn btn-info">Add</button>
            </form>
        </WorkerComponent>
        <div class="row">
            <div v-for="customer in customers" :key="customer.id" class="customer col-md-3">
                <h3> <i class="bi bi-person-fill"></i> {{ customer.name }}</h3>
                <p> <i class="bi bi-telephone-fill"></i> {{ customer.phone }}</p>
                <p> <i class="bi bi-envelope-paper-fill"></i> {{ customer.email }}</p>
                <p> <i class="bi bi-geo-alt-fill"></i> {{ customer.location }}</p>
            </div>
        </div>

            
    </div>
</div>
    
</template>

<script>
import axios from 'axios';
import WorkerComponent from '@/components/WorkerComponent.vue';
import SideNav from '@/components/SideNav.vue';

export default {
    name : 'CustomersView',
    components: {
        SideNav,
        WorkerComponent
    },
    data(){
        return{
            customers: [],
            error: null,
            customerModal: false,
            name: '',
            phone: '',
            email: '',
            location: ''
        }
    },
    methods: {
        getCustomers(){
            axios.get('customers')
            .then(response => {
                this.customers = response.data;
            })
            .catch(error => {
                console.log(error);
            })
        },
        submit() {
            axios.post('customers', {
                name: this.name,
                phone: this.phone,
                email: this.email,
                location: this.location
            })
            .then(response => {
                console.log(response.data);
                this.getCustomers();
                this.customerModal = false;
            })
            .catch(error => {
                console.log(error);
            })
        }
    },
    created(){
        this.getCustomers();
    }
}

</script>

<style scoped>

button{
    background-color: var(--primary-color);
    color: var(--secondary-color);
    border: none;
    padding: 10px;
    border-radius: 5px;
    margin: 10px;
}

button:hover{
    background-color: var(--secondary-color);
    color: var(--primary-color);
    box-shadow: 0 0 10px var(--secondary-color);
}
 
.customer{
    background-color: var(--primary-color);
    color: var(--secondary-color);
    border-radius: 5px;
    padding: 10px;
    margin: 10px;
}

.customer:hover{
    background-color: var(--secondary-color);
    color: var(--primary-color);
    cursor: pointer;
    /* glow effect */
    box-shadow: 0 0 10px var(--secondary-color);
}

.customer h3{
    font-size: 22px;
}

.customer p{
    font-size: 18px;
    color: aliceblue;
}
</style>