<template>
<div class="row">
    <div class="col-md-2">
        <SideNav/>
    </div>
    <div class="col-md-10">
        <h1>Bills Page</h1>
        <hr>
        <button @click="deleteBills" class="btn btn-info">Delete All</button>
        <div class="row">
            <div v-for="bill in bills" :key="bill.id" class="col-md-4">
                <h3><b>Meter ID: </b>{{ bill.meter_id }}</h3>
                <p><b>Amount: </b>{{ bill.amount }}</p>
                <p><b>Status</b>{{ bill.status }}</p>
                <p>{{ bill.user_id }}</p>
                <p><b>units:</b>  {{ bill.units }}</p>
                <p><b>Time Calculated: </b>{{ bill.created_at }}</p>
            </div>

        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios';

import SideNav from '@/components/SideNav.vue';

export default {
    name: 'BillsView',
    components: {
        SideNav
    },
    data() {
        return {
            bills: []
        }
    },
    methods: {
        getBills() {
            axios.get('bills')
            .then(response => {
                this.bills = response.data.bills;
            })
            .catch(error => {
                console.log(error);
            })
        },
        deleteBill(id) {
            axios.delete(`bills/${id}`)
            .then(response => {
                this.bills = response.data.bills;
            })
            .catch(error => {
                console.log(error);
            })
        },
        deleteBills() {
            axios.delete('bills')
            .then(response => {
                this.bills = response.data.bills;
            })
            .catch(error => {
                console.log(error);
            })
        }
    },
    mounted() {
        this.getBills();
    }
}

</script>