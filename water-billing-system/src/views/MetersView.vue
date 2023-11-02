<template>
    <div class="d-flex justify-content-between top-head">
        <h2>Meters Page</h2>
        <button class="btn info" @click="meterModal = true" > <i class="bi bi-pencil-fill"></i>Register meter</button>
    </div>
    <hr>

    <!-- <hr> -->
    <WorkerComponent v-if="meterModal" @close="meterModal = false">
        <h2>Register meter</h2>
        <hr>
        <form action="" class="">
            <input type="text" v-model="meter_number" placeholder="Meter number">
            <input type="text" v-model="meter_type" placeholder="Meter type">
            <input type="datetime-local" v-model="installation_date" placeholder="Installation date">
            <input type="text" v-model="gps_coordinates" placeholder="Map Co-ordinates">
            <button class="btn btn-info">Add</button>
        </form>
    </WorkerComponent>

    <div class="row">
        <div v-if="meters.length > 0">
            <div v-for="meter in meters" :key="meter.id" class="col-md-4">
                <p><b>Meter Number: </b>{{ meter.meter_number  }}</p>
                <p><b>Meter Type: </b>{{ meter.meter_type }}</p>
                <p><b>Installation date: </b>{{ meter.installation_date }}</p>
            </div>
        </div>
        <div v-else>
            <p class="text-danger"> {{ error }} </p>
        </div>
    </div>



</template>

<script>
import WorkerComponent from '@/components/WorkerComponent.vue';
import axios from 'axios';


export default {
    name: 'MetersView',
    components: {
        WorkerComponent
    },
    data() {
        return {
            meters : [],
            error: null,
            meter_number: '',
            meter_type: '',
            installation_date: '',
            gps_coordinates: '',
            meterModal: false,
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
        }
    },
    mounted() {
        this.getMeters();
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