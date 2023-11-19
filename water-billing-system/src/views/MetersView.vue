<template>
<div class="row">
    <div class="col-md-2">
        <SideNav/>
    </div>
    <div class="col-md-10">
        <div class="d-flex justify-content-between top-head">
            <h2>Meters Page</h2>
            <button class="btn info" @click="meterModal = true" > <i class="bi bi-pencil-fill"></i>Register meter</button>
        </div>
        <hr>

        <!-- <hr> -->
        <WorkerComponent v-if="meterModal" @close="meterModal = false">
            <h2>Register meter</h2>
            <hr>
            <form @submit.prevent="submit">
                <select v-model="customer_id">
                    <option value="">Select customer</option>
                    <option v-for="customer in customers" :key="customer.id" :value="customer.id">{{ customer.name }}</option>
                </select>
                <input type="text" v-model="meter_number" placeholder="Meter number">
                *Must start with NWC(number)
                <input type="text" v-model="meter_type" placeholder="Meter type">
                <input type="datetime-local" v-model="installation_date" placeholder="Installation date">
                <input type="text" v-model="gps_coordinates" placeholder="Map Co-ordinates">
                <button class="btn btn-info">Add</button>
            </form>
        </WorkerComponent>

        <!-- <div class="row"> -->
            <div v-if="meters.length > 0" class="row">
                <div v-for="meter in meters" :key="meter.id" class="col-md-4">
                    <p><b>Meter Number: </b>{{ meter.meter_number  }}</p>
                    <p><b>Customer: </b> None of ID _{{ meter.customer_id }}</p>
                    <p><b>Meter Type: </b>{{ meter.meter_type }}</p>
                    <p><b>Installation date: </b>{{ meter.installation_date }}</p>
                </div>
            </div>
            <div v-else>
                <p class="text-danger"> {{ error }} </p>
            </div>
        <!-- </div> -->
    </div>
</div>



</template>

<script>
import WorkerComponent from '@/components/WorkerComponent.vue';
import SideNav from '@/components/SideNav.vue';
import axios from 'axios';


export default {
    name: 'MetersView',
    components: {
        WorkerComponent,
        SideNav
    },
    data() {
        return {
            meters : [],
            error: null,
            customer_id: '',
            meter_number: '',
            meter_type: '',
            installation_date: '',
            gps_coordinates: '',
            meterModal: false,
            customers: [],
            customer: []
        };
    },
    methods: {
        getMeters(){
            axios.get('meters')
            .then(response => {
                this.meters = response.data;
            })
            .catch(error => {
                // console.log(error);
                this.error = `${error.response.data.message}`;
                // this.meters = "An error occured. Check the console for details.";
            })
        },
        getAllCustomers(){
            axios.get('customers')
            .then(response => {
                this.customers = response.data;
            })
            .catch(error => {
                // console.log(error);
                this.error = `${error.response.data.message}`;
                // this.meters = "An error occured. Check the console for details.";
            })
        },
        submit(){
            console.log(this.installation_date)

            // Create a new Date object from the installation_date
            let date = new Date(this.installation_date);

            // Format the date in the desired format
            let formattedDate = `${date.getFullYear()}-${('0' + (date.getMonth() + 1)).slice(-2)}-${('0' + date.getDate()).slice(-2)} ${('0' + date.getHours()).slice(-2)}:${('0' + date.getMinutes()).slice(-2)}:${('0' + date.getSeconds()).slice(-2)}`;

            console.log(formattedDate)

            axios.post('meters', {
                customer_id: this.customer_id,
                meter_number: this.meter_number,
                meter_type: this.meter_type,
                installation_date: formattedDate,
                gps_coordinates: this.gps_coordinates
            })
            .then(response => {
                console.log(response.data);
                this.getMeters();
                this.meterModal = false;
            })
            .catch(error => {
                console.log(error);
            })
        },
        getCustomerByID(id){
            axios.get(`customers/${id}`)
            .then(response => {
                this.customer = response.data;
                console.log(this.customer)
            })
            .catch(error => {
                console.log(error);
            })
        }
    },
    mounted() {
        this.getMeters();
        this.getAllCustomers();
        this.getCustomerByID(3);
    }

}

</script>

<style scoped>

.info{
    background-color: var(--primary-color);
    color: white;
    border-radius: 10px;
    padding: 10px;
    /* margin: 10px; */

}

.top-head{
    padding-left: 20px;
    padding-right: 20px;
}

.row .col-md-4{
    background-color: var(--primary-color);
    color: white;
    border-radius: 10px;
    padding: 20px;
}

form {
        /* display: flex;
        flex-direction: column; */
        /* width: 50%; */
        text-align: center;
        justify-content: center;
    }

    form input {
        margin-bottom: 10px;
    }

    form select {
        margin-bottom: 10px;
    }

    form button {
        margin-bottom: 10px;
    }

    form option{
        text-transform: capitalize;
    }

</style>