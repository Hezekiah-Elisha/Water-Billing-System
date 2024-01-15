<template>
<div class="row">
    <div class="col-md-2">
        <SideNav/>
    </div>
    <div class="col-md-10">
        <h2>Meter Reading Package</h2>
        <hr>
        <button @click="delete_all" class="btn btn-info"> <i class="bi bi-trash2-fill"></i> Delete all</button>
        <div class="row tiles workers">
            <div v-for="meterReading in meterReadings" :key="meterReading.id" class="col-md-4 info">
                <h4>{{ meter_info(meterReading.meter_id) }}</h4>
                <hr>
                <img :src="'https://hezekiahelisha.pythonanywhere.com/meters/readings/uploads/'+meterReading.reading_image" class="img-fluid" :alt="meterReading.reading_image">
                <p>Reading: {{ meterReading.reading_value }}</p>
                <p> <i class="bi bi-geo-alt-fill"></i> {{ meterReading.reading_gps_coordinates }}</p>
                <p> <i class="bi bi-calendar-fill"></i> {{ meterReading.reading_date }}</p>
                <p> <i class="bi bi-journal-bookmark-fill"></i> {{ meterReading.meter_status }}</p>
                <p> <i class="bi bi-clock-history"></i> {{ meterReading.created_at }}</p>
                <button class="btn btn-info w-100">
                    <i class="bi bi-eye-fill"></i> View
                </button>
            </div>
        </div>
    </div>
</div>


</template>

<script>
import axios from 'axios'
import SideNav from '@/components/SideNav.vue';

export default {
    name: 'MeterReadingsView',
    components: {
        SideNav
    },
    data() {
        return {
            meterReadings: {},
            meter: {}
        }
    },
    methods: {
        loadMeterReadings() {
            axios
                .get('meters/readings')
                .then(response => {
                this.meterReadings = response.data;
                console.log(response.data)
                })
                .catch(error => {
                console.log(error);
                });
        },
        meter_info(meter_id){
            axios
                .get('meters/'+meter_id)
                .then(response => {
                this.meter = response.data;
                console.log(response.data)
                })
                .catch(error => {
                console.log(error);
                });
        },
        delete_all(){
            axios
                .delete('meters/readings')
                .then(response => {
                    this.meterReadings = response.data["readings"];
                    console.log(response.data)
                }).catch(error => {
                    console.log(error);
                });
        }
    },
    mounted() {
        this.loadMeterReadings(),
        this.meter_info()
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

.info img{
    width: 100%;
    height: 200px;
    object-fit: cover;
}

</style>